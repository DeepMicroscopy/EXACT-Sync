from time import sleep
import re
import logging

from exact_sync.v1.rest import ApiException

logger = logging.getLogger(__name__)

class PaginationBaseAPI(object):

    # Retry behaviour for transient gateway errors. Enabled by default; disable
    # per API object with `SomeApi(client, retry=False)` or `api.retry = False`.
    retry = True
    retry_statuses = (502, 503, 504)
    retry_max_attempts = 5
    retry_backoff = 0.5  # seconds, doubled after each failed attempt

    def _call_with_retry(self, *args, **kwargs):
        delay = self.retry_backoff
        for attempt in range(1, self.retry_max_attempts + 1):
            try:
                return self.api_client.call_api(*args, **kwargs)
            except ApiException as e:
                if e.status not in self.retry_statuses or attempt == self.retry_max_attempts:
                    raise
                logger.warning("API returned %s, retrying in %.1fs (attempt %d/%d)",
                               e.status, delay, attempt, self.retry_max_attempts)
                sleep(delay)
                delay *= 2

    def _call_api(self, *args, **kwargs):
        if not self.retry:
            return self.api_client.call_api(*args, **kwargs)
        if kwargs.pop('async_req', None):
            # keep async semantics: retry inside the worker thread
            return self.api_client.pool.apply_async(self._call_with_retry, args, kwargs)
        return self._call_with_retry(*args, **kwargs)
    
    def _get_all(self, func:callable, **kwargs):

        data = func(**kwargs)

        if kwargs.get('async_req'):
            data = data.get()
        if data.next != None:   
            threads = []             
            limit = int(re.findall("limit=([0-9]*)", data.next)[0])
            offset = int(re.findall("offset=([0-9]*)", data.next)[0])
            for page_offset in range(offset, data.count, offset):
                kwargs['offset'] = page_offset
                if kwargs.get('async_req'):
                    thread = func(**kwargs)
                    threads.append(thread)
                else:    
                    (new_data) = func(**kwargs)
                    data.results += new_data.results

            if kwargs.get('async_req'):
                while (len(threads) > 0):
                    for thread in threads:
                        if thread.ready():
                            data.results += thread.get().results
                            threads.remove(thread)
                    sleep(0.25)

            data.next = None
            data.previous = None
        return data

