import os.path

import aioredis as aioredis
import peewee_async
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import asyncio

import user
from base import BaseHandler
from db import database

define('port',default=8000,help='default port',type=int)

# 设置tornado静态文件夹的目录
static_path=os.path.join(os.path.dirname(__file_),"static")

class TestHandler(BaseHandler):
    async def get(self):
        self.finish({"msg":"hello Tornado"})

# 集成路由

urlpatterns=[(r'/',TestHandler)]
urlpatterns+=(user.urlpatterns)

app= tornado.Application(
    handlers=urlpatterns,static_path=static_path,debug=True
)

# 将数据库链接注入到事件循环中
app.objects=peewee_async.Manager(database)

# 将异步redis 链接注入事件循环
#async def redis_pool(loop)
# return await aioredis.create_redis_pool("localhost",encoding='utf8',loop=loop)

# loop=asyncio.get_event_loop()

# app.redis=loop.run_until_complete(redis_pool(loop))

if __name__ == '__main__':
    print("开启服务")
    tornado.options.parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()