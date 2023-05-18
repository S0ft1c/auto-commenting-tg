import duckdb


class DuckDB(object):

    def __init__(self):
        # creating database
        self.conn = duckdb.connect('database.duckdb')
        self.c = self.conn.cursor()

        self.c.sql("""create table if not exists channels (
        channel_name string,
        )""")

        self.c.sql("""create table if not exists phrases (
        phrase string,
        )""")

    def sql_req(self, req: str):
        return self.c.sql(req)

    def __del__(self):
        self.conn.close()


db = DuckDB()
