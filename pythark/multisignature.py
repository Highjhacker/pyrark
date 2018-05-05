from .api import API


class MultiSignature(API):
    """
    Operations for MultiSignatures.
    """

    def get_pending(self, publicKey):
        """ Get pending multi signatures transactions.

        :param publicKey: A valid Ark publicKey.
        :return:
        """
        resp = self.request('get', "api/multisignatures/pending", publicKey=publicKey)
        return resp.json()

    def get_accounts(self, publicKey):
        # TypeError: NetworkError when attempting to fetch resource.
        """ Get a list of accounts.

        :param publicKey: A valid Ark publicKey.
        :return:
        """
        resp = self.request('get', "api/multisignatures/accounts", publicKey=publicKey)
        return resp.json()
