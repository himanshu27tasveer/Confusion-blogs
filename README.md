# Flask Blog and Django Blog

## For Installing them follow these steps!

For installing either of them you have to run command in cmd 
It is recommended if you install these files in a different virtual Environment. For that you have to run below commands in CMD.
```
python -m venv blog
blog\Scripts\activate
```
After that 
`pip3 install -r requirements.txt`

## Configurations for Flask Blog 

For flask blog ypu have to set soem environment variables or use them directly in code (not recommended).
```
EMAIL_USER = 'your gmail address'
EMAIL_PASS = 'your gmail password'
SECRET_KEY = 'some random strings'
SQLALCHEMY_DATABASE_URI = 'url for your database'

```

And finally set your gmail setting to less secure mode (important! if you want to use forgot password facility).

## Configurations for Django Blog

To cofigure your django blog add `EMAIL_USER and EMAIL_PASSWORD`.
