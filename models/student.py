from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

students = Table("students", meta, 
                Column("id", Integer, primary_key=True), 
                Column("name", String(255)), 
                Column("nota", Float))

meta.create_all(engine)