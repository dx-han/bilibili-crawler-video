# -*- coding: utf-8 -*-
"""Class: Storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
from config import SQL_URI


class Storage():
    """ Store downloaded info into database. """
    def __init__(self, model, df):
        self.table_name = model.__tablename__
        self.model = model
        self.df = df

    @staticmethod
    def start_session(echo=True):
        """Start session for MySQL."""
        engine = create_engine(SQL_URI, echo=echo)
        Session = sessionmaker(bind=engine)
        session = Session()
        return engine, session


    @staticmethod
    def create_table(model, engine):
        """Execute operation of creating table if not exists."""
        if model.__table__.exists(engine):
            pass
            # engine.execute('ALTER TABLE {table} RENAME TO {table}_{timestamp:.0f}'.format(
            #     table=model.__tablename__, timestamp=time.time()
            # ))
        else:
            model.__table__.create(engine)


    def save_data(self):
        """Insert data into database."""
        engine, session = self.start_session()
        self.create_table(self.model, engine)
        data = self.df.to_dict('record')
        session.bulk_insert_mappings(self.model, data)
        self.close_session(session)


    @staticmethod
    def close_session(session):
        """Close session of insert data."""
        session.commit()
        session.close()
