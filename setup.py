"""
thumbor_root_alias_loader
---------------

URL root alias http loader.

Allows hiding the root path to an image.

ex:
#1#/path/to/original.tiff -> //bucket.s3.amazon.com/eh/path/to/original.tiff
"""

from setuptools import setup


setup(
    name='thumbor-root-alias-loader',
    version='0.1',
    url='http://www.crated.com',
    license='Copyright 2014 DNA11 Inc.',
    author='Martin Samson',
    author_email='martin@canvaspop.com',
    maintainer='Martin Samson',
    maintainer_email='martin@canvaspop.com',
    description='URL root path alias http loader.',
    long_description=__doc__,
    packages=[
        'thumbor_root_alias_loader'
    ],
    zip_safe=True,
    include_package_data=False,
    platforms='any',
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=[
        'pytest', 'nose', 'mock'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
