from .api import API


class Loader(API):
    """
    Operations for Loaders.
    """
#    def __init__(self):
#        self.api = API()

    def get_status(self):
        """ Get the blockchain status.

        :return:
        """
        resp = self.request('get', "api/loader/status")
        return resp.json()

    def get_sync(self):
        """ Get the synchronisation status of the client.

        :return:
        """
        resp = self.request('get', "api/loader/status/sync")
        return resp.json()

    def autoconfigure(self):
        """ Auto-configure the client Loader.

        :return:
        """
        resp = self.request('get', "api/loader/autoconfigure")
        return resp.json()