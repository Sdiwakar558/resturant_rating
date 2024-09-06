import os
import shutil
class Check_Clean_Folder:
    def check_existing_folder(self,current_working_directory,existing_folder_path):
        final_path = os.path.join(current_working_directory,existing_folder_path)
        try:
            if os.path.exists(final_path):
                shutil.rmtree(final_path)
                self.check_existing_folder(current_working_directory,final_path)
            else:
                os.mkdir(final_path)
        except Exception as e:
            raise e