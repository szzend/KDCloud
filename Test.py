import os
from sqlalchemy import create_engine
import pandas as pd
import fun
eng=create_engine(os.environ["SNC200"])
input("复制数据后按回车键继续...")
df=pd.read_clipboard()
s=df["FTTABLENAME"]

fun.pInstance(s,eng)

def do(eng,df):
    todo=df.values.tolist()
    result=pd.DataFrame()
    for t in todo:
        sql=f"select min({t[2]}),max({t[2]}) from {t[0]}"
        print(sql)
        _df=pd.read_sql(sql,eng)
        result=result.append(_df)
    return result

def do(eng,tbs):
    df=pd.DataFrame()
    _tbs=tbs["tb"].values.tolist()
    for tb in _tbs:
        sql=f"select FSTABLENAME,FSBILLID,FSID from {tb};"
        _df=pd.read_sql(sql,eng)
        _df["tb"]=tb
        df=df.append(_df)
    return df