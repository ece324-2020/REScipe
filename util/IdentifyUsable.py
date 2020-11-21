
import pandas as pd

data = pd.read_csv("cleaned_data.csv")

print(data.columns)
print(data)

to_be_removed = []
for index, row in data.iterrows():
    if ".png" in row["url"]:
        to_be_removed += [index]
        print(row["code"], row["url"])

print(data.shape)

data = data.drop(index=to_be_removed).reset_index(drop=True)

print(len(to_be_removed))
print(data.shape)

data.to_csv("usable_data.csv", index=False)

