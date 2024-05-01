from PySide6 import QtWidgets, QtSql

class Connect:
    def __init__(self):
        super().__init__(Connect, self)

    def create_connect(self):
        db = QtSql.QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('')
        db.setHostName('')
        db.setPassword('')
        db.setUserName('')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        self.query = QtSql.QSqlQuery()

        self.query.exec(
                """CREATE TABLE IF NOT EXISTS translator_info (
                    id serial PRIMARY KEY,
                    user_text REAL,
                    translate_text REAL
                );"""
            )
        

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query
   

    def inserts(self, user_text, translate_text):
        self.sql_query = ('INSERT INTO translator_info(user_text, translate_text) VALUES(?, ?);')
        self.execute_query_with_params(self.sql_query, [user_text, translate_text])
