import pandas as pd
from time import perf_counter

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# name, extention = os.path.splitext(r"E:\23-12-2021\Stock More than 1 m.txt")

txtFile = input("Please Enter Full Text File Path : ")
numOfRows = int(input("Please Enter Number OF Rows You Wnat In Every File : "))
path = input("Please Enter Path you wish to save the files : ")

t1_start = perf_counter()

data = pd.read_csv(rf"{txtFile}", sep="\t", chunksize=numOfRows)

counter = 0
for df in data:
    print(df)
    counter += 1
    df.to_excel(rf"{path}\df-{counter}.xlsx", index=False)

t1_stop = perf_counter()

print("End at",  t1_stop - t1_start, " seconds")
