# -*- coding: utf-8 -*-
"""
    thumbor root alias loader

    Loads a resource using aliased root paths instead of showing the full
    s3 bucket url.

    Overloads the thumbor's http_loader.
"""
import urllib
from thumbor.loaders import http_loader


__ALL__ = ["validate", "load", "return_contents"]


def validate(context, url):
    """Validate a url. Pass through function to http_loader.validate
    """

    url = _prepare(context, url)
    if url is False:
        return False

    return http_loader.validate(context, url)


def _prepare(context, url):
    """Prepare a url, replacing the root alias with the real url.

    Reads the ROOT_ALIAS_LOADER_URLS config dictionary, looking
    """

    config = context.config.ROOT_ALIAS_LOADER_URLS

    parts = url.split('/', 1)
    if len(parts) != 2:
        return False

    alias = config.get(urllib.unquote(parts[0]), None)

    # Skip building new url when the alias does not exists.
    if alias is None:
        return url

    parts[0] = alias

    return "/".join(parts)


def load(context, url, callback):
    """Format the url and passes it to the base http_loader module.
    """
    url = _prepare(context, url)
    http_loader.load(context, url, callback)


def return_contents(response, url, callback):
    return http_loader.return_contents(response, url, callback)
