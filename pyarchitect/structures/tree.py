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
from numbers import Number
from pyarchitect.utils.log import Loggable


class Node(Loggable):
    """
    This class is an implementation of a node in tree data structure.
    ---------
    @author:    Hieu Pham.
    @created:   15th August, 2020.
    """

    @property
    def name(self):
        """
        Get node name.
        """
        return self._name

    @property
    def root(self):
        """
        Get node root.
        """
        return self._root

    @property
    def is_root(self):
        """
        Check a node is a tree root or not?
        A node is a root when it contains no root.
        """
        return self._root is None

    @property
    def is_top(self):
        """
        Check a node is a top leaf or not?
        A node is a top leaf when it contains no leaf node.
        """
        return len(self._leaves) == 0

    def __init__(self, name=None, root=None):
        """
        Class constructor.
        :param name:    node name.
        :param root:    root node.
        """
        # Assign and validate node name.
        # Node name can be number, string, boolean or NoneType.
        self._name = 'none' if name is None else name
        assert isinstance(self._name, (Number, str, bool)), \
            self.message('node name must be number, string, boolean or none.')
        # Assign and validate root node.
        assert root is None or isinstance(root, Node), \
            self.message('node root must be a node or none.')
        if isinstance(root, Node):
            root.attach(self)
        self._root = root
        # Assign container to keep leaf nodes.
        self._leaves = dict()

    def attach(self, node=None):
        """
        Attach a leaf node.
        :param node: node to be attached.
        """
        # Assign and validate attached node.
        assert isinstance(node, Node), self.message('attached node must be a node.')
        assert node._root is None or node._root != self, self.message('cannot attach a node which belongs to another.')
        # Attach leaf node.
        node._root = self
        self._leaves[node._name] = node
        # Return self for later use.
        return self

    def detach(self, name=None):
        """
        Detach a leaf node.
        :param node: node name to be detached.
        """
        # Assign and validate node name.
        name = 'none' if name is None else name
        assert isinstance(self._name, (Number, str, bool)), \
            self.message('node name must be number, string, boolean or none.')
        # Detach node.
        node = self._leaves.pop(name, None)
        if isinstance(node, Node):
            node._root = None
        # Return results.
        return self, node

    def visit(self, name=None):
        """
        Visit a node or set of nodes forwardly based on name(s).
        :param name: node name(s).
        """
        # In case of visiting a set of nodes.
        if isinstance(name, (list, tuple)):
            node = self
            for n in name and not node.is_top:
                node = node.visit(n)
            return node
        # In case of visiting single node.
        else:
            # Assign and validate node name.
            name = 'none' if name is None else name
            assert isinstance(self._name, (Number, str, bool)), \
                self.message('node name must be number, string, boolean or none.')
            # Return correct node.
            return self._leaves.get(name, None)
