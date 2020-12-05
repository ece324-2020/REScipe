
import pandas as pd

from PIL import Image
import requests
from io import BytesIO


data = pd.read_csv("cleaned_data.csv")

unsuccessful = []

#pd.set_option('display.max_columns', None)
print(data.columns)
print(data)
print(data["url"][0])
print(data["code"][0])

for index, row in data.iterrows():
    url = row["url"]
    code = row["code"]
    file_name = str(code)+".jpg"
    if index%100 == 0:
        print(file_name)

    try:
        # get image
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        # adjust image
        img = img.resize((224,224), Image.ANTIALIAS)
        img = img.convert("RGB")

        #img.show()
        img.save(file_name)
    except:
        unsuccessful += [row]
        print(index, "unsuccessful")

print(unsuccessful)
