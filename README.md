# FastFoods
This is an food delivery web application to be used by customers, restaurants, admins and delivery riders.
![FastFoods Main UI](https://github.com/Exprescode/FastFoods/blob/master/images/ui_2.png?raw=true)
![FastFoods Order UI](https://github.com/Exprescode/FastFoods/blob/master/images/ui_1.png?raw=true)
![FastFoods Promo UI](https://github.com/Exprescode/FastFoods/blob/master/images/ui_3.png?raw=true)
![FastFoods Admin UI](https://github.com/Exprescode/FastFoods/blob/master/images/ui_4.png?raw=true)
![FastFoods ER Diagram](https://github.com/Exprescode/FastFoods/blob/master/images/er.png?raw=true)

## Frontend
### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Backend
### Requirements
1. Python 3
2. Postgresql

### Prerequisite
1. Ensure that `postgres` is the password fro `postgres` user in postgresql. The use of other user or password will require modification to the `app.py`.
    - For `psql` in Windows, use `\password postgres` to change `postgres` user password.
    - For Linux ensure that `md5` is set for `postgres` user in `pg_hba.conf` (default path `/etc/postgresql/[VERSION]/main`)
        - Example `local all postgres md5`

2. Run `psql`, then in the same directory as all `.sql` files run `\i create.sql` >  `\i triggers.sql` > `\i fullpopulate.sql` (This may take a few minutes to complete.)

### Setup
1. Run `python -m pip install -r requirements.txt`, assuming the default python is python3
2. For Windows run `python app.py`
3. For Linux run `chmod +x app.py` followed by `./app.py` or `python app.py`
