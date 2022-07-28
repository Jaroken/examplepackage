import sys
import examplepackage

if __name__ == '__main__':
    length = int(sys.argv[1])
    ncols = int(sys.argv[2])


    dz = examplepackage.random_dataframe(length = length)
    dz.add_random_columns(ncols = ncols)
    print(dz.df)