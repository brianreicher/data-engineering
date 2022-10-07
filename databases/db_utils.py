"""
File: db_utils.py

Description: database utils
"""

import os
import pandas as pd
import mysql.connector


class DBUtils:

    def __init__(self, user, password, database, host='localhost'):
        self.con = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)

    def close(self):
        self.con.close()
        self.con = None

    def execute_query(self, query):
        rs = self.con.cursor()

        # execute a query
        rs.execute(query)

        # fetch data
        rows = rs.fetchall()
        cols = list(rs.column_names)

        # convert to dataframe and close resource
        rs.close()
        return pd.DataFrame(rows, columns=cols)

