# SqliteWithoutSQL #

## What is this? ##
SqliteWithoutSQL is my first module for using sqlite in python without SQL code.  
It is quite comfortable, because:
- You **haven`t to know** SQL
- There are **all abilities** in the module

## How to install? ##
You can instal sqlitewithoutsql via pip:
```
pip install sqlitewithoutsql
```
Or from [Github](https://github.com/evryz4/sqlitewithoutsql/)

---

## Using ##
### Connecting a database ###
```python
from sqlitewithoutsql.database import Database

db = Database('data.db')
```
### Creating the table ###
```python
from sqlitewithoutsql.database import Database
from sqlitewithoutsql.sqltype import Sqltype

db = Database('data.db')
db.new_table(name='test', col1=Sqltype.INT, col2=Sqltype.STR)
```
### Inserting the values ###
```python
from sqlitewithoutsql.database import Database

db = Database('data.db')
db.insert(table_name='test', 123, 'abc')
```
### Getting the values ###
```python
from sqlitewithoutsql.database import Database

db = Database('data.db')
table = db.get_table(table_name='test')
print(table)
```
### Editing the values ###
```python
from sqlitewithoutsql.database import Database

db = Database('data.db')
db.edit(table_name='test', id=1, column_name='col1', new_value=456)
```
### Deleting the values ###
```python
from sqlitewithoutsql.database import Database

db = Database('data.db')
db.delete(table_name='test', id=1)
```
