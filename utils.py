import pandas as pd

"""
k4gt
In Python, backslash = special characters. 'hello\nworld' where \n means newline

Window path names commonly have backslashes. r stands for "raw" and will cause blackslashes in 
the string to be interpreted as actual backslashes rather than special characters.

https://stackoverflow.com/questions/42654934/need-of-using-r-before-path-name-while-reading-a-csv-file-with-pandas

ASK: What does I: do?
"""

CLEANED_ILI_TALLY_FILE_NAME = r"I:\2023 ILI Pipe Tally Consolidation\All_ILIData.csv"

def read_cleaned_ILI_tally() -> pd.DataFrame:
    # Read the file 
    # k4gt: recognize '' as na values
    # ASK k4gt: low_memory = False to ensure no mixed type interference?
    data = pd.read_csv(CLEANED_ILI_TALLY_FILE_NAME, low_memory=False, na_values='')
    # Output the number of rows
    print(f"Total rows = {len(data)}")
    print(f"Headers: {list(data)}")
    return data