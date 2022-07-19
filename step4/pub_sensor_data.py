# -*- coding: utf-8 -*-
"""
センサー値をクラウドにアップロードするコード
引数1: センサー値のリアルタイムデータ(JSON)
"""
import sys
import json
import boto3
import datetime
from boto3.session import Session

# ----- 定数 -----
# このファイルを実行時に受け取る引数(str型)
ARGS = sys.argv

# AWS プロファイル情報
PROFILE_NAME = 'zynq-handson'
session = Session(profile_name=PROFILE_NAME, region_name="ap-northeast-1")
IOT_DATA = session.client('iot-data')

class PubSensorData():
    def __init__(self):
        self.arg_accel_x_data = ARGS[1]
        self.arg_accel_y_data = ARGS[2]
        self.arg_accel_z_data = ARGS[3]
        self.arg_gyro_x_data = ARGS[4]
        self.arg_gyro_y_data = ARGS[5]
        self.arg_gyro_z_data = ARGS[6]
        self.arg_mag_x_data = ARGS[7]
        self.arg_mag_y_data = ARGS[8]
        self.arg_mag_z_data = ARGS[9]

    def get_now_datetime(self):
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        timestamp = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        return timestamp

    def create_json_data(self, timestamp):
        sensor_data_json = {
                                "DeviceID": "id001",
                                "Datetime": timestamp,
                                "AccelX": float(self.arg_accel_x_data),
                                "AccelY": float(self.arg_accel_y_data),
                                "AccelZ": float(self.arg_accel_z_data),
                                "GyroX" : float(self.arg_gyro_x_data),
                                "GyroY" : float(self.arg_gyro_y_data),
                                "GyroZ" : float(self.arg_gyro_z_data),
                                "MagX" : float(self.arg_mag_x_data),
                                "MagY" : float(self.arg_mag_y_data),
                                "MagZ" : float(self.arg_mag_z_data)
                            }
        return json.dumps(sensor_data_json)

    def publish_sensor_data(self, sensor_data):
        response = IOT_DATA.publish(
                topic='handson/sensorLogData',
                qos = 1,
                payload = sensor_data
        )
        print(response)
    
    def main(self):
        try:
            timestamp = self.get_now_datetime()
            sensor_data = self.create_json_data(timestamp)
            self.publish_sensor_data(sensor_data)
        except Exception as error:
            print(error)

#　初期化
pub_sensor_data = PubSensorData()

if __name__ == "__main__":
    pub_sensor_data.main()
