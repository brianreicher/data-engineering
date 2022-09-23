import sankey as sk


def main():
    # df = pd.read_csv('bio.csv')
    df = 'data/bio.csv'
    sk.Sankey(df, 'disease', 'gene', 'pubs').make_sankey()


if __name__ == '__main__':
    main()


'''
Notes:

zip(a, b) pairs two lists
list(df.source) produces a list of df column values
dict(list of tuples) = new dict
'''