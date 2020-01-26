from django.urls import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize("path,code,redirect", [('index', 200, None), ('eve_auth:login', 302, 'https://login.eveonline.com/v2/oauth/authorize'), ('eve_auth:logout', 302, '/')])
def test_urls(client, path, code, redirect):
    request = client.get(reverse(path))
    assert request.status_code == code
    if redirect:
        assert request.url.startswith(redirect)