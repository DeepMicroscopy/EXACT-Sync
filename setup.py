import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EXACT-Sync", 
    version="0.0.39",
    author="Christian Marzahl, Marc Aubreville",
    author_email="marc.aubreville@hs-flensburg.de",
    description="A package to download images and annotations from the EXACT Server https://github.com/DeepMicroscopy/Exact",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepMicroscopy/EXACT-Sync",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 
        'tqdm', 
        'requests-toolbelt',
        'pillow',
        "locust==1.1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


#python -m build
#python -m twine upload dist/*
