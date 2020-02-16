from . import __version__


class Block:
    def __init__(self, index, relayer):
        self.index = index
        self.ver = __version__
        self.relayer = relayer

        self.nonce = None
