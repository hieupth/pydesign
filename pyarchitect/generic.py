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