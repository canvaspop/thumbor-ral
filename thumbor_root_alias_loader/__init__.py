# -*- coding: utf-8 -*-
"""
    thumbor root alias loader

    Loads a resource using aliased root paths instead of showing the full
    s3 bucket url.

    Overloads the thumbor's http_loader.
"""

from thumbor.loaders import http_loader


__ALL__ = ["validate", "load", "return_contents"]


def validate(context, url):
    """Validate a url. Pass through function to http_loader.validate
    """

    url = _prepare(url)
    return http_loader.validate(context, url)


def _prepare(context, url):
    """Prepare a url, replacing the root alias with the real url.
    """

    #TODO replace the #bucket_id# with the bucket root url.
    return url


def load(context, url, callback):
    """Format the url and passes it to the base http_loader module.
    """
    url = _prepare(context, url)
    http_loader.load(context, url, callback)


def return_contents(response, url, callback):
    return http_loader.return_contents(response, url, callback)
