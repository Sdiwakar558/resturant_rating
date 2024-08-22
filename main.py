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

class Calling_all_function:
    def __init__(self):
        self.Zomato_raw_data = r"C:\Users\diwashar\zomato_data for resturant_model"
        self.pickel_model_path = r"C:\Users\diwashar\restaurant_rating\Pickle_model_to_predict"
        self.Pkl_model_name = "store_model.sav"
        self.model_file_path = os.path.join(self.pickel_model_path, self.Pkl_model_name)
    def main_calling_function(self):
        csv_reader_class_instance = Read_csv(self.Zomato_raw_data)
        dataframe = csv_reader_class_instance.read_csv_file()
        Cleaned_data = Clean_raw_data().clean_data(dataframe)
        Encoaded_data = Data_Encoader().encode_data(Cleaned_data)
        X = Encoaded_data.iloc[:, [2, 3, 5, 6, 7, 8, 9, 11]]
        Y = Encoaded_data['rate']
        self.X_train, self.X_test, self.Y_train, self.y_test = train_test_split(
            X, Y, test_size=.1, random_state=353)

        Best_model = Best_model_finder(self.X_train, self.X_test, self.Y_train, self.y_test).comapre_all_model()
        print(Best_model)
        # Here is the Best model name
        model_detail_name = Best_model[1]
        ##serializing the ML model for further prediction
        with open(self.model_file_path,'wb') as file:
            pickle.dump(model_detail_name,file)
    def predict_data_pickle_model(self):
        #deserializing the ML model
        with open(self.model_file_path,'rb') as files:
            loaded_model = pickle.load(files)
            predicted_data=loaded_model.predict(self.X_test)
            return r2_score(self.y_test,predicted_data)
    # refactoring the folder for pickle model
    def check_pickle_folder(self):
        if os.path.exists(self.pickel_model_path):
            shutil.rmtree(self.pickel_model_path)
            self.check_pickle_folder()
        else:
            os.mkdir(self.pickel_model_path)
if __name__ =="__main__":
    instance_of_main_method_class = Calling_all_function()
    instance_of_main_method_class.check_pickle_folder()
    instance_of_main_method_class.main_calling_function()
    instance_of_main_method_class.predict_data_pickle_model()