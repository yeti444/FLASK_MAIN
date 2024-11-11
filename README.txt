###############Adatbázis:
PostgreSQL

Adatbázis dump:
db/sql.sql


##############Linux:

.venv létrehozása:
python3 -m venv .venv

Belépés a venv-be
source .venv/bin/activate

Szükséges pip csomagok:
pip install Flask
pip install psycopg2-binary
pip install python-dotenv
pip install bcrypt
pip install pytz
pip install pytest
pip install pytest-xdist
pip install flask_jwt_extended
pip install flask_cors
pip install gunicorn

##############Windows:

.venv létrehozása:
python -m venv .venv

Belépés a venv-be
.venv\Scripts\activate

Szükséges pip csomagok:
pip install Flask
pip install psycopg2
pip install python-dotenv
pip install bcrypt
pip install pytz
pip install pytest
pip install pytest-xdist
pip install flask_jwt_extended
pip install flask_cors
pip install gunicorn

##############.env létrehozása

utils/generate_env.py futtatása

titkos kulcs:
utils/genSecretKey.py futtatása
töltse ki a .env fájlt!

##############gunicorn szerver config módosítása

Ha gunicorn szervert szeretne indítani:
./gunicorn_config.py módosítását ajánlom


##############Szerver futtatása
gunicorn -c gunicorn_config.py app:app

vagy

flask run
