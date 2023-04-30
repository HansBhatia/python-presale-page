from .create_session import create_session

table_name = "GRAPESCAN.PUBLIC.MAILING_LIST"

def insert_email(email: str):
    # get session
    session = create_session()
    
    # insert
    data = session.sql(f"INSERT INTO {table_name} VALUES ('{email}')")
    data.collect()