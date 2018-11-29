from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text

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
engine = create_engine('mysql+mysqlconnector://tallybook:tallybook@207.246.91.225:3306/jobskill')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)