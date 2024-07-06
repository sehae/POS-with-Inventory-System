from sqlalchemy import create_engine

def get_db_engine():
    # Replace 'username', 'password', 'localhost', 'dbname' with your actual MySQL credentials and database name
    engine = create_engine('mysql+pymysql://root:root@localhost/poswithinventorysystem')
    return engine