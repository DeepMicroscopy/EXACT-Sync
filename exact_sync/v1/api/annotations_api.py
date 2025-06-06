# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import
from exact_sync.v1.api.pagination_base_api import PaginationBaseAPI
import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from exact_sync.v1.api_client import ApiClient


class AnnotationsApi(PaginationBaseAPI):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_annotation(self, **kwargs):  # noqa: E501
        """create_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Annotation body:
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_annotation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_annotation_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_annotation_with_http_info(self, **kwargs):  # noqa: E501
        """create_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Annotation body:
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_annotation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        response_type = 'Annotation'
        if isinstance(params['body'], list):
            response_type = "list[Annotation]"

        body_params = {}
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def destroy_annotation(self, id, **kwargs):  # noqa: E501
        """destroy_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_annotation(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.destroy_annotation_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.destroy_annotation_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def destroy_annotation_with_http_info(self, id, **kwargs):  # noqa: E501
        """destroy_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_annotation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `destroy_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def multiple_delete(self, id__in, **kwargs):  # noqa: E501
        """multiple_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multiple_delete(id__in=1,2,3,4, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id__in: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.multiple_delete_with_http_info(id__in, **kwargs)  # noqa: E501
        else:
            (data) = self.multiple_delete_with_http_info(id__in, **kwargs)  # noqa: E501
            return data

    def multiple_delete_with_http_info(self, id__in, **kwargs):  # noqa: E501
        """multiple_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multiple_delete_with_http_info(id__in=1,2,3,4, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id__in: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id__in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id__in' not in params or
                params['id__in'] is None):
            raise ValueError("Missing the required parameter `id__in=1,2,3,4` when calling `multiple_delete` ")  # noqa: E501

        collection_formats = {}

        path_params = {}
        query_params = []
        if 'id__in' in params:
            query_params.append(('id__in', params['id__in']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/multiple_delete/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def list_annotations(self, pagination:bool=True, **kwargs):  # noqa: E501
        """list_annotations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_annotations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str id: id
        :param str time: time
        :param str time__lte: time__lte
        :param str time__gte: time__gte
        :param str time__range: time__range
        :param str unique_identifier: unique_identifier
        :param str unique_identifier__contains: unique_identifier__contains
        :param str description: description
        :param str description__contains: description__contains
        :param str deleted: deleted
        :param str image: image
        :param str user: user
        :param str annotation_type: annotation_type
        :param str verified_by: verified_by
        :param str verified_by__range: verified_by__range
        :param str vector_x: Vector-X-Range
        :param str vector_y: Vector-Y-Range
        :param bool meta_data__isnull: Meta data is null
        :param bool vector__isnull: Vector is null
        :param int vector_type: Vector type
        :return: Annotations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if pagination:
            if kwargs.get('async_req'):
                return self.list_annotations_with_http_info(**kwargs)  # noqa: E501
            else:
                (data) = self.list_annotations_with_http_info(**kwargs)  # noqa: E501
                return data
        else:
            return self._get_all(self.list_annotations_with_http_info, **kwargs)

    def list_annotations_with_http_info(self, **kwargs):  # noqa: E501
        """list_annotations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_annotations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str id: id
        :param str time: time
        :param str time__lte: time__lte
        :param str time__gte: time__gte
        :param str time__range: time__range
        :param str unique_identifier: unique_identifier
        :param str unique_identifier__contains: unique_identifier__contains
        :param str description: description
        :param str description__contains: description__contains
        :param str deleted: deleted
        :param str image: image
        :param str user: user
        :param str annotation_type: annotation_type
        :param str verified_by: verified_by
        :param str verified_by__range: verified_by__range
        :param str vector_x: Vector-X-Range
        :param str vector_y: Vector-Y-Range
        :param bool meta_data__isnull: Meta data is null
        :param bool vector__isnull: Vector is null
        :param int vector_type: Vector type
        :return: Annotations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'id', 'id__in' 'time', 'time__lte', 'time__gte', 'time__range', 'unique_identifier', 'unique_identifier__contains', 'unique_identifier__in', 'description', 'description__contains', 'deleted', 'image', 'image__in', 'user', 'annotation_type', 'annotation_type__in', 'verified_by', 'verified_by__range', 'vector_x', 'vector_y', 'meta_data__isnull', 'vector__isnull', 'vector_type']  # noqa: E501
        all_params.append('omit')
        all_params.append('fields')
        all_params.append('expand')
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_annotations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'id__in' in params:
            query_params.append(('id__in', params['id__in']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'time__lte' in params:
            query_params.append(('time__lte', params['time__lte']))  # noqa: E501
        if 'time__gte' in params:
            query_params.append(('time__gte', params['time__gte']))  # noqa: E501
        if 'time__range' in params:
            query_params.append(('time__range', params['time__range']))  # noqa: E501
        if 'unique_identifier' in params:
            query_params.append(('unique_identifier', params['unique_identifier']))  # noqa: E501
        if 'unique_identifier__contains' in params:
            query_params.append(('unique_identifier__contains', params['unique_identifier__contains']))  # noqa: E501
        if 'unique_identifier__in' in params:
            query_params.append(('unique_identifier__in', params['unique_identifier__in']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'description__contains' in params:
            query_params.append(('description__contains', params['description__contains']))  # noqa: E501
        if 'deleted' in params:
            query_params.append(('deleted', params['deleted']))  # noqa: E501
        if 'image' in params:
            query_params.append(('image', params['image']))  # noqa: E501
        if 'image__in' in params:
            query_params.append(('image__in', params['image__in']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501
        if 'annotation_type' in params:
            query_params.append(('annotation_type', params['annotation_type']))  # noqa: E501
        if 'annotation_type__in' in params:
            query_params.append(('annotation_type__in', params['annotation_type__in']))  # noqa: E501
        if 'verified_by' in params:
            query_params.append(('verified_by', params['verified_by']))  # noqa: E501
        if 'verified_by__range' in params:
            query_params.append(('verified_by__range', params['verified_by__range']))  # noqa: E501
        if 'vector_x' in params:
            query_params.append(('vector_x', params['vector_x']))  # noqa: E501
        if 'vector_y' in params:
            query_params.append(('vector_y', params['vector_y']))  # noqa: E501
        if 'meta_data__isnull' in params:
            query_params.append(('meta_data__isnull', params['meta_data__isnull']))  # noqa: E501
        if 'vector__isnull' in params:
            query_params.append(('vector__isnull', params['vector__isnull']))  # noqa: E501
        if "vector_type" in params:
            query_params.append(('vector_type', params['vector_type']))  # noqa: E501
        if 'omit' in params:
            query_params.append(('omit', params['omit']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E50
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501
            
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_annotation(self, id, **kwargs):  # noqa: E501
        """partial_update_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_annotation(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int annotation_type:
        :param object vector:
        :param int image:
        :param int last_editor:
        :param int user:
        :param bool deleted:
        :param str description:
        :param str unique_identifier:
        :param list[int] uploaded_media_files:
        :param object meta_data:
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_annotation_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.partial_update_annotation_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def partial_update_annotation_with_http_info(self, id, **kwargs):  # noqa: E501
        """partial_update_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_annotation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param int annotation_type:
        :param object vector:
        :param int image:
        :param int last_editor:
        :param int user:
        :param bool deleted:
        :param str description:
        :param str unique_identifier:
        :param list[int] uploaded_media_files:
        :param object meta_data:
        :param last_edit_time
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'annotation_type', 'last_edit_time', 'vector', 'image', 'last_editor', 'user', 'deleted', 'description', 'unique_identifier', 'uploaded_media_files', 'meta_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `partial_update_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = {}
        if 'annotation_type' in params: 
            body_params['annotation_type'] = params['annotation_type']
        if 'vector' in params: 
            body_params['vector'] = params['vector']
        if 'image' in params: 
            body_params['image'] = params['image']
        if 'last_editor' in params: 
            body_params['last_editor'] = params['last_editor']
        if 'user' in params: 
            body_params['user'] = params['user']
        if 'deleted' in params: 
            body_params['deleted'] = params['deleted']
        if 'description' in params: 
            body_params['description'] = params['description']
        if 'unique_identifier' in params: 
            body_params['unique_identifier'] = params['unique_identifier']
        if 'uploaded_media_files' in params: 
            body_params['uploaded_media_files'] = params['uploaded_media_files']
        if 'meta_data' in params: 
            body_params['meta_data'] = params['meta_data']
        if 'last_edit_time' in params: 
            body_params['last_edit_time'] = params['last_edit_time'] 

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_annotation(self, id, **kwargs):  # noqa: E501
        """retrieve_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_annotation(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str id2: id
        :param str time: time
        :param str time__lte: time__lte
        :param str time__gte: time__gte
        :param str time__range: time__range
        :param str unique_identifier: unique_identifier
        :param str unique_identifier__contains: unique_identifier__contains
        :param str description: description
        :param str description__contains: description__contains
        :param str deleted: deleted
        :param str image: image
        :param str user: user
        :param str annotation_type: annotation_type
        :param str verified_by: verified_by
        :param str verified_by__range: verified_by__range
        :param str vector_x: Vector-X-Range
        :param str vector_y: Vector-Y-Range
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_annotation_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_annotation_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def retrieve_annotation_with_http_info(self, id, **kwargs):  # noqa: E501
        """retrieve_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_annotation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str id2: id
        :param str time: time
        :param str time__lte: time__lte
        :param str time__gte: time__gte
        :param str time__range: time__range
        :param str unique_identifier: unique_identifier
        :param str unique_identifier__contains: unique_identifier__contains
        :param str description: description
        :param str description__contains: description__contains
        :param str deleted: deleted
        :param str image: image
        :param str user: user
        :param str annotation_type: annotation_type
        :param str verified_by: verified_by
        :param str verified_by__range: verified_by__range
        :param str vector_x: Vector-X-Range
        :param str vector_y: Vector-Y-Range
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'id2', 'time', 'time__lte', 'time__gte', 'time__range', 'unique_identifier', 'unique_identifier__contains', 'description', 'description__contains', 'deleted', 'image', 'user', 'annotation_type', 'verified_by', 'verified_by__range', 'vector_x', 'vector_y']  # noqa: E501
        
        all_params.append('omit')
        all_params.append('fields')
        all_params.append('expand')

        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `retrieve_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'id2' in params:
            query_params.append(('id', params['id2']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'time__lte' in params:
            query_params.append(('time__lte', params['time__lte']))  # noqa: E501
        if 'time__gte' in params:
            query_params.append(('time__gte', params['time__gte']))  # noqa: E501
        if 'time__range' in params:
            query_params.append(('time__range', params['time__range']))  # noqa: E501
        if 'unique_identifier' in params:
            query_params.append(('unique_identifier', params['unique_identifier']))  # noqa: E501
        if 'unique_identifier__contains' in params:
            query_params.append(('unique_identifier__contains', params['unique_identifier__contains']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'description__contains' in params:
            query_params.append(('description__contains', params['description__contains']))  # noqa: E501
        if 'deleted' in params:
            query_params.append(('deleted', params['deleted']))  # noqa: E501
        if 'image' in params:
            query_params.append(('image', params['image']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501
        if 'annotation_type' in params:
            query_params.append(('annotation_type', params['annotation_type']))  # noqa: E501
        if 'verified_by' in params:
            query_params.append(('verified_by', params['verified_by']))  # noqa: E501
        if 'verified_by__range' in params:
            query_params.append(('verified_by__range', params['verified_by__range']))  # noqa: E501
        if 'vector_x' in params:
            query_params.append(('vector_x', params['vector_x']))  # noqa: E501
        if 'vector_y' in params:
            query_params.append(('vector_y', params['vector_y']))  # noqa: E501
        if 'omit' in params:
            query_params.append(('omit', params['omit']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E50
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

            
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_annotation(self, id, **kwargs):  # noqa: E501
        """update_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param Annotation body:
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_annotation_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_annotation_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_annotation_with_http_info(self, id, **kwargs):  # noqa: E501
        """update_annotation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param Annotation body:
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}
        
        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotations/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
