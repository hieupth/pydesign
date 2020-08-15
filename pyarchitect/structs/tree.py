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
from pyarchitect.common.log import LogObject


class TreeNode(LogObject):
    """
    This class is an implementation of node in tree data structure.
    ---------
    @author:    Hieu Pham.
    @created:   15th August, 2020.
    """
    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._root

    @property
    def is_root(self):
        return self._root is None

    @property
    def is_top(self):
        return len(self._leaves) == 0

    @staticmethod
    def check_name(name=None):
        assert name.isnumeric() or isinstance(name, str), 'Node name should be string or number.'

    def __init__(self, name=None, root=None):
        """
        Class constructor.
        :param name: node name.
        :param root: node root.
        """
        # Check variables.
        self.check_name(name)
        assert isinstance(root, TreeNode) or None
        # Assign variables.
        self._name = name
        self._root = root
        self._leaves = dict()

    def add(self, node):
        """
        Assign a leaf node.
        :param node: node to be assigned.
        """
        # Check variables.
        assert isinstance(node, TreeNode), self.message('can only add a node.')
        assert node.parent is None or node.parent == self, self.message('cannot add a node of another.')
        # Assign leaf node.
        node._root = self
        self._leaves[node.name] = node
        # Return current node.
        return self

    def pop(self, name=None):
        """
        Reassign a node with specific name.
        :param name: node name.
        """
        # Check variables.
        self.check_name(name)
        # Reassign node.
        if name in self._leaves:
            node = self._leaves.pop(name)
            node._root = None
        else:
            node = None
        # Return reassigned node.
        return node

    def visit(self, name=None):
        """
        Visit a leaf node.
        :param name: node name(s)
        """
        # In case of name is listable, we visit nodes level by level.
        if isinstance(name, (list, tuple)):
            node = self
            for n in name and not node.is_top:
                node = node.visit(n)
            return node
        # Otherwise, simply get a node with specific name.
        else:
            self.check_name(name)
            return self._leaves.get(name, None)
