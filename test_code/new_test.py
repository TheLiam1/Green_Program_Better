import plotly.express as px

df = px.data.iris()
df["error"] = df["sepal_width"] / 50 

"""
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 marginal_x="box", marginal_y="violin",
                 trendline="ols",
                 error_x="error")
"""
df2 = px.data.tips()
print(df2)
exit()
fig2 = px.bar(df, x="species", y="sepal_length") # Daten werden einfach aufsummiert - ist hier nicht besonders sinnvoll

fig2.show()
