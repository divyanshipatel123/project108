import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
avgRating = df["Avg Rating"].tolist()
fig = ff.create_distplot([avgRating], ["Average rating of mobile brands"])
fig.show()