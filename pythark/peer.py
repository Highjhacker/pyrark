from .api import API


class Peer(API):
    """
    Operations for Peers.
    """

    def get_peer(self, ip, port):
        """ Get a single peer.

        :param ip: Valid IP of the peer.
        :param port: Valid port of the peer.
        :return:
        """
        resp = self.request('get', "api/peers/get", ip=ip, port=port)
        return resp.json()

    def get_peers(self):
        """ Get all peers.

        :return:
        """
        resp = self.request('get', "api/peers")
        return resp.json()

    def get_peer_version(self):
        """ Get the peer version.

        :return:
        """
        resp = self.request('get', "api/peers/version")
        return resp.json()
