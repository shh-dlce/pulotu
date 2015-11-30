
## Running the tests

```
coverage run --source='.' --omit='website/apps/*/migrations/*' manage.py test --failfast
coverage report
```

## Running flake8

```
flake8 website/ | grep -v migrations | grep -v tests
```


