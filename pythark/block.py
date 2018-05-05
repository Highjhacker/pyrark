from .api import API


class Block(API):
    """
    Operations for Blocks.
    """

    def get_block(self, id):
        """ Get block by id.

        :param id: Valid Block ID.
        :return:
        """
        resp = self.request('get', "api/blocks/get", id=id)
        return resp.json()

    def get_blocks(self, **kwargs):
        """ Get all blocks.

        :param kwargs: Optional parameters. limit, orderBy, offset, generatorPublicKey, totalAmount, totalFee, reward,
        previousBlock, height
        :return:
        """
        resp = self.request('get', "api/blocks", **kwargs)
        return resp.json()

    def get_height(self):
        """ Get the blockchain height.

        :return:
        """
        resp = self.request('get', "api/blocks/getHeight")
        return resp.json()

    def get_epoch(self):
        """ Get the blockchain epoch.

        :return:
        """
        resp = self.request('get', "api/blocks/getEpoch")
        return resp.json()

    def get_nethash(self):
        """ Get the blockchain nethash.

        :return:
        """
        resp = self.request('get', "api/blocks/getNethash")
        return resp.json()

    def get_fee(self):
        """ Get the transaction fee for sending "normal" transactions.

        :return:
        """
        resp = self.request('get', "api/blocks/getFee")
        return resp.json()

    def get_fees(self):
        """ Get the network fees.

        :return:
        """
        resp = self.request('get', "api/blocks/getFees")
        return resp.json()

    def get_milestone(self):
        """ Get the blockchain milestone.

        :return:
        """
        resp = self.request('get', "api/blocks/getMilestone")
        return resp.json()

    def get_reward(self):
        """ Get the blockchain reward.

        :return:
        """
        resp = self.request('get', "api/blocks/getReward")
        return resp.json()

    def get_supply(self):
        """ Get the blockchain supply.

        :return:
        """
        resp = self.request('get', "api/blocks/getSupply")
        return resp.json()

    def get_status(self):
        """ Get the blockchain status.

        :return:
        """
        resp = self.request('get', "api/blocks/getStatus")
        return resp.json()
