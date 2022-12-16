import os
from contextlib import contextmanager
from typing import Generator

from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import config


class SessionMaker:
    def __init__(self, user, password, url, db_name, ssl_dir=None):
        self.login = {
            "user": user,
            "password": password,
            "url": url,
            "db_name": db_name,
        }
        if ssl_dir:
            self.ssl_files = {
                "ca": os.path.join(ssl_dir, "server-ca.pem"),
                "key": os.path.join(ssl_dir, "client-key.pem"),
                "cert": os.path.join(ssl_dir, "client-cert.pem"),
                "check_hostname": False,
            }
        else:
            self.ssl_files = None
        self.uri = f"mysql+pymysql://{self.login['user']}:{self.login['password']}@{self.login['url']}/{self.login['db_name']}"
        self.engine = create_engine(self.uri, connect_args={"ssl": self.ssl_files})
        self.sessionmaker = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def yield_db(self) -> Generator[Session, None, None]:
        """This generator is a helper function that can be called to create
        a context manager on the fly. In particular this is used by FastAPI."""
        Session = self.sessionmaker()
        self._db = Session
        try:
            yield self._db
        finally:
            self._db.close()

    @contextmanager
    def get_db(self) -> Generator[Session, None, None]:
        return self.yield_db()


db = SessionMaker(**config["SQL"])

# Dependency.
# The request of the session is handled by the middleware
def get_db(request: Request):
    """Gets the DB\n
    The request of the session is handled by the middleware

    Args:
        request (Request): Request object

    Returns:
        Database object
    """
    return request.state.db


Base = declarative_base()
