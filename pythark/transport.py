from .api import API
from logzero import logger

try:
    import arky
    from arky import rest
except ImportError as error:
    logger.info("You don't have Arky installed, you can't post a new transaction without this module.")
    logger.info(error)


class Transport(API):
    """
    Operations for Transports.
    """

    def get_peers(self):
        """ Get a list of peers.

        :return:
        """
        resp = self.request('get', "peer/list")
        return resp.json()

    def get_common_blocks(self, ids):
        """ Get a list of blocks by ids

        :param ids: List of Block ids.
        :return:
        """
        resp = self.request('get', "peer/blocks/common", ids=','.join(ids))
        return resp.json()

    def get_blocks(self, address):
        """ Get all blocks.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "peer/blocks", address=address)
        return resp.json()

    def get_block(self, address):
        # Doesn't work, even the curl from Swagger, need to be checked.
        """ Get a single block.

        :param address: A valid Ark address.
        :return:
        """
        resp = self.request('get', "peer/block", address=address)
        return resp.json()

    def get_transactions(self):
        """ Get a list of transactions.

        :return:
        """
        resp = self.request('get', "peer/transactions")
        return resp.json()

    def post_transaction(self, network, recipientId, amount, secret, vendorField="", secondSecret=""):
        """ Post a new transaction.

        :param network: The network we want to use (ark, dark, ...)
        :param recipientId: A valid Ark address.
        :param amount: Amount of currency we want to transfer.
        :param secret: BIP39 seedpass.
        :param vendorField: Optional vendorField.
        :param secondSecret: Optional BIP39 second seedpass.
        :return:
        """
        rest.use(network)

        return arky.core.sendTransaction(recipientId=recipientId, amount=amount, vendorField=vendorField, secret=secret,
                                         secondSecret=secondSecret)

    def post_transaction_bis(self, recipientId, amount, secret, secondSecret="", vendorField=None):
        transactions = []

        resp = self.request('post', "peer/transactions", recipientId=recipientId, amount=amount, secret=secret, secondSecret=secondSecret, vendorField=vendorField)
        return resp.json()

    def get_transactions_from_ids(self, ids):
        """ Get a list of transactions by ids.

        :param ids: A list of valid Transaction id
        :return:
        """
        resp = self.request('get', "peer/transactionsFromIds", ids=','.join(ids))
        return resp.json()

    def get_height(self):
        """ Get the blockchain height.

        :return:
        """
        resp = self.request('get', "peer/height")
        return resp.json()

    def get_status(self):
        """ Get the blockchain status.

        :return:
        """
        resp = self.request('get', "peer/status")
        return resp.json()