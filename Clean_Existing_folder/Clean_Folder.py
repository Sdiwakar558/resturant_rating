import os
import shutil
class Check_Clean_Folder:

    def check_existing_folder(self,current_working_directory,existing_folder_path):
        try:
            if os.path.exists(existing_folder_path):
                shutil.rmtree(existing_folder_path)
                self.check_existing_folder(existing_folder_path)
                print(os.getcwd())
            else:
                os.mkdir(existing_folder_path)
        except Exception as e:
            raise e