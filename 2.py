print('hello')

import zipfile
with zipfile.ZipFile("hack/data/Sample_Data.zip","r") as zip_ref:
    zip_ref.extractall("hack/data")