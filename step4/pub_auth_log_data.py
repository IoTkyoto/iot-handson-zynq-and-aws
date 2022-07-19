# -*- coding: utf-8 -*-
"""
センサー値をクラウドにアップロードするコード
引数1: センサー値のリアルタイムデータ(JSON)
"""
import sys
import json
import boto3
from boto3.session import Session

# ----- 定数 -----
# このファイルを実行時に受け取る引数(JSON)
ARGS = sys.argv

# AWS プロファイル情報
PROFILE_NAME = 'zynq-handson'
session = Session(profile_name=PROFILE_NAME, region_name="ap-northeast-1")
IOT_DATA = session.client('iot-data')

class PubAuthLogData():
    def __init__(self):
        self.arg_auth_log_data = ARGS[1]

    def publish_auth_log_data(self):
        response = IOT_DATA.publish(
                topic='handson/authLogData',
                qos = 1,
                payload = self.arg_auth_log_data
        )
        print(response)
    
    def main(self):
        try:
            self.publish_auth_log_data()
        except Exception as error:
            print(error)

#　初期化
pub_auth_log_data = PubAuthLogData()

if __name__ == "__main__":
    pub_auth_log_data.main()
