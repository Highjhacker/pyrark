from .api import API


class Account(API):
    """
    Operations for Accounts.
    """

    def get_balance(self, address):
        """ Get the balance of an account.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "api/accounts/getBalance", address=address)
        return resp.json()

    def get_public_key(self, address):
        """ Get the public key of an account.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "api/accounts/getPublickey", address=address)
        return resp.json()

    def get_delegate_fee(self):
        """ Get the delegate fee of an account.

        :return:
        """
        resp = self.request('get', "api/accounts/delegates/fee")
        return resp.json()

    def get_delegates(self, address, **kwargs):
        """ Get the delegates of an account.

        :param address: A valid Ark address.
        :param kwargs: Optional parameters. orderBy, limit, offset
        :return:
        """
        resp = self.request('get', "api/accounts/delegates", address=address, **kwargs)
        return resp.json()

    def get_accounts(self, address):
        """ Get account information of an address.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "api/accounts", address=address)
        return resp.json()

    def get_top_accounts(self, **kwargs):
        """ Get a list of top account

        :param kwargs: Optional parameters. limit, offset
        :return:
        """
        resp = self.request('get', "api/accounts/top", **kwargs)
        return resp.json()
