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