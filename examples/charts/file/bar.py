from bokeh.charts import Bar, output_file, show, vplot, hplot, defaults
from bokeh.sampledata.autompg import autompg as df

defaults.width = 450
defaults.height = 350

bar_plot = Bar(df, label='cyl', title="label='cyl'")

bar_plot2 = Bar(df, label='cyl', bar_width=0.4, title="label='cyl' bar_width=0.4")

bar_plot3 = Bar(df, label='cyl', values='mpg', agg='mean',
                title="label='cyl' values='mpg' agg='mean'")

bar_plot4 = Bar(df, label='cyl', title="label='cyl' color='DimGray'", color='dimgray')

# multiple columns
bar_plot5 = Bar(df, label=['cyl', 'origin'], values='mpg', agg='mean',
                title="label=['cyl', 'origin'] values='mpg' agg='mean'")

bar_plot6 = Bar(df, label='origin', values='mpg', agg='mean', stack='cyl', color='cyl',
                title="label='origin' values='mpg' agg='mean' stack='cyl'", legend='top_right')

bar_plot7 = Bar(df, label='origin', values='displ', agg='mean', group='cyl', color='cyl',
                title="label='origin' values='mpg' agg='mean' stack='cyl'", legend='top_right')

# np_negative_grouped = Bar(
#     random * -1, cat=categories, title="All negative input | Grouped",
#     ylabel="Random Number", width=width, height=height
# )
#
# np_custom = Bar(
#     mixed, cat=categories, title="Custom range (start=-3, end=0.4)",
#     ylabel="Random Number", width=width, height=height,
#     continuous_range=Range1d(start=-3, end=0.4)
# )
#
# np_mixed_grouped = Bar(
#     mixed, cat=categories, title="Mixed-sign input | Grouped",
#     ylabel="Random Number", width=width, height=height
# )

# collect and display
output_file("bar.html")

show(
    vplot(
        hplot(bar_plot, bar_plot2, bar_plot3),
        hplot(bar_plot4, bar_plot5, bar_plot6),
        hplot(bar_plot7)
    )
)
