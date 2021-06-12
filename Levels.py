import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
as_index = False
print(df.groupby("level")["attempt"].mean())
fig = px.scatter(df, x = df.groupby("level")["attempt"].mean(),y = ["Level 1", "Level 2", "Level 3", "Level 4"])
fig.show()