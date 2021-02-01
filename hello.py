#libraries and stuff that probably won't import properly
import pandas as pd
from glob import glob 

file_extension = ".csv"
file_list = [ i for i in glob(f"*{file_extension}")]
print(file_list)

