import pytest

from juno.api.interface import ApiRequester
from juno.constants import PLATFORM


class TestApiRequester:
    @pytest.mark.parametrize(
        'uri, kwargs, expected_value', [
            ('/lol/v1', {'test_param': 'test'}, f'https://{PLATFORM["BR1"]}'+'/lol/v1'), # noqa
            ('/lol/v1/{test_param}', {'test_param': 'test'}, f'https://{PLATFORM["BR1"]}'+'/lol/v1/test'), # noqa
            ('/lol/v1/{test1_param}/{test2_param}', {'test1_param': 'test1', 'test2_param': 'test2'}, f'https://{PLATFORM["BR1"]}'+'/lol/v1/test1/test2'), # noqa
        ]
    )
    def test_endpoint(self, uri, kwargs, expected_value):
        requester = ApiRequester('BR1')
        assert requester._get_endpoint(uri, kwargs) == expected_value
