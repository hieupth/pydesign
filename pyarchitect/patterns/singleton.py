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
from threading import Lock
from typing import Optional


class Singleton(type):
    """
    Restricts the instantiation of a class to one instance. Supported thread-safe.
    ---------
    @author:    Hieu Pham.
    @created:   24th June, 2020.
    """
    # Singleton instance.
    _instance: Optional = None
    # Lock for thread-safe mode,
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Where the instance of the class can behave and called like a function.
        :param args:    additional arguments to be passed.
        :param kwargs:  additional keyword arguments to be passed.
        :return:        singleton instance.
        """
        # Now, imagine that the program has just been launched. Since there's no Singleton instance yet, multiple
        # threads can simultaneously pass the previous conditional and reach this point almost at the same time.
        # The first of them will acquire lock and will proceed further, while the rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional, goes inside and creates the Singleton
            # instance. Once it leaves the lock block, a thread that might have been waiting for the lock release may
            # then enter this section. But since the Singleton field is already initialized, the thread won't create a
            # new object.
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        # Finally, return the singleton instance.
        return cls._instance