from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from config import DbConfig

username = DbConfig.username
password = DbConfig.password
host = DbConfig.host
database = DbConfig.database
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class positionIds(Base):
    # 表的名字:
    __tablename__ = 'position_ids'

    # 表的结构:
    position_id = Column(Integer, primary_key=True)
    job = Column(String(255))
    status = Column(Integer)

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://'+username+':'+password+'@'+host+'/'+database)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)