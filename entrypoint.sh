python /web/manage.py migrate
#create default user Groups with related permissions
python /web/manage.py create_groups
python /web/manage.py runserver 0.0.0.0:8000