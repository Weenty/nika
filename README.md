pip install -r requirements.txt

py manage.py migrate 

py manage.py seeds --all 5

py manage.py runserver 