# ----------------------------------------------------------------------------
# Copyright (c) 2023-2024, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._version import get_versions
from .heatmap import plot_heatmap
from .scatterplot import scatterplot_2d

__version__ = get_versions()['version']
del get_versions

__all__ = ['plot_heatmap', 'scatterplot_2d']
