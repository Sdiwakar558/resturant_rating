from datetime import datetime

class App_Log_writer:
    def __init__(self):
        self.datetime_data = datetime.now()
        self.date = self.datetime_data.date()
        self.time = self.datetime_data.strftime("%H:%M:%T")
    def Log_writer(self,file_obj,message):
        file_obj.write(f"{self.date}, {self.time}, {message}\n")
