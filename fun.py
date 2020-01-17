import os
from sqlalchemy import create_engine
import pandas as pd
import datetime
#指定数据库
eng_s=create_engine(os.environ["TOSNC"])    #源
eng_t=create_engine(os.environ["To200"])     #目标
#conn_s=eng_s.connect()
#conn_t=eng_t.connect()

#找出目标表中最大的id
def findMaxId(tb,fieldId,eng=eng_t):
    """
    找出目标表中最大的id
    tb:string 为目标表名
    fieldId:string 为id字段名
    返回值为整数或NoneType
    """
    sql=f"select max({fieldId}) from {tb};"
    r=eng.execute(sql)
    return r.fetchone()[0]

def getKeyBillNo(tb:str,key:str="FID",field:str="FBILLNO",eng=eng_t):
    """
    从目标表中得到单据编号及主键FID
    """
    sql=f"select {key},{field} from {tb};"
    return pd.read_sql(sql,eng)

def getPK(tb:str,key:str,eng=eng_t):
    """
    从目标表中得到指定的主键
    """
    sql=f"select {key} from {tb};"
    return pd.read_sql(sql,eng)


def getBillHeaderFromSourceByCreateDate(tb,start_date,end_date="",eng=eng_s):
    """
    依据创建日期取出源表数据(单据头数据表)
    """
    s=""
    if end_date:
        s=f" AND FCREATEDATE<'{end_date}'"
    #sql=f"select * from {tb} where FCREATEDATE>='{start_date}'  {s}"
    #sql=f"select * from T_SAL_DELIVERYNOTICE where FBILLNO in ('FHTZD191231014','FHTZD200104011')"
    #sql=f"select * from T_SAL_OUTSTOCK where FBILLNO in ('XSCKD200109018','XSCKD200109019','XSCKD200109020')"
    sql=f"select * from T_PRD_INSTOCK where FBILLNO in ('SCRK200109326')"


    df= pd.read_sql(sql,eng)
    fdate=datetime.datetime.strptime("2020-02-01","%Y-%m-%d")
    if "FDATE" in df.keys():
        return df[df["FDATE"]<fdate]
    return df



def getEntriesById(tbName:str,fieldId,fids,eng=eng_s):
    """
    避免限制，需分两步来操作
    fids为df列
    """
    #_fids=str(tuple(fids.to_list()))

    id_min=fids.min()
    sql=f"select * from {tbName} where {fieldId} >= {id_min}"
    _df=pd.read_sql(sql,eng)
    _df=_df[_df[fieldId].isin(fids)]
    return _df




def pInstance(s,eng):
    """
    检查t_bf_instanceentry中无效项(目标FTID不存在)
    s为Series
    """
    df=pd.DataFrame()
    
    for ss in s:
        sql="""select * from T_BF_INSTANCEENTRY e where not exists (select 1 from {0} t where t.fentryid=e.FTID and e.FTTABLENAME='{1}') and e.FTTABLENAME='{2}'"""
        if ss[-1:].isdigit():
            tb=ss[:-1]
        else:
            tb=ss
        sql=sql.format(tb,ss,ss)
        _df=pd.read_sql(sql,eng)
        print(f"{tb}:{len(_df)}")
        if len(_df)>0:
            df=df.append(_df)
    df.to_sql("t_bf_instanceentry_qnwb_todelete",eng, if_exists='append', index=False)




"""
with engine.begin() as conn:
    df.to_sql(name='my_balance', con=conn, if_exists='append',
              index=False, index_label='id')

def do(df):
    records=df.to_records()
    name,FNUMBER="",""
    for r in records:
        name=r[2]
        FNUMBER=r[1]
        sql=f"update T_BD_MATERIAL_L set FNAME='{name}' where FMATERIALID in (select FMASTERID  from T_BD_MATERIAL  where FNUMBER='{FNUMBER}')"
        print(conn.execute(sql))


def do(df):
    records=df.to_records()
    name,FNUMBER="",""
    for r in records:
        name=r[2]
        FNUMBER=r[1]
        sql=f"update T_BD_MATERIAL_L set FSPECIFICATION='{name}' where FMATERIALID in (select FMASTERID  from T_BD_MATERIAL  where FNUMBER='{FNUMBER}')"
        print(conn.execute(sql))
"""
