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
#     "face_tokens": '123456789'
#     }
#
# response = requests.post(http_url, data=data)
# print(response.text)

"""
get faceset detail
"""
http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
data = {
    "api_key": key,
    "api_secret": secret,
    "faceset_token": "ebf222df9586a44829c5546698cec44b",
    }

response = requests.post(http_url, data=data)
print(response.text)


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

