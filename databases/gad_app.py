"""
File: gad_app.py

Description: gad application
"""

import db_utils
import sankey as sk


class GadApp:
    def __init__(self, user, password, database, phenotype, min=2, host='localhost', go_gene='gene'):
        self.db = db_utils.DBUtils(user, password, database, host)
        self.phenotype = phenotype
        self.min = min
        self.df = None

        if go_gene == 'gene':
            self.disease_gene_subnetwork()
        else:
            self.disease_go_subnetwork()

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
        self.df = df[df.npubs >= self.min]

    def disease_go_subnetwork(self):
        query = f"""
                    select *
                    from disease_go
                    where go_term in (
                        select go_term
                        from disease_go
                        where phenotype = '{self.phenotype}')
                    order by phenotype, go_term;
                """

        # execute query
        df = self.db.execute_query(query)

        # Filter for number of publications
        self.df = df[df.num_genes >= self.min]

    def sankey(self):
        cols = self.df.columns
        sk.show_sankey(self.df, cols[0], cols[1], cols[2])


if __name__ == '__main__':
    gad = GadApp(user='root', password='PASSWORD', database='bio', phenotype='cancer', go_gene='go')
    gad.sankey()
