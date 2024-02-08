"""
Task-1: Create context manager for Session class where se
"""

class DataBase:
    def open(self):
        pass

    def close(self):
        pass

    def connect(self):
        return ConSession(self)


class ConSession:

    def __init__(self, data_base: DataBase):
        self.data_base = data_base

    def __enter__(self):
        return self.data_base.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data_base.close()

    def execute(self, query):
        print(f"Execute query: {query}")
        # execute data base query
        pass


def test_connection():
    db = DataBase()
    with db.connect() as session:
        session.execute('SELECT * FROM table')
