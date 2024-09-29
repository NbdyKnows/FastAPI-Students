from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv 
import os

load_dotenv()

engine = create_engine(os.getenv("route"))

meta = MetaData()

conn = engine.connect()