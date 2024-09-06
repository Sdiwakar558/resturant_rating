import pandas as pd
import os
pd.set_option('future.no_silent_downcasting', True)
class Read_csv:
    def __init__(self,csv_file_path):
        if os.path.exists(csv_file_path):
            Raw_data_path = os.path.join(csv_file_path,os.listdir(csv_file_path)[0])
            self.final_path = Raw_data_path
    def read_csv_file(self):
        Zomato_raw_dataframe = pd.read_csv(self.final_path)
        return  Zomato_raw_dataframe