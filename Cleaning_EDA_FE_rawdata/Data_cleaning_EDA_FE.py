import os
import pandas as pd

class Csv_preprocess:
    def __init__(self):
        self.zomato_csv = '../raw_data_from_source'


    def read_csv_data(self):
        file_name = os.listdir(self.zomato_csv)[0]
        raw_csv_path = os.path.join(self.zomato_csv,file_name)
        zomato_raw_dataframe = pd.read_csv(raw_csv_path)
        zomato_raw_dataframe = zomato_raw_dataframe.drop(['url','phone','dish_liked'],axis=1)
        zomato_raw_dataframe.drop_duplicates(inplace=True)
        zomato_raw_dataframe.dropna(how='any',inplace=True)
        zomato_raw_dataframe = zomato_raw_dataframe.rename(columns={'approx_cost(for two people)':'cost',
                                                                    'listed_in(type)':'type','listed_in(city)':'city'})
        print(zomato_raw_dataframe)









if __name__ =='__main__':
    Csv_preprocess().read_csv_data()