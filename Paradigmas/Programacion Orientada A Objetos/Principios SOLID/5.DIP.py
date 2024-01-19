from abc import ABC, abstractmethod

# Dependecy Inversion Principle

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL database:", data)

class PostgreSQLDatabase(Database):
    def save(self, data):
        print("Saving data to PostgreSQL database:", data)

class Application:
    def __init__(self, database):
        self.database = database

    def process_data(self, data):
        self.database.save(data)

data = "Hello, World!"

mysql_db = MySQLDatabase()
app = Application(mysql_db)
app.process_data(data)

postgres_db = PostgreSQLDatabase()
app = Application(postgres_db)
app.process_data(data)

