import boto3
import os


# Log will store in data_preprocessing_log
class Est_aws_conn:

    def __init__(self):
        self.AWS_access_key_id = os.getenv('AWS_Access_key_id')
        self.AWS_access_security_code = os.getenv('AWS_Access_security_code')


    def conn_details(self):
        client_conn = boto3.client('s3',aws_access_key_id=self.AWS_access_key_id,
                              WS_access_security_code=self.AWS_access_security_code)
        return client_conn
