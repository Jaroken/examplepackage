import sys
from examplepackage import random_dataframe

if __name__ == '__main__':
    length = int(sys.argv[1])
    ncols = int(sys.argv[2])


    dz = random_dataframe.random_dataframe(length = length)
    dz.add_random_columns(ncols = ncols)
    print(dz.df)