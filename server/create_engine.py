from sqlalchemy import create_engine

def get_db_engine():
    username = 'root'
    password = 'root'
    host = 'localhost'
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/poswithinventorysystem')
    return engine
