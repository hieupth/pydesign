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
