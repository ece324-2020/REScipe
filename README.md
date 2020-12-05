# REScipe

### Outer Folder Should Be EMPTY Except readme

### Prerequisites

run `pip install pipreqs` if it's the first time installing the package

If you add new installation packages to any file, run `pipreqs --force .`, this will update the requirements.txt file.

run `pip install -r requirements.txt` if you're running files from the repo for the first time after any updates or git pulls. 

bare_minimum.csv: so far only 20 images and titles, used for testing other features so far.

total_data.xlsx: 45 000 rows containing image sources, recipe titles, url extensions, and other information relating to the recipe. (URL Extension is unique, can use as a key)
