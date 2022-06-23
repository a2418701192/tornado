import hashlib
import re

from tornado.web import url

from base import BaseHandler
from db import UserModel


def make_password(password):
    # md5
    md5=hashlib.md5()
    # 转码
    sign_utf8=str(password).encode(encoding="utf-8")
    # 加密
    md5.update(sign_utf8)
    # 返回密文
    return md5.hexdigest()

def is_valid_email(email):
    ex_email=re.complie(r'[1-9][0-9]{4,10}@qq\.com$')
    # 匹配match search
    res =ex_email.match(email)
    return res

import redis

# 声明用户接口
class UserHandler(BaseHandler):

    # 声明方法

    async def post(self):
        # 接收参数
        email =self.get_argument('email',None)
        password=self.get_argument('password',None)

        # 异步入库
        try:
            user=await self.application.objects.create(UserModel,email=email,password=make_password(password))
            r=redis.Redis()
            r.set("code","1234")

            self.finish({"msg":"注册成功","errcode":0})
        except Exception as e:
            self.finish({"msg":"请更换email","errcode":1})

# 声明路由
urlpatterns=[

    url('/user/',UserHandler),
]