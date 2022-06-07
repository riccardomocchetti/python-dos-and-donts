from snowflake.connector import ProgrammingError, connect

class MyApplicationError(RuntimeError):
    pass

connection = connect(...)


# Don't do this
def send_query(query):
    try:
        connection.cursor().execute(query)
        connection.commit()
    except ProgrammingError:
        raise MyApplicationError()
    finally:
        connection.close()


# Do this instead
def send_query(query):
    try:
        connection.cursor().execute(query)
        connection.commit()
    except ProgrammingError as error:
        raise MyApplicationError() from error
    finally:
        connection.close()