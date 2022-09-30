"""
File: gad.py

Description: A demo of my developed sankey API using gene-disease association

"""
import sankey as sk
import pandas as pd


def extract_local_network(gad: pd.DataFrame, phenotype: str, min_pub=3):
    # positive associations only
    gad = gad[gad.association == 'Y']

    # extract key columns {phenotype, gene}
    gad = gad[['phenotype', 'gene']]

    # convert all to lowercase
    gad.phenotype = gad.phenotype.str.lower()

    # count pubs for each disease-gene combo
    gad = gad.groupby(['phenotype', 'gene']).size().reset_index(name='npubs')

    gad.sort_values('npubs', ascending=False, inplace=True)
    gad = gad[gad.npubs >= min_pub]

    # phenotype of interest
    gad_pheno = gad[gad.phenotype == phenotype]

    # finding all gad associations involving phenotype linked genes
    # gad = gad[gad.gene.isin(gad_pheno.gene)]
    gad = pd.merge(gad, gad_pheno.gene, on='gene')

    return gad


def main():
    df = 'data/gad.csv'
    gad = pd.read_csv(df)
    # analysis parameters
    phenotype = 'breast cancer'

    local = extract_local_network(gad, phenotype)
    sk.Sankey(local, 'phenotype', 'gene', 'npubs').make_sankey()
    print(local)


if __name__ == '__main__':
    main()
