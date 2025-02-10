from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, Result
from typing import Any, Dict, List, Optional

from config import Config

class DatabaseManager:
    def __init__(self, connection_string: str):
        self.engine: Engine = create_engine(Config.SQL_ALCHEMY_DATABASE_URI)

    def execute_ddl(self, ddl_statement: str) -> None:
        """
        Execute a DDL statement (e.g., CREATE TABLE, ALTER TABLE).
        """
        with self.engine.connect() as connection:
            connection.execute(text(ddl_statement))
            connection.commit()

    def execute_insert(self, insert_statement: str, params: Optional[Dict[str, Any]] = None) -> None:
        """
        Execute an INSERT statement.
        params: Dictionary of parameters to bind.
        """
        with self.engine.connect() as connection:
            connection.execute(text(insert_statement), params or {})
            connection.commit()

    def execute_query(self, query_statement: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a SELECT query statement.
        params: Dictionary of parameters to bind.
        Returns list of dictionaries representing rows.
        """
        with self.engine.connect() as connection:
            result: Result = connection.execute(text(query_statement), params or {})
            rows = result.mappings().all()
            return [dict(row) for row in rows]

# Example usage:
if __name__ == "__main__":
    # Update the connection string for your database; example uses SQLite:
    db = DatabaseManager("sqlite:///example.db")

    # Example DDL: create a table
    ddl = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    );
    """
    db.execute_ddl(ddl)

    # Example insertion: insert a user
    insert_sql = "INSERT INTO users (name, email) VALUES (:name, :email)"
    db.execute_insert(insert_sql, {"name": "Alice", "email": "alice@example.com"})

    # Example query: select all users
    select_sql = "SELECT * FROM users"
    users = db.execute_query(select_sql)
    print(users)