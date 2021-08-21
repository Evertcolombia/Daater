#!/usr/bin/python3

import pandas as pd
import numpy as np

class ReadFile():
    """" Read two DataFrame and compare itself
        
        attrs:
        @_colname: name of the column to compare
        @_df: dataFrame for online file
        @_df2: dataFrame for detail file
        @_colId: id of the column to compare in online
        @_colId2:  id of the column to compare in detail
        @_missings: array with diffrent values on column to compare
    """

    def __init__(self, n_col):
        self._colName = n_col
        self._df = None
        self._df2 = None
        self._colId = 0
        self._colId2 = 0
        self._missings = []

    def get_column_index(self, columns, columns2):
        """ get the index of the column  to compare in
            both dataFrames
        """
        self._colId = list(columns).index(self._colName)
        self._colId2 = list(columns2).index(self._colName)


    def open_dataFrames(self, path, path2):
        """ create data frames for online and detail file

            self_df - will contains the online dataFrame
            self_df2 - will contains the detail dataFrame
        """
        self._df = pd.read_csv(path, sep="~", header=0, engine='python')
        self._df["exportador"] =  self._df["exportador"].astype(str)
        self._df["direccion_importador"] =  self._df["direccion_importador"].astype(str)
        self._df2 = pd.read_csv(path2, sep="~", header=0, engine='python')

    def compare_dataFrames(self):
        """ Compare two dataframes """
        for i in range(0, len(self._df.index)):
            on_value = self._df.iloc[i][self._colId]
            self._df.at[i, "detalle"] = 0 #  detalle column rows to 0

            if str(on_value) == "nan":
                continue

            try:
                found = np.where(self._df2[self._colName] == np.int64(on_value))
            except:
                self._missings.append(on_value)

            if len(found[0]) > 0:
                self.update_dataFrame(i, found[0][0])
                st = "Updt row {} {} - values: {} - {} - {} - {}"
                print(st.format(i,
                        on_value,
                        self._df2.iloc[found[0][0]][22],
                        self._df2.iloc[found[0][0]][6],
                        self._df2.iloc[found[0][0]][24],
                        self._df2.iloc[found[0][0]][92]
                    )
                )
                
    def update_dataFrame(self, on_id, dt_id):
        """ update row from online file 
            args:
            @on_id: id for row in online file
            @dt_id: id for row in detail file
        """
        self._df.at[on_id, "nit_importador"] = self._df2.iloc[dt_id][22]
        self._df.at[on_id, "razon_social_importador"] = self._df2.iloc[dt_id][6]
        self._df.at[on_id, "exportador"] = self._df2.iloc[dt_id][24]
        self._df.at[on_id, "direccion_importador"] = self._df2.iloc[dt_id][92]

    def export_df_to_csv(self, pathname):
        """ exports a dataframe as csv file """
        self._df.to_csv(pathname, sep='~', na_rep='', index=False)
        print("The file has been saved! congrats")