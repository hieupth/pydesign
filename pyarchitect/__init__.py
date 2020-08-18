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
from __future__ import absolute_import
import logging


# --------------------------------------------------------------------------------
# When this library is imported, it configures logging system formats
# automatically to generate easier readable logs.
# --------------------------------------------------------------------------------
# Assign logging formats.
LOG_FORMAT = '%(levelname)s (%(asctime)s) pid=%(process)d: %(message)s'
LOG_DATE_FORMAT = 'UTC%Z %d.%m.%y %H:%M:%S'
# Setting up logging system.
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)