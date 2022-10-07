import mysql.connector
from sankey import show_sankey
import pandas as pd
import os


class Bio():

    def __init__(self, phenotype, min_pubs=2):
        self.db = mysql.connector.connect(
            host='localhost',
            user='USERNAME',  # DON'T HARDCODE USERNAME
            password='PASSWORD',  # DON'T HARDCODE PASSWORD
            database='bio')

        self.phenotype = phenotype
        self.min_pubs = min_pubs
        self.df = None

    def disease_gene_subnetwork(self):
        query = f"""
                  SELECT *
                  FROM gad_pubs
                  WHERE gene_symbol in (
                    SELECT gene_symbol
                    FROM gad_pubs
                    WHERE phenotype='{self.phenotype}')
                  ORDER BY gene_symbol;
                 """

        # create a result set
        rs = self.db.cursor()

        # execute a query
        rs.execute(query)

        # fetch data
        rows = rs.fetchall()
        cols = list(rs.column_names)

        # convert to dataframe and close resource
        df = pd.DataFrame(rows, columns=cols)
        rs.close()

        # filter npubs
        self.df = df[df.npubs >= self.min_pubs]

    def sankey(self):
        if self.df is None:
            self.disease_gene_subnetwork()

        cols = self.df.columns
        show_sankey(self.df, cols[0], cols[1], cols[2])


if __name__ == '__main__':
    bio = Bio('asthma')
    bio.sankey()

