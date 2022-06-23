import datetime

import peewee
import peewee_async

# 创建数据库连接对象
database = peewee_async.PooledMySQLDatabase("scoial", host="localhost", port=3306, user="root", password="root")


# 基类

class BaseModel(peewee.Model):
    id = peewee.IntegerField(primary_key=True, unique=True, constraints=[peewee.SQL('AUTO_INCREMENT')])

    # 入库时间
    create_time = peewee.DateField(default=datetime.datetime.now(), help_text="入库时间")

    # 重写父类方法
    def save(self, *args, **kwargs):
        # 判断什么时候赋值入库方法
        if self._pk is None:
            # 赋值
            self.create_time = datetime.datetime.now()

        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        # 传递数据库连接
        database = database


# 用户表
class UserModel(BaseModel):
    email = peewee.CharField(null=False, unique=True, max_length=100)

    password = peewee.CharField(null=False, max_length=100)

    state = peewee.IntegerField(null=False, default=0)

    class Mata:
        # 声明表名
        db_table = 'user'


if __name__ == '__main__':
    # 创建表
    # UserModel.create_table(True)
    # UserModel.drop_table(True)
    # 添加测试数据
    user = UserModel.create(email="test123@test.com", password='123')

    print(user.id)
