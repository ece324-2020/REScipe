# REScipe

### Description

The goal of REScipe is to recommend possible recipes given a food image.

### Prerequisites

run `pip install pipreqs` if it's the first time installing the package

If you add new installation packages to any file, run `pipreqs --force .`, this will update the requirements.txt file.

run `pip install -r requirements.txt` if you're running files from the repo for the first time after any updates or git pulls. 

### Directories

data - contains all kinds of data, from raw data to training results - some data are not included in the GitHub repo due to oversized files

preprocessing - contains all the scripts that deal with early data processing

LDA_model - contains the code for unsupervised LDA topic modelling

NN_model - contains the code for our main model - includes training code and visualization code


