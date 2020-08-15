
from pyarchitect.structures.tree import Node


class KwargParser(Node):

    def __init__(self, name=None, key=None, default=None, ignore=False):
        super().__init__(name=name)
        self.key = key
        self.ignore = ignore
        self.default = default

    def attach(self, kwargparser=None):
        assert isinstance(kwargparser, KwargParser), \
            self.message('only kwargparser can be attached.')
        super().attach(kwargparser)

    def parse(self, **kwargs):
        """
        Parse arguments from keyword arguments.
        :param
        """
        args = dict()
        # Assign argument keyword.
        key = self.key if self.key else self.name
        # Parse arguments.
        if not self.ignore:
            args.update({key: kwargs.get(self.name, self.default)})
        elif self.ignore and self.is_top and self.name in kwargs:
            args.update({key: kwargs.get(self.name, self.default)})
        else:
            for _, node in self._leaves.items():
                args.update(node.parse(**kwargs))
        # Return parsed arguments.
        return args
