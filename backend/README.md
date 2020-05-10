# CS2102-backend
## Requirements
1. Python 3
2. Postgresql

## Setup Database

1. Connect to postgresql using `psql` and change password of different `postgres` user to `postgres` or other password but this will require a change in the password in `app.py`
- Change the password using `\password postgres`
- For Linux make sure that under `pg_hba.conf` (`/etc/postgresql/[VERSION]/main`), the method for postgres user is `md5` to allow manual password authentication
    - Example  `local all postgres md5`

1. Run `psql` and then in the same directory as the `.sql` files run `\i create.sql` >  `\i triggers.sql` > `\i fullpopulate.sql` (this might take awhile due to the large number of statements and 1 or 2 insertion errors might occur due to the large number of transactions)

## Setup script
1. `python -m pip install -r requirements.txt`, assuming the default python is python3

2. For Linux: `chmod +x app.py` then `./app.py` or `python app.py`
3. For Windows: `python app.py`