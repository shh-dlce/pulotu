
## Running the tests

```
coverage run --source='.' --omit='wsgi.py' manage.py test --failfast
coverage report --skip-covered -m  --omit='website/apps/*/migrations/*'
```

## Running flake8

```
flake8 website/ | grep -v migrations | grep -v tests
```


