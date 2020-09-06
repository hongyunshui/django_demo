from django.db import models
# Create your models here.


class NaturalPerson(models.Model):
    """人员信息"""
    # 姓名
    name = models.CharField(max_length=50)
    # 性别
    sex = models.IntegerField(choices=((1, '男'), (2, '女')))
    # 民族
    nation = models.CharField(max_length=20)
    # 身份证号码
    id = models.CharField(max_length=18, primary_key=True)
    # 住址
    addr = models.CharField(max_length=200)
    # 签发机关
    sio = models.CharField(max_length=100, db_column='signing_and_issuing_organization')
    # 添加日期
    date_added = models.DateTimeField(auto_now_add=True)
    # # 常用返回值
    # return_inf = (name, sex, id, addr)

    def __str__(self):
        """返回人员信息"""
        return self.name
