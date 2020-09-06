# django_demo


## 部署
    1.下载代码
    git clone https://github.com/hongyunshui/django_demo.git django_demo
    2.安装python-3.5.4
    3.安装virtualenv
    pip install virtualenv
    4.创建虚拟环境
    python -m venv venvname
    5.激活虚拟环境
    source venvname/bin/activate
    6. 进入项目下载的目录 django_demo
    cd django_demo
    7. 安装相关依赖
    pip install -r requirements.txt
    8.初始化数据
    python manage.py makemigrations app01/make_document
    python manage.py migrate
    9.创建超级用户
    python manage.py createsuperuser
    8.启动项目
    python manage.py runserver ip:port

## 说明
    此项目默认使用的是sqllite数据库。可在navcat中查看表数据

    如果想清空数据请在虚拟环境中执行python manage.py flush命令
    然后重新创建超级用户python manage.py createsuperuser

## 添加新的应用程序
    在命令行中切换到manage.py所在的目录
    执行命令 startapp
    python manage.py startapp app_name
    
    定义模型，编辑应用程序目录下的models.py
    from django.db import models
    class NaturalPerson(models.Model):
        """人员信息"""
        # 姓名
        name = models.CharField(max_length=50)
        # 性别
        sex = models.BooleanField()
        # 民族
        nation = models.CharField(max_length=20)
        # 身份证号码
        id = models.CharField(max_length=18, primary_key=True)
        # 住址
        addr = models.CharField(max_length=200)
        # 签发机关
        sio = models.CharField(max_length=100, db_column='signing_and_issuing_organization')
        # 添加日期
        date_added = models.DateTimeField(auto_created=True)
        # 常用返回值
        return_inf = (name, sex, id, addr)
    
        def __str__(self):
            """返回人员信息"""
            return self.return_inf
    ##激活模型
    编辑settings.py中INSTALLED_APPS的值
    --snip--
    INSTALLED_APPS = (
    --snip--
    'django.contrib.staticfiles',
    # 我的应用程序
    'learning_logs',
    )
    --snip--
    把新建的app及模型相关数据添加到数据库中
    python manage.py makemigrations app_name
    python manage.py migrate
    
    ##向管理网站注册新建的models
    编辑app中admin.py文件
    


