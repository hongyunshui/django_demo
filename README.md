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
    python manage.py makemigrations app01
    python manage.py migrate
    9.创建超级用户
    python manage.py createsuperuser
    8.启动项目
    python manage.py runserver ip:port

## 说明
    此项目默认使用的是sqllite数据库。可在navcat中查看表数据

    如果想清空数据请在虚拟环境中执行python manage.py flush命令
    然后重新创建超级用户python manage.py createsuperuser

