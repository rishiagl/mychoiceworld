# Deployment Steps

## Core

```
cd mychoiceworld
git pull
source .venv/bin/activate
pip install -r requirements.txt

```
if there are any changes to settings.py then 
```
cd core/core
nano settings.py
```
if there are models changes then
```
cd /mychoiceworld/core
python3 manage.py makemigrations
python3 manage.py migrate
```

if there are any tailwind ui changes
```
cd /mychoiceworld/core
pyhton3 manage.py tailwind build
```

Important Step for deployement
```
cd /mychoiceworld/core
gunicorn -c 'config/gunicorn/prod.py'
tail -f '/var/log/gunicorn/error.py'
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

