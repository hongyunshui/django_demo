from django.db import models
# Create your models here.


class NaturalPerson(models.Model):
    """自然人信息"""
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


class RecordsSource(models.Model):
    """案卷来源码表"""
    source_id = models.IntegerField()
    source_value = models.CharField(max_length=50)

    def __str__(self):
        return self.source_value


class BaseRecordsTB(models.Model):
    """案情表"""
    # 案情表ID
    record_id = models.IntegerField()
    # 案卷ID
    archive_id = models.IntegerField()
    # 案发时间
    record_time = models.DateTimeField()
    # 案发地址
    # 案件类型
    # 执法程序
    # 所属区域
    # 主办人
    # 协办人
    # 案情描述
    # 案由
    # 违责依据
    # 违责
    # 罚则依据
    # 罚则
    # 当事人类型
    # 当事人编号

    def __str__(self):
        return self.archive_id
