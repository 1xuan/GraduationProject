__author__ = 'yixuan'
__date__ = '下午12:39'

import requests



"""
新建faceset
"""
# http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
# key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
# secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
# data = {
#     "api_key": key,
#     "api_secret": secret,
#     "display_name": 'yixuan',
#     "outer_id": 'first'
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)


"""
获取faceset
"""
# http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
# key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
# secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
# data = {
#     "api_key": key,
#     "api_secret": secret,
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)

"""
删除faceset
"""
# http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
# key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
# secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
# data = {
#     "api_key": key,
#     "api_secret": secret,
#     "faceset_token": "dee71ab8ee5bb0bade703fda3d764e0f"
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)

"""
添加face_token
"""
# http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
# key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
# secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
# data = {
#     "api_key": key,
#     "api_secret": secret,
#     "faceset_token": "ebf222df9586a44829c5546698cec44b",
#     "face_tokens": '1234567'  # invalid face_token
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)

# """
# get faceset detail
# """
# http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
# key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
# secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
# data = {
#     "api_key": key,
#     "api_secret": secret,
#     "faceset_token": "ebf222df9586a44829c5546698cec44b",
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)


"""
remove face_tokens
"""
# http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
# key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
# secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
# data = {
#     "api_key": key,
#     "api_secret": secret,
#     "faceset_token": "ebf222df9586a44829c5546698cec44b",
#     "face_tokens": "RemoveAllFaceTokens",
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)

import json
import cv2

pin = False

# face++相关参数
http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
data = {
    "api_key": key,
    "api_secret": secret,
    }

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    # cv2.resize(frame,frame,320,240,0)
    # show a frame
    if ret is True:
        cv2.imwrite("photo.png", frame)
        filepath = "/home/yixuan/PycharmProjects/test/photo.png"

        # 上传图片进行人脸检测
        with open(filepath, "rb") as fp:
            files = {"image_file": fp}
            # response = requests.post(http_url, data=data, files=files)
            # print(response.text)
            while True:
                response = requests.post(http_url, data=data, files=files)
                response = json.loads(response.text)
                if not response.get('error_message'):
                    break

        # 如果没有检测到人脸则继续检测
        print(response)
        if len(response['faces']) == 0:
            continue

        # 获取face_token的值
        face_token = response["faces"][0]["face_token"]

        # 调用后台接口,并返回结果判断
        ret = requests.get("http://127.0.0.1:8000/interaction/{0}/".format(face_token)).text
        print(ret)
        if ret == 'True':
            print('open')
            pin = True
            break
        else:
            print('close')
            break

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()


