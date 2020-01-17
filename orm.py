from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.orm import sessionmaker,Session

import os
eng=create_engine(os.environ['TOxx'])
meta=MetaData(eng)
session=Session(bind=eng)
tb_instance=Table("t_bf_instanceentry",meta,autoload=True)
dataset=session.query(tb_instance)
