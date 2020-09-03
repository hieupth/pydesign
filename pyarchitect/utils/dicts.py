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
from pyarchitect.generic import examine


def update(x, y):
    """
    Update a dictionary by another one.
    :params x:  input dict to be updated.
    :params y:  source dict.
    :return:    updated dict.
    ---------
    @author:    Hieu Pham.
    @created:   24th August, 2020.
    """
    examine(isinstance(x, dict) and isinstance(y, dict), 'inputs should be dict.')
    # Assign dict keys.
    keys = [set(x.keys()), set(y.keys())]
    keys = [keys[0], keys[1], keys[0].union(keys[1]), keys[1].intersection(keys[0])]
    keys.insert(len(keys), keys[2] - keys[3])
    # Update keys which only belongs to one dict.
    z = {k: x.get(k, y.get(k, None)) for k in keys[-1]}
    # Update keys which belongs to both dict.
    for k in keys[3]:
        xk, yk = x.get(k, None), y.get(k, None)
        z.update({k: update(xk, yk) if isinstance(xk, dict) and isinstance(yk, dict) else yk})
    # Return updated dict.
    return z
