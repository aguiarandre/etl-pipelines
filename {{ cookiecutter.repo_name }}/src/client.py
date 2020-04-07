from sqlalchemy import create_engine
import logging
import os

logger = logging.getLogger('client.py')


class Client:
    """
    Connection to the database. 

    The current implementation only refers to the PostgreSQL 
    database, however, this could be easily enhanced to any 
    database at all, including cloud.
    """

    def __init__(self, params):
        """
        Connect to the database.

        Use the information contained in the params.py file 
        to connect to the postgreSQL database.
        """


        try:
            self.engine = create_engine(f'postgresql+psycopg2://{params.user}:{params.password}@{params.host}/{params.database}')
            self.conn = self.engine.connect()
        except Exception as e:
            logger.warning('Could not connect to the database on client.py file.')
            logger.warning('Verify your credentials for {params.user}.')
            logger.warning(e)
