import requests
from retrying import retry

NETWORKS = {
    'main': {
        'base_urls': [
            'https://node1.arknet.cloud/'
        ],
        'headers': {
            'nethash': '6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988',
            'version': '1.0.1',
            'port': '4001'
        }
    },
    'dev': {
        'base_urls': [
            'http://167.114.29.52:4002/'
        ],
        'headers': {
            'nethash': '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23',
            'version': '1.1.1',
            'port': '4002'
        }
    },
    'kapu': {
        'base_urls': [
            'https://walletapi.kapu.one/'
        ],
        'headers': {
            'nethash': '6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988',
            'version': '1.0.1',
            'port': '4001'
        }
    }
}


class API:
    """
    Class allowing us to interact with the API.
    """
    def __init__(self, network="main"):
        self.network = network

    @retry(stop_max_attempt_number=10, wait_fixed=10000)
    def request(self, req_type, endpoint, **kwargs):
        """ Do a HTTP request to a specified endpoint (with optional parameters).

        :param req_type: The request type. Either `get` or `post`.
        :param endpoint: The endpoint we want to reach.
        :param kwargs: Optional parameters of the query.
        :return: Request response if HTTP code is equal to 200.
        """
        payload = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        headers = NETWORKS[self.network]['headers']
        for i, base_url in enumerate(NETWORKS[self.network]['base_urls']):
            try:
                if req_type == 'post':
                    r = requests.post(base_url + endpoint, headers=headers, params=payload, timeout=10)
                elif req_type == 'get':
                    r = requests.get(base_url + endpoint, headers=headers, params=payload, timeout=10)
                else:
                    raise ValueError('Invalid request type: ' + req_type)
                if r.status_code == 200:
                    return r
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                print("URL #{} failed: {}".format(i + 1, e))
        print('Failed to process {} request'.format(req_type))
