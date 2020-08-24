# ------------------------------------------------------------------------------
#  GNU General Public License
#
#  Copyright (c) 2020, Hieu Pham.
#
#  This file is part of Py-Architect.
#  <https://github.com/hieupth/pyarchitect>
#
#  Py-Architect is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Py-Architect is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Py-Architect. If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------
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
        if self.ignore:
            args.update({key: self.parse_leaves(**kwargs)})
        else:
            key = self.key if self.key else self.name
            if not self.is_top:
                args.update({key: self.parse_leaves(**kwargs.get(self.name, {}))})
            else:
                args.update({key: kwargs.get(self.name, self.default)})
        # Return parsed arguments.
        return args

    def parse_leaves(self, **kwargs):
        """
        Parse arguments of leaf nodes from keyword arguments.
        :param kwargs:  keyword arguments to be parsed.
        """
        args = dict()
        # Parse arguments.
        for item in self.leaves:
            args.update(item.parse(**kwargs))
        # Return arguments.
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
