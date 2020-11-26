
import pandas as pd

# read tokens csv
tokens = pd.read_csv("filtered_token.csv")
print("filtered_token.csv")
print(tokens.shape)

# read data excel
data = pd.read_excel("total_data.xlsx").drop(columns=['A', 'D', 'E', 'F', 'G'])
print("total_data.xlsx")
print(data.shape)

# remove some rows in data
indexes = tokens["index"].to_numpy().tolist()
to_be_removed = []
for i in range(len(data)):
    if i not in indexes:
        to_be_removed += [i]

data = data.drop(index=to_be_removed).reset_index(drop=True)

print("tokens")
print(tokens.shape)
#print(tokens)
print("total_data")
print(data.shape)
#print(data)

# combine to one DataFrame
data = pd.concat([tokens, data], axis=1)
print(data.shape)

#pd.set_option('display.max_columns', None)
#print(data.columns)
#print(data)

# save to file

data.to_csv("cleaned_data.csv", index=False)
