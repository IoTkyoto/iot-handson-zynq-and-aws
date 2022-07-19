"""
Rekognitionを利用して特定の画像に顔を分析するLambdaのためのコード
Method: POST
"""
import json
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

# 定数
REKOGNITION_CLIENT = boto3.client('rekognition')
REQUIRED_KEYS: list = ['bucket_name','file_name','threshold']

# Rekognitionで作成したコレクション名を入れてください
COLLECTION_ID = 'iot-handson-zynq-authentication-collection'
# Rekognitionで一度に検出したい顔の最大数（最大4096人まで可）
MAX_FACES = 10


def search_face(s3_bucket: str, s3_obj: str, threshold: float) -> dict:
    """
    画像とマッチする人物を特定する
    """
    try:
        search_result = REKOGNITION_CLIENT.search_faces_by_image(
            CollectionId=COLLECTION_ID,
            Image={'S3Object': {'Bucket': s3_bucket, 'Name': s3_obj}},
            MaxFaces=MAX_FACES,
            FaceMatchThreshold=threshold,
        )
        return search_result

    # S3アクセス時のエラーに対処
    except Exception as error:
        return make_response(400, '[FAILED]{}'.format(error))


def analyze_faces(s3_bucket: str, s3_obj: str) -> dict:
    """
    画像の中から顔を検出し、その顔の分析結果を返す
    """
    try:
        analyze_result = REKOGNITION_CLIENT.detect_faces(
            Image={'S3Object': {'Bucket': s3_bucket, 'Name': s3_obj}},
            Attributes=["ALL"],
        )
        return analyze_result

    # S3アクセス時のエラーに対処
    except Exception as error:
        return make_response(400, '[FAILED]{}'.format(error))


def check_validation(body: dict):
    """
    バリデーションチェックをする関数
    """
    if not isinstance(body, dict):
        return make_response(400, '[FAILED]Invalid body type')

    errors: list = []
    for key in REQUIRED_KEYS:
        if not key in body.keys():
            errors.append('key "{}" not found'.format(key))
        if body[key] == '':
            errors.append('no value found for "{}"'.format(key))
        if key == 'threshold' and isinstance(body[key], float):
            errors.append('invalid value type: "{}"'.format(body[key]))
        elif not isinstance(body[key], str):
            errors.append('invalid value type: "{}"'.format(body[key]))

        return errors


def make_response(status_code: int, msg: str, payloads: dict = None):
    """
    レスポンスを作成する
    """
    if payloads:
        body = json.dumps({'msg': msg, 'payloads': payloads})
    else:
        body = json.dumps({'msg': msg})

    return {
        'statusCode': status_code,
        'body': body,
    }


def load_json(str_json: str) -> dict:
    """
    JSON文字列をPythonで処理できる形にする
    """
    if str_json is None:
        return make_response(400, '[FAILED]Data required')
    # Lambdaテスト時にdict型で入ってくるためif分岐
    if isinstance(str_json, str):
        # キー名がシングルクォーテーションで囲まれた場合jsonを変換できないためダブルクォーテーションに変換
        str_json = str_json.replace('\'', '"')
        return json.loads(str_json)
    else:
        return str_json


def make_timestamp() -> str:
    """
    タイムスタンプを作成する
    """
    date_now = datetime.now()
    return str(date_now.strftime('%Y-%m-%d %H:%M:%S'))


def lambda_handler(event, _):
    """
    /analyzeに対するPOSTをトリガーに実行
    """
    try:
        body = load_json(event['body'])
        validation_errors = check_validation(body)
        if validation_errors:
            return make_response(400, '[FAILED]' + ', '.join(validation_errors))
        search_result = search_face(
            body['bucket_name'], body['file_name'], body['threshold']
        )
        analyzing_result = analyze_faces(body['bucket_name'], body['file_name'])

        result_dict = {
            "timestamp": make_timestamp(),
            "body_search_result": search_result,
            "body_analyze_result": analyzing_result,
        }
        return make_response(
            200, "[SUCCEEDED]Rekognition and Analysis done", result_dict
        )
    except Exception as error:
        print('[DEBUG]: {}'.format(error))
        return make_response(500, '[FAILED]An error occurred : {}'.format(str(error)))