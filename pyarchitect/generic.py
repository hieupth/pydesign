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
import logging as log


def examine(expression=True, message=None):
    """
    Raise an assert error with a message if expression is false.
    ---------
    @author:    Hieu Pham.
    @created:   16th August, 2020.
    """
    try:
        message = message if message else 'something wrong.'
        assert expression, message
    except AssertionError:
        log.error(message, exc_info=True)
        exit(1)


class Object:
    """
    Enabling some utilities for inherited classes.
    ---------
    @author:    Hieu Pham.
    @created:   16th August, 2020.
    """

    def message(self, message=None):
        """
        Generate message string within class name.
        :param message: message string.
        """
        message = message if message else 'silent is gold.'
        return '%s %s' % (self, message)

    def examine(self, expression=True, message=None):
        """
        Raise an assert error with a message if expression is false.
        :param expression:  boolean expression.
        :param message:     message string.
        """
        examine(expression, self.message(message if message else 'something wrong.'))