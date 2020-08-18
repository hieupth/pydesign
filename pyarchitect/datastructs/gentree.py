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
from numbers import Number
from types import LambdaType
from pyarchitect.generic import Object


class Node(Object):
    """
    This class is an implementation of node in general tree data structure.
    ---------
    @author:    Hieu Pham.
    @created:   17th August, 2020.
    """

    @property
    def name(self):
        """Get node name."""
        return self.__nick__

    @name.setter
    def name(self, name):
        """
        Set node name.
        :param name: node name.
        """
        # First validate name.
        name = name if name else 'none'
        self.examine(isinstance(name, (str, bool, Number)), 'node name must be a string, boolean or number.')
        # Assign node name.
        self.__nick__ = name

    @property
    def parent(self):
        """Get parent node."""
        return self.__parent__

    @parent.setter
    def parent(self, parent):
        """
        Set parent node.
        :param parent: parent node.
        """
        # First validate parent node.
        self.examine(isinstance(parent, Node) or parent is None, 'parent node must be an instance of %s.' % Node)
        # Attach to parent.
        if self.parent != parent:
            # Detach old parent first.
            if self.parent is not None:
                self.parent.detach(self.name)
            # Then attach to new parent node.
            if parent is not None:
                parent.attach(self)

    @property
    def leaves(self):
        """Get all leaf nodes."""
        return list(self.__leaves__.values())

    @property
    def is_root(self):
        """Check this node is root or not?"""
        return self.parent is None

    @property
    def root(self):
        """Get root node of current tree."""
        node = self
        while not node.is_root:
            node = node.parent
        return node

    @property
    def is_top(self):
        """Check this node is top lead or not?"""
        return len(self.leaves) == 0

    @property
    def tops(self):
        """Get top leaves of current tree."""
        return self.search(lambda node: node.is_top)

    def __init__(self, name=None, parent=None):
        """
        Class constructor.
        :param name:    node name.
        :param parent:  parent node.
        """
        # Node name.
        self.__nick__ = 'none'
        # Parent node of this node.
        self.__parent__ = None
        # Leaf nodes of this node.
        self.__leaves__ = dict()
        # Now, we validate and assign node name.
        self.name = name
        # Then, we validate and assign parent node.
        self.parent = parent

    def attach(self, node=None):
        """
        Attach a leaf node.
        :param node: node to be attached.
        """
        # Validate leaf node.
        if node:
            self.examine(isinstance(node, Node), 'attached node must be a %s.' % Node)
            self.examine(node.parent == self or node.parent is None, 'cannot attach node of another tree.')
        # Assign leaf node.
        node.__parent__ = self
        self.__leaves__[node.name] = node
        # Return results.
        return self, node

    def detach(self, name=None):
        """
        Detach a leaf node.
        :param name: node name to be detached.
        """
        # Validate node name.
        name = name if name else 'none'
        self.examine(isinstance(name, (str, Number, bool)), 'name must be a string, number or bool.')
        # Detach leaf node.
        node = self.__leaves__.pop(name, None)
        # Reassign variables.
        if node is not None:
            node.__parent__ = None
        # Return results
        return self, node

    def search(self, cond=None):
        """
        Exhausted search for nodes that meet the condition.
        :param cond: condition expression.
        """
        self.examine(isinstance(cond, LambdaType) or callable(cond), 'condition must be callable with 1 param.')
        # Assign variables.
        founds, lookup = [], [self]
        # We use dynamic programming algorithm with two list: founds and lookup
        # to avoid recursive which could cause stack-overflow when the tree is large.
        while len(lookup) > 0:
            node = lookup.pop(0)
            if cond(node):
                founds.append(node)
            else:
                lookup.extend(node.leaves)
        # Return founded results.
        return founds
