# Deployment Steps

## ssh

```
ssh -i "easemypos_key.pem" admin@43.204.117.105
```

## internal

```
cd mychoiceworld
git pull
source .venv/bin/activate
pip install -r requirements.txt

```
if there are any changes to settings.py then 
```
cd internal/internal
nano settings.py
```
if there are models changes then
```
cd /mychoiceworld/internal
python3 manage.py makemigrations
python3 manage.py migrate
```

if there are any tailwind ui changes
```
cd /mychoiceworld/internal
python3 manage.py tailwind build
python3 manage.py collectstatic
```

Important Step for deployement
```
cd /mychoiceworld/internal
gunicorn -c 'config/gunicorn/prod.py'
tail -f '/var/log/gunicorn/error.log'
kill pid
gunicorn -c 'config/gunicorn/prod.py'
sudo systemctl reload nginx
```


## Index

``` 
cd mychoiceworld/index
git pull
./node_modules/.bin/vite build 
sudo systemctl reload nginx

```



# For API authentication using django-rest-knox refer [documention](https://jazzband.github.io/django-rest-knox/)


# Lessons from Production

Never rm your files or directory
create a backup of your database


# Work to-do in application security

## String input escaping in html forms


