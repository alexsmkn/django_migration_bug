# django_migration_bug
Bug demonstration

# How to reproduce:
```sh
mkdir /tmp/django_migration_bug
cd /tmp/django_migration_bug
virtualenv -p python2 env
. ./env/bin/activate
git clone https://github.com/alexsmkn/django_migration_bug.git
cd django_migration_bug
pip install -r requirements.txt
python manage.py migrate
```
