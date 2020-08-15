
# ###############################################################################
#  MIT License
#
#  Copyright (c) 2020, Hieu Pham. All right reversed.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ###############################################################################
from pyarchitect.structures.tree import Node


class KwargParse(Node):
    """
    Parse arguments from keyword arguments.
    ---------
    @author:    Hieu Pham.
    @created:   15th August, 2020.
    """

    def __init__(self, name=None, key=None, default=None, ignore=False):
        """
        Class constructor.
        :param name:    argument name.
        :param key:     argument key which replace name when parsed.
        :param default: argument default value.
        :param ignore:  ignore parsing process.
        """
        super(KwargParse, self).__init__(name=name)
        # Assign variables.
        self.key = key
        self.ignore = ignore
        self.default = default

    def attach(self, kwargparse=None):
        """
        Attach a kwargparse.
        :param kwargparse: a kwargparse to be attached. 
        """
        # Validate kwargparse.
        assert isinstance(kwargparse, KwargParse), \
            self.message('only kwargparse can be attached.')
        # Attach kwargparse.
        return super().attach(kwargparse)

    def parse(self, **kwargs):
        """
        Parse arguments from keyword arguments.
        :param kwargs:  keyword arguments to be parsed.
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
