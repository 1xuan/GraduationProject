import requests
import json
import os

from datetime import datetime
from django.db import models

from GraduationProject.settings import BASE_DIR


class Action(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    identity = models.CharField(max_length=20, verbose_name='身份')
    time = models.DateField(default=datetime.now, verbose_name='时间')

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    identity = models.CharField(max_length=20, verbose_name='身份')
    face_token = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='image', max_length=100, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # 重命名并存储图片
        self.image.name = self.name + self.image.name[-4:]
        super(Person, self).save(*args, **kwargs)

        # 得到face_token的值
        filepath = os.path.join(BASE_DIR, self.image.name)
        http_url_detect = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
        key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
        secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
        data_detect = {
            "api_key": key,
            "api_secret": secret,
        }

        with open(filepath, 'rb') as fp:
            files = {'image_file': fp}
            while True:
                response = requests.post(http_url_detect, data=data_detect, files=files)
                response = json.loads(response.text)
                if not response.get('ERROR_MESSAGE'):
                    break

        # 没有检测到人脸便抛出错误
        self.face_token = response['faces'][0]['face_token']



        # 添加face_token到faceset
        http_url_add = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
        data_add = {
            "api_key": key,
            "api_secret": secret,
            "faceset_token": "ebf222df9586a44829c5546698cec44b",
            "face_tokens": self.face_token
            }
        while True:
            response = requests.post(http_url_add, data=data_add)
            response = json.loads(response.text)
            if not response.get('ERROR_MESSAGE'):
                break

        super(Person, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(BASE_DIR, self.image.name))
        """
        remove face_tokens
        """
        http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
        key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
        secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
        data = {
            "api_key": key,
            "api_secret": secret,
            "faceset_token": "ebf222df9586a44829c5546698cec44b",
            "face_tokens": self.face_token,
            }

        while True:
            response = requests.post(http_url, data=data)
            response = json.loads(response.text)
            if not response.get('ERROR_MESSAGE'):
                break

        super(Person, self).delete(*args, **kwargs)


