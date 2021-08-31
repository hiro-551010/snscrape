import json
import pprint
import pandas as pd

with open("tweets.csv") as f:
    data = pd.read_json(f)
    data["content"] = data["content"].replace('\n', '', regex=True)
    data.to_csv("tweets2.csv")
    