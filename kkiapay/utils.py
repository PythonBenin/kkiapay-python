import requests
from requests.auth import HTTPBasicAuth


def make_request(method: str, url: str, data=None, json=None, auth=None, **kwargs):
    """Perform a request.
    Usage::
      >>> from .utils import make_request
      >>> req = make_request('get', 'https://api-sandbox.kkiapay.me')
    """

    try:
        r = getattr(requests, method)(
            url,
            data=data,
            json=json,
            auth=auth if not auth else HTTPBasicAuth(**auth),
            **kwargs,
        )

        return r.json()
    except requests.exceptions.RequestException as e:
        raise e
