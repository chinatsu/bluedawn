# bluedawn

a random discord bot

## setup

requires [poetry](https://python-poetry.org/).

create a file named `secret.py` inside the bot directory. the file should contain the following:

```
TOKEN="your bot token here"
NAME="a name that the bot uses for responses"
```

the following command should take care of dependencies.
```
poetry install
```


## running

```
poetry run python bot
```
