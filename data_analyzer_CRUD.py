import pandas as pd

data = pd.read_csv("operations.csv")

print(data["operation"].value_counts())

print(data.groupby("operation")["duration_ms"].mean().round(2))

print(data.groupby("table_name")["operation"].count())

print(data.groupby("user_id")["operation"].count().sort_values(ascending=False))