import os
import shutil
from App_logger.Logger import App_Log_writer


class Check_Log_file:
    def __init__(self):
        self.Log_root_path = './Log'
        self.sub_path_preprocessing = './Log/Data_Preprocessing_Log'
        self.sub_path_training = './Log/Training_Log'
        self.App_Log_writer = App_Log_writer()
        self.log_file_path = './Folder_logger.txt'

    def folder_exist_or_create(self):
        log_file = open(self.log_file_path, 'r+')
        log_file.close()
        try:
            log_file = open(self.log_file_path, 'a+')
            if os.path.exists(self.Log_root_path):
                shutil.rmtree(self.Log_root_path)
                self.App_Log_writer.Log_writer(log_file,'path exist so deleted existing content')
                self.folder_exist_or_create()
            else:
                folder_list = [self.Log_root_path,self.sub_path_preprocessing,self.sub_path_training]
                for folder in folder_list:
                    os.mkdir(folder)
                self.App_Log_writer.Log_writer(log_file, 'Folder created successfully')
        except OSError:
            log_file = open(self.log_file_path, 'a+')
            self.App_Log_writer.Log_writer(log_file, f'{OSError} occured')
            log_file.close()
        except Exception as e:
            log_file = open(self.log_file_path, 'a+')
            self.App_Log_writer.Log_writer(log_file, f'{e} occured')
            log_file.close()
            raise e

if __name__ =='__main__':
    Check_Log_file().folder_exist_or_create()