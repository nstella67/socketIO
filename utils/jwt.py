from flask import  Blueprint, request, jsonify
from utils.common_util import respond
import boto3
from botocore.exceptions import ClientError
import utils.config as def_config
import datetime
import jwt


def put_jwt(member_id, access_token, refresh_token, table_name, region_name, aws_access_key_id, aws_secret_access_key):
    dynamodb = boto3.resource('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(
            Item={
                'memberId': str(member_id),
                'accessToken': access_token,
                'refreshToken': refresh_token
            }
        )
    except ClientError as e:
        return {"result":"fail", "result_code":[2000, 210], "result_msg":str(e), "data":""}

    return {"result":"success", "result_code":[1000, 200], "result_msg":"", "data":""}


def get_jwt(member_id, table_name, region_name, aws_access_key_id, aws_secret_access_key):
    dynamodb = boto3.resource('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key={'memberId': str(member_id)})
    except ClientError as e:
        return {"result":"fail", "result_code":[2000, 210], "result_msg":str(e), "data":""}

    if not 'Item' in response:
        return {"result":"fail", "result_code":[3060, 200], "result_msg":"로그인 정보를 확인할 수 없습니다. 다시 로그인해주세요.", "data":""}
    return {"result":"success", "result_code":[1000, 200], "result_msg":"", "data":response['Item']}



def update_jwt(member_id, access_token, table_name, region_name, aws_access_key_id, aws_secret_access_key):
    dynamodb = boto3.resource('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    table = dynamodb.Table(table_name)
    try:
        response = table.update_item(
            Key={
                'memberId': str(member_id)
            },

            UpdateExpression="set accessToken=:accessToken",
            ExpressionAttributeValues={
                ':accessToken': access_token
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        return {"result":"fail", "result_code":[2000, 210], "result_msg":str(e), "data":""}

    return {"result":"success", "result_code":[1000, 200], "result_msg":"", "data":""}


# jwt를 복호화한 후 payload에서 유효기간이 지났을 경우 해당 jwt를 제거
def delete_jwt(member_id, access_token, table_name, region_name, aws_access_key_id, aws_secret_access_key):
    dynamodb = boto3.resource('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    table = dynamodb.Table(table_name)

    try:
        response = table.delete_item(
            Key={
                'memberId': str(member_id)
            },
            ConditionExpression="accessToken=:accessToken",
            ExpressionAttributeValues={
                ":accessToken": access_token
            }
        )
    except ClientError as e:
        if str(e) == 'An error occurred (ConditionalCheckFailedException) when calling the DeleteItem operation: The conditional request failed':
            return {"result": "fail", "result_code": [3110, 900], "result_msg": "이미 로그아웃 되었습니다.", "data": ""}

        return {"result":"fail", "result_code":[2000, 210], "result_msg":str(e), "data":""}

    return {"result":"success", "result_code":[1000, 200], "result_msg":"", "data":""}


def get_jwt_access_token(member_id, cust_name, cust_id, cust_id_gbn, user_id):

    key = def_config.JWT_SECRET_KEY

    # pyjwt에서 제공하는 decode의 timezone이 utc라서 encoding할 만료시간도 utc를 기준으로 세팅하였음.
    payload = {
        "member_id":str(member_id),
        "cust_name":cust_name,
        "cust_id":cust_id,
        "cust_id_gbn":cust_id_gbn,
        "user_id": user_id,
        # "member_level":"admin",  # 관리자, 일반회원, 기업회원 등등
        # 'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=2)  #유효기간 : 현재시간으로부터 2시간
        'exp':datetime.datetime.utcnow() + datetime.timedelta(days=1)  # 테스트를 위해 매우 짧은 시간으로 세팅함.
        # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)  # 테스트를 위해 매우 짧은 시간으로 세팅함.
    }

    token = jwt.encode(payload, key, algorithm='HS256')

    return token


def get_jwt_refresh_token(member_id, cust_name, cust_id, cust_id_gbn, user_id):
    key = def_config.JWT_SECRET_KEY

    # pyjwt에서 제공하는 decode의 timezone이 utc라서 encoding할 만료시간도 utc를 기준으로 세팅하였음.
    payload = {
        "member_id":str(member_id),
        "cust_name":cust_name,
        "cust_id": cust_id,
        "cust_id_gbn": cust_id_gbn,
        "user_id": user_id,
        # 'exp':datetime.datetime.utcnow() + datetime.timedelta(days=7)  #유효기간 : 현재시간으로부터 7일
        'exp':datetime.datetime.utcnow() + datetime.timedelta(days=7)  # 테스트를 위해 매우 짧은 시간으로 세팅함.
    }

    token = jwt.encode(payload, key, algorithm='HS256')

    return token