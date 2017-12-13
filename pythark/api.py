from .network import Network
import requests
import random

BASE_URL = "https://api.arknode.net/" # "http://37.59.129.164:4001/"
BASE_URL_DEV = "http://167.114.29.52:4002/"
BASE_URL_KAPUMAIN = "https://walletapi.kapu.one/"

FALLBACKS_MAIN_ADDRESSES = []
FALLBACKS_DEV_ADDRESSES = []
FALLBACKS_KAPU_ADDRESSES = []


class API(Network):
    """
    Class allowing us to interact with the API.
    """
    def __init__(self):
        self.network = self.set_network()

    def get(self, endpoint, **kwargs):
        """ Do a HTTP get request to a specified endpoint (with optionnal parameters).

        :param endpoint: The endpoint we want to reach.
        :param kwargs: Optionnal parameters of the query.
        :return: Request response if HTTP code is equal to 200.
        """
        payload = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        try:
            if self.network == 'main':
                headers_main = get_main_network_headers()
                r = requests.get("{0}{1}".format(BASE_URL, endpoint), headers=headers_main, params=payload, timeout=10)
            if self.network == 'dev':
                headers_dev = get_dev_network_headers()
                r = requests.get("{0}{1}".format(BASE_URL_DEV, endpoint), headers=headers_dev, params=payload, timeout=10)
            if self.network == 'kapu':
                headers_kapu_main = get_kapu_main_network_headers()
                r = requests.get("{0}{1}".format(BASE_URL_KAPUMAIN, endpoint), headers=headers_kapu_main, params=payload, timeout=10)
            if r.status_code == 200:
                return r
        except requests.exceptions.Timeout:
            if self.network == "dev":
                populate_fallback(FALLBACKS_DEV_ADDRESSES, self.network)
                url = select_random_ip(FALLBACKS_DEV_ADDRESSES) + "/"
                r = requests.get("{0}{1}".format(url, endpoint), headers=headers_dev, params=payload)
            elif self.network == "kapu":
                populate_fallback(FALLBACKS_KAPU_ADDRESSES, self.network)
                url = select_random_ip(FALLBACKS_KAPU_ADDRESSES) + "/"
                r = requests.get("{0}{1}".format(url, endpoint), headers=headers_kapu_main, params=payload)
            else:
                populate_fallback(FALLBACKS_MAIN_ADDRESSES, self.network)
                url = select_random_ip(FALLBACKS_MAIN_ADDRESSES) + "/"
                r = requests.get("{0}{1}".format(url, endpoint), headers=headers_main, params=payload)
            if r.status_code == 200:
                return r


def get_main_network_headers():
    headers = {
        "nethash": "6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988",
        "version": "1.0.1",
        "port": "4001"
    }
    return headers


def get_dev_network_headers():
    headers = {
        "nethash": "578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23",
        "version": "1.1.1",
        "port": "4002"
    }
    return headers


def get_kapu_main_network_headers():
    headers = {
        "nethash": "313ea34c8eb705f79e7bc298b788417ff3f7116c9596f5c9875e769ee2f4ede1",
        "version": "0.3.0",
        "port": "9700"
    }
    return headers


def populate_fallback(fallback, network):
    from . import Peer
    if network == 'dev':
        p = Peer("dev")
    elif network == 'kapu':
        p = Peer("kapu")
    else:
        p = Peer()
    r = p.get_peers()
    for peer in r["peers"]:
        if peer["delay"] <= 50:
            fallback.append(peer)
    return fallback


def select_random_ip(fallback):
    rand = random.choice(fallback)
    return rand['ip']
