# 基础类
# 配置跨域

import json

# 声明基类
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def ___init__(self, *args, **kwargs):
        RequestHandler.__init__(self, *args, **kwargs)

    # 重写分类方法
    def set_default_headers(self):
        # 设置请求头信息
        print("开始设置")

        # 域名信息
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Origin", "x-requested-with")
        self.set_header("Access-Control-Allow-Origin", "POST,GET,PUT,DELETE,TRACE,HEAD,PATCH,OPTIONS")

    def finish(self, chunk=None):
        if chunk is not None and not isinstance(chunk, bytes):
            chunk = json.dumps(chunk, indent=4, sort_keys=True, default=str, ensure_ascii=False)

        try:
            RequestHandler.write(self, chunk)
        except Exception as e:
            pass
        RequestHandler.finish(self)

    def post(self):
        self.write("这里是post请求")

    def trace(self):
        self.write("这里是trace请求")

    def get(self):
        self.write("这里是get请求")

    def put(self):
        self.write("这里是put请求")

    def head(self):
        self.write("这里是head请求")

    def delete(self):
        self.write("这里是delete请求")

    def patch(self):
        self.write("这里是patch请求")

    def options(self, *args):

        # 设置状态吗
        self.set_status(204)
        self.finish()
