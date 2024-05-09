# ----------------------------------------------------------------------------
# Copyright (c) 2023-2024, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Plugin, Metadata, Str, Choices, Bool
from q2_stats._type import (GroupDist, Matched, Ordered)

from q2_vizard._heatmap import plot_heatmap
from q2_vizard._scatterplot import scatterplot


plugin = Plugin(name='vizard',
                version='0.0.1.dev0',
                website='https://github.com/qiime2/q2-vizard',
                description='This QIIME 2 plugin is the first choice of wizard'
                            ' lizards for protection and entertainment.',
                short_description='The first choice of wizard lizards.')


plugin.visualizers.register_function(
    function=plot_heatmap,
    inputs={'data': GroupDist[Ordered, Matched]},
    parameters={
        'transpose': Bool,
        'order': Str % Choices('ascending', 'descending')
    },
    name='Plot Heatmap',
    description='',
)


plugin.visualizers.register_function(
    function=scatterplot,
    inputs={
    },
    parameters={
        'metadata': Metadata,
        'x_measure': Str,
        'y_measure': Str,
        'title': Str
    },
    name='Scatterplot',
    description='Basic scatterplot for visualizing two numeric Metadata'
                ' measures with optional categorical color grouping.',
    parameter_descriptions={
        'metadata': "Any metadata-like input with at least two"
                    " numeric measures for visualizing.",
        'x_measure': "Numeric measure from the input Metadata that should be"
                     " plotted on the x-axis.",
        'y_measure': "Numeric measure from the input Metadata that should be"
                     " plotted on the y-axis.",
        'title': "The title of the scatterplot."}
)
