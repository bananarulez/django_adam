# Deploy editapp

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --username admin --email test@test
python3 manage.py runserver
```

Open: http://127.0.0.1:8000/
