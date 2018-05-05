from .api import API


class Delegate(API):
    """
    Operations for Delegates.
    """

    def get_delegates_count(self, address):
        """ Get the count of delegates.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "api/delegates/count", address=address)
        return resp.json()

    def search_delegates(self, query, **kwargs):
        """ Search for specific delegates.

        :param query: The name we want to search.
        :param kwargs: Optional parameters. limit
        :return:
        """
        resp = self.request('get', "api/delegates/search", q=query, **kwargs)
        return resp.json()

    def get_voters(self, publicKey):
        """ Get a list of voters for a delegate.

        :param publicKey: A valid Ark publicKey.
        :return:
        """
        resp = self.request('get', "api/delegates/voters", publicKey=publicKey)
        return resp.json()

    def get_delegate(self, username):
        """ Get a single delegate.

        :param username: The delegate's name.
        :return:
        """
        resp = self.request('get', "api/delegates/get", username=username)
        return resp.json()

    def get_delegate_publickey(self, publicKey):
        """ Get a single delegate.

        :param publicKey: A valid Ark publicKey.
        :return:
        """
        resp = self.request('get', "api/delegates/get", publicKey=publicKey)
        return resp.json()

    def get_delegates(self, **kwargs):
        """ Get all delegates.

        :param kwargs: Optional parameters. orderBy, limit, offset.
        :return:
        """
        resp = self.request('get', "api/delegates", **kwargs)
        return resp.json()

    def get_delegate_fee(self, address):
        """ Get the delegate fee.

        :param address:
        :return:
        """
        resp = self.request('get', "api/delegates/fee", address=address)
        return resp.json()

    def get_forged_by_account(self, generatorPublicKey):
        """ Get the amount of ARKs forged by an account.

        :param generatorPublicKey: A valid Ark generatorPublicKey.
        :return:
        """
        resp = self.request('get', "api/delegates/forging/getForgedByAccount", generatorPublicKey=generatorPublicKey)
        return resp.json()

    def get_next_forgers(self, address):
        """ Get the next forgers.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "api/delegates/getNextForgers", address=address)
        return resp.json()
