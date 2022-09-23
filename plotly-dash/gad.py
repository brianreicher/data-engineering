"""
File: gad.py

Description: A demo of my developed sankey API using gene-disease association

"""
import pandas as pd

import sankey as sk
import pandas


def main():
    df = 'data/gad.csv'
    gad = pd.read_csv(df)
    print(gad)


if __name__ == '__main__':
    main()
