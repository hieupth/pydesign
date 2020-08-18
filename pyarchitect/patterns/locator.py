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


class Locator:
    """
    Encapsulating the processes involved in obtaining a service with a strong abstraction layer.
    Supported multi-thread safe.
    ---------
    @author:    Hieu Pham.
    @created:   24th June, 2020.
    """

    def __init__(self):
        """
        Class constructor.
        """
        # Storing all services.
        self._container = dict()
        # Lock for thread-safe.
        self._lock = Lock()

    def get(self, name: str) -> object:
        """
        Get service by name.
        :param name:    name of service.
        :return:        service object.
        """
        return self._container.get(name)

    def set(self, name, service, overwrite=False):
        """
        Set service with specific name.
        :param name:        name of service.
        :param service:     service object.
        :param overwrite:   overwrite existed or not.
        """
        with self._lock:
            if (name in self._container and overwrite) or name not in self._container:
                self._container[name] = service
