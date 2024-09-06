import os
from Read_csv_data.Read_csv_data import Read_csv
from Cleaning_Raw_data.Raw_data_cleaner import Clean_raw_data
from Training_model.Model_finder import Best_model_finder
from Encode_data.Encode import Data_Encoader
import pickle
import shutil
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from Training_model.Model_finder import Best_model_finder
import matplotlib.pyplot as plt
import seaborn as sns
from Clean_Existing_folder.Clean_Folder import Check_Clean_Folder

class Calling_all_function:
    def __init__(self):
        self.current_working_directory = os.getcwd()
        self.EDA_graph_data_path = os.path.join(self.current_working_directory,'EDA_Graph_plot')
        self.Zomato_raw_data = os.getenv('Zomato_raw_data')
        self.pickel_model_path =os.path.join(self.current_working_directory,'Pickle_model_to_predict')
        self.Pkl_model_name = os.getenv('Pickel_model_name')
        self.model_file_path = os.path.join(self.pickel_model_path, self.Pkl_model_name)

    def main_calling_function(self):
        try:
            csv_reader_class_instance = Read_csv(self.Zomato_raw_data)
            dataframe = csv_reader_class_instance.read_csv_file()
            self.Cleaned_data = Clean_raw_data().clean_data(dataframe)
            self.Encoaded_data = Data_Encoader().encode_data(self.Cleaned_data)
            X = self.Encoaded_data.iloc[:, [2, 3, 5, 6, 7, 8, 9, 11]]
            Y = self.Encoaded_data['rate']
            self.X_train, self.X_test, self.Y_train, self.y_test = train_test_split(
                X, Y, test_size=.1, random_state=353)

            Best_model = Best_model_finder(self.X_train, self.X_test, self.Y_train, self.y_test).comapre_all_model()
            print(Best_model)
            # Here is the Best model name
            model_detail_name = Best_model[1]
            ##serializing the ML model for further prediction
            with open(self.model_file_path,'wb') as file:
                pickle.dump(model_detail_name,file)
        except Exception as e:
            raise e
    def EDA_graph_plot(self):
        try:
            plt.figure(figsize=(10,10))
            corr = self.Encoaded_data.corr()
            sns.heatmap(corr,annot=True,center=0)
            heatmap_img = 'correlation_heatmap.png'
            plt.savefig(os.path.join(self.EDA_graph_data_path,heatmap_img))
        #     above code will give PNG image of 
        except Exception as e:
            raise e

    def predict_data_pickle_model(self):
        #deserializing the ML model
        try:
            with open(self.model_file_path,'rb') as files:
                loaded_model = pickle.load(files)
                predicted_data=loaded_model.predict(self.X_test)
                return r2_score(self.y_test,predicted_data)
        except Exception as e:
            raise e

    # refactoring the folder for pickle model
    def folder_cleanup(self):
        try:
            instance_for_cleaning_folder = Check_Clean_Folder()
            instance_for_cleaning_folder.check_existing_folder(self.current_working_directory,self.EDA_graph_data_path)
        except Exception as e:
            raise e
if __name__ =="__main__":
    instance_of_main_method_class = Calling_all_function()

    instance_of_main_method_class.folder_cleanup()
    # it will clean folder
    instance_of_main_method_class.main_calling_function()
    instance_of_main_method_class.EDA_graph_plot()
    instance_of_main_method_class.predict_data_pickle_model()