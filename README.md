root alias loader (thumbor-ral) (c) 2014 Canvaspop


# Thumbor-ral
Under the hood, thumbor-ral uses the existing `http_loader` module to fetch the image.
The `http_loader` module will need to be properly configured.

## Installation
`pip install git+ssh://git@github.com/canvaspop/thumbor-ral.git`

## Configuration
Thumbor-ral requires the following configuration object: `ROOT_ALIAS_LOADER_URLS`

The `ROOT_ALIAS_LOADER_URLS` is a dictionary of key (alias) -> url prefix.

### Examples


```python
ROOT_ALIAS_LOADER_URLS={
    '#1#': 'http://my-secret-bucket.s3.amazon.com/path/to/awesomeness',
    '#2#': 'http://example.com'
}
```

`#1#/path/to/example.jpg` will map to `http://my-secret-bucket.s3.amazon.com/path/to/awesomeness/path/to/example.jpg`

`lol/path/not/found.jpg` will fail validation.
