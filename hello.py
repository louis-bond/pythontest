#libraries and stuff that probably won't import properly
import pandas as pd
from glob import glob 
import os


#os.chdir("C:/Users/louis/Desktop/Meng_project/Nov_5th_CSV")
file_extension = ".csv"
file_list = [ i for i in glob(f"*{file_extension}")]
print(file_list)
