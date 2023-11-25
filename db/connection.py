# Standard Library
# Standard Library

# Third Party Stuff
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# My Stuff
import credentials

alchemy_url = URL.create(
    drivername="postgresql+psycopg",
    username=credentials.DB_USER,
    host=credentials.DB_HOST,
    database=credentials.DB_NAME,
    port=credentials.DB_PORT,
    password=credentials.DB_PASS,
)

db_engine = create_engine(url=alchemy_url, echo=False)
