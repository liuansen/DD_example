# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings


Base = declarative_base()


class AccessToken(Base):
    __tablename__ = 'access_token'

    id = Column(String(20), primary_key=True)
    access_token = Column(String(256))


if __name__ == '__main__':
    engine = create_engine(settings.MYSQL_CONNECT)
    Base.metadata.create_all(engine)
