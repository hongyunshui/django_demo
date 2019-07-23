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
6. 安装相关依赖
pip install -r requirements.txt
6.启动项目
python manage.py runserver ip:port

## 说明
此项目使用的是sqllite数据库，其中已经包含部分数据按照以上方法部署完之后即可使用
如果向清空数据请在虚拟环境中执行python manage.py flush命令，然后重新创建超级用户python manage.py createsuperuser

