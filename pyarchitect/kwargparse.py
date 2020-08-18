# --------------------------------------------------------------------------------
#  MIT License
#
#  Copyright (c) 2020, Hieu Pham. All rights reserved.
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
# --------------------------------------------------------------------------------
from pyarchitect.datastructs.gentree import Node


class KwargParse(Node):
    """
    Parse arguments from keyword arguments.
    ---------
    @author:    Hieu Pham.
    @created:   16th August, 2020.
    @modified:  18th August, 2020.
    """

    def __init__(self, name=None, key=None, default=None, ignore=False):
        """
        Class constructor.
        :param name:    name of parse.
        :param key:     name replacement when parsed.
        :param default: default value when parsed.
        :param ignore:  ignore parse or not?
        """
        self.key = key
        self.ignore = ignore
        self.default = default
        super(KwargParse, self).__init__(name)

    def attach(self, name=None, key=None, default=None, ignore=False):
        """
        Attach a kwarg parse.
        :param name:    name of parse.
        :param key:     name replacement when parsed.
        :param default: default value when parsed.
        :param ignore:  ignore parse or not?
        """
        return super(KwargParse, self).attach(node=KwargParse(name, key, default, ignore))

    def parse(self, **kwargs):
        """
        Parse arguments from keyword arguments.
        :param kwargs:  keyword arguments to be parsed.
        """
        args = dict()
        # Assign keyword.
        key = self.key if self.key else self.name
        # Parse arguments.
        if len(self.leaves) > 0:
            kwargs = kwargs.get(self.name)
            kwargs = kwargs if isinstance(kwargs, dict) else dict()
            for leaf in self.leaves:
                args.update(leaf.parse(**kwargs))
            args = dict({key: args})
        else:
            args.update({key: kwargs.get(self.name, self.default)})
        # Return parsed arguments.
        return args

    def to_dict(self):
        """
        Convert this parse to dictionary.
        """
        _dict = dict(name=self.name, ignore=self.ignore)
        if self.key:
            _dict.update(key=self.key)
        if self.default:
            _dict.update(default=self.default)
        for leaf in self.leaves:
            _dict.update({leaf.name: leaf.to_dict()})
        return _dict
