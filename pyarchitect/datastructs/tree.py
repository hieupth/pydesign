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
from numbers import Number
from pyarchitect.generic import Object


class Node(Object):

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._parent

    @property
    def is_root(self):
        return self._parent is None

    @property
    def is_top(self):
        return len(self._leaves) == 0

    @property
    def root(self):
        return self._root

    def __init__(self, name=None, parent=None):
        """
        Class constructor.
        :param name:    node name.
        :param parent:  parent node.
        """
        self._root = None
        self._tops = None
        self._parent = None
        # Assign leaf nodes container.
        self._leaves = dict()
        # Validate and assign node name.
        self._name = name if name else 'none'
        self.examine(isinstance(self._name, (str, Number, bool)), 'name must be a string, number or bool.')
        # Validate and assign parent node.
        if parent is not None:
            self.examine(isinstance(parent, Node), 'parent node must be a %s.' % Node)
            parent.attach(self)

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
        node._parent = self
        node._root = self if self.is_root else self._root
        self._leaves[node.name] = node
        # Return current node.
        return self

    def detach(self, name=None):
        """
        Detach a leaf node.
        :param name: node name to be detached.
        """
        # Validate node name.
        name = name if name else 'none'
        self.examine(isinstance(name, (str, Number, bool)), 'name must be a string, number or bool.')
        # Detach leaf node.
        node = self._leaves.pop(name, None)
        if node is not None:
            node._parent = None
        # Return results.
        return self, node
