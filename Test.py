import os
from sqlalchemy import create_engine
import pandas as pd
eng=create_engine(os.environ["TOSNC"])
sql=r"update T_PRD_PPBOMENTRY_C set FSTOCKID={0} where FENTRYID={1}"
input("复制数据后按回车键继续...")
df=pd.read_clipboard()
vv=df.values.tolist()

for v in vv:
    sql=sql.format(v[1],v[0])
    eng.execute(sql)
    print(v[0]," done")

