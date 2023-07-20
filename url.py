from urllib.parse import urlparse, parse_qs


class Url():
    def __init__(self, url):
        self.url = url
        url_parse = urlparse(self.url)
        self.scheme = url_parse.scheme
        self.hostname = url_parse.hostname
        self.query = url_parse.query

    def __eq__(self, other):
        return self.url == other

    def get_scheme(self):
        return self.scheme

    def get_hostname(self):
        return self.hostname

    def get_query_params(self):
        return parse_qs(self.query)

    def get_query_param(self, key, value=None):
        query_params = self.get_query_params()
        if key not in query_params.keys():
            return value
        return query_params[key][0]


URL1 = 'http://hexlet.io?key=value&key2=value2'
URL2 = 'https://google.com:80?a=b&c=d&lala=value'


def test_url1():
    url = Url(URL1)
    assert url.get_scheme() == 'http'
    assert url.get_hostname() == 'hexlet.io'
    assert url.get_query_params() == {
        'key': ['value'],
        'key2': ['value2'],
        }
    assert url.get_query_param('key') == 'value'
    assert url.get_query_param('key2', 'lala') == 'value2'
    assert url.get_query_param('new', 'ehu') == 'ehu'
    assert url == (Url(URL1))
    assert not url == (Url(URL2))

test_url1()


