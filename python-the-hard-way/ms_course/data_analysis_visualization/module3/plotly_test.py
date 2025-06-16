import plotly.express as px
scatter_plot_example = px.scatter(augmented_data, x="Taxes", y = "Total_Cost")
scatter_plot_example.show()