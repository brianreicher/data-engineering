"""
File: gad_app.py

Description: gad application
"""

import db_utils
import sankey as sk


class GadApp:
    def __init__(self, user, password, database, phenotype, min_pubs=2, host='localhost' ):
        self.db = db_utils.DBUtils(user, password, database, host)
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

        df = self.db.execute_query(query)
        self.df = df[df.npubs >= self.min_pubs]

    def sankey(self):
        if self.df is None:
            self.disease_gene_subnetwork()

        cols = self.df.columns
        sk.show_sankey(self.df, cols[0], cols[1], cols[2])


if __name__ == '__main__':
    gad = GadApp(user='root', password='PASSWORD', database='bio', phenotype='cancer')
    gad.sankey()
