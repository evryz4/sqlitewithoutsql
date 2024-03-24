from typing import Any
import sqlite3
from sqltype import Sqltype

class Database:
    def __init__(self, path: str):
        """Connect to the sqlite database
        
        Ps: If you haven't any database, just create a .db file"""

        self._connection = sqlite3.connect(path)
        self._cursor = self._connection.cursor()

    def commit(self):
        """Update the database"""

        self._connection.commit()

    def new_table(self, name: str, **columns: dict[str, Sqltype]):
        """Create new table
        
        name - the name of the table

        columns - kwargs with names of columns and their types"""

        sql = f'create table if not exists {name}(\nid integer primary key autoincrement,\n'
        for col in columns:
            sql += f'{col} {columns[col].value},'
        sql = sql[:-1]
        sql += ')'

        self._cursor.execute(sql)
        self.commit()
    
    def insert(self, table_name: str, *values):
        """Insert values into the table"""
        sql = f'select * from {table_name}'
        columns = []
        for col in self._cursor.execute(sql).description[1:]:
            columns.append(col[0])
        
        columns = ','.join(columns)

        sql = f'insert into {table_name}({columns}) values('
        for value in values:
            if value is None:
                sql += 'NULL,'
            elif type(value) is int:
                sql += str(value) + ','
            elif type(value) is str:
                sql += f'"{value}",'
        sql = sql[:-1]
        sql += ')'

        self._cursor.execute(sql)
        self.commit()
    
    def get_table(self, table_name: str) -> dict[int, dict[str, Any]]:
        """Get the dict: key - table id, data - dict with column names and vars
        
        Example: {1: {col1: 1, col2: 'abc'},
                  2: {col1: 3, col2: 'def'}}"""

        sql = f'select * from {table_name}'
        cols = self._cursor.execute(sql).description[1:]

        ret = {}
        for row in self._cursor.fetchall():
            ret[row[0]] = {}
            for col in range(len(cols)):
                ret[row[0]][cols[col][0]] = row[col+1]

        return ret
    
    def delete(self, table_name: str, id: int):
        """Delete row with entered id in table"""

        sql  = f'delete from {table_name} where id = {id}'
        self._cursor.execute(sql)
        self.commit()
    
    def edit(self, table_name: str, id: int, column_name: str, new_value):
        """Edit the value in column"""

        if isinstance(new_value, int):
            sqlvalue = f'{new_value}'
        else:
            sqlvalue = f'"{new_value}"'

        sql = f'update {table_name} set {column_name} = {sqlvalue} where id = {id}'
        self._cursor.execute(sql)
        self.commit()
