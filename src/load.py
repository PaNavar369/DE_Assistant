import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def load_data(df):

    database_url = os.getenv("mysql+pymysql://root:root@localhost:3306/de_assistant")

    if not database_url:
        raise ValueError("DATABASE_URL is not configured.")

    engine = create_engine(database_url)

    df.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False
    )

    return True