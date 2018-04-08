## StubTradeAPI
*Description* : The API is used to provide historic data to FinApp

####How to install
```
git clone <github_url>
cd StubTradeAPI
pip install -r requirements.txt
```

#### How to start server
Migrations can only done the first time. 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

####How to load data to the API

```
python load.py data.csv
```
