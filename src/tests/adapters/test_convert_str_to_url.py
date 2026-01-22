import pytest

from building_web_browser_from_scratch.adapters import ConvertStrToUrl
from building_web_browser_from_scratch.core.models import URL, SchemesEnum

@pytest.fixture
def convert_str_to_url():
    return ConvertStrToUrl()

class TestInit:
    def test_if_raises_type_error_when_input_is_not_a_str(self):
        with pytest.raises(TypeError):
            ConvertStrToUrl(input=123)

class TestRun:
    def test_case_1(self, convert_str_to_url : ConvertStrToUrl):
        url = 'https://www.example.com/index.html'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTP
        assert url.hostname == 'www.example.com'
        assert url.path == '/index.html'

    def test_case_2(self, convert_str_to_url : ConvertStrToUrl):
        url = 'https://developer.mozilla.org/en-US/docs/Web/HTTP'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTPS
        assert url.hostname == 'developer.mozilla.org'
        assert url.path == '/en-US/docs/Web/HTTP'

    def test_case_3(self, convert_str_to_url : ConvertStrToUrl):
        url = 'https://api.github.com/users/octocat/repos'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTPS
        assert url.hostname == 'api.github.com'
        assert url.path == '/users/octocat/repos'

    def test_case_4(self, convert_str_to_url : ConvertStrToUrl):
        url = 'http://example.org/articles/2024/networking.html'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTP
        assert url.hostname == 'example.org'
        assert url.path == '/articles/2024/networking.html'

    def test_case_5(self, convert_str_to_url : ConvertStrToUrl):
        url = 'https://medium.com/@user/how-http-works-123abc'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTPS
        assert url.hostname == 'medium.com'
        assert url.path == '/@user/how-http-works-123abc'

    def test_case_6(self, convert_str_to_url : ConvertStrToUrl):
        url = 'https://www.amazon.com.br/gp/product/B0XYZ123'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTPS
        assert url.hostname == 'www.amazon.com.br'
        assert url.path == '/gp/product/B0XYZ123'

    def test_case_7(self, convert_str_to_url : ConvertStrToUrl):
        url = 'http://localhost/api/v1/health'

        url = convert_str_to_url.run(url)
        assert isinstance(url, URL)

        assert url.scheme == SchemesEnum.HTTP
        assert url.hostname == 'localhost'
        assert url.path == '/api/v1/health'


         