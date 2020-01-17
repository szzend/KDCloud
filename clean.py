from sqlalchemy import create_engine
import pandas as pd
conn="mssql+pyodbc://act:tofuture@192.168.1.240/SNC200?driver=ODBC+Driver+17+for+SQL+Server"
eng=create_engine(conn)

def cleanLK(eng):
    df=pd.read_sql("select tb  from qnwb_tbnames_forlk",eng)
    _tbs=df["tb"].values.tolist()
    for tb in _tbs:
        sql=f'update lk  set lk.FSID=m."to"  from {tb} lk '
        q=' inner join qnwb_id_map m on lk.FSID=m.source and lk.FSTABLENAME=m.tb where m.source<>m."to" '
        r=eng.execute(sql+q)
        print(f'update {tb}: {r.rowcount} rows data..')
        sql=f'update lk  set lk.FSBILLID=m."to"  from {tb} lk '
        q=' inner join qnwb_id_map m on lk.FSBILLID=m.source and left(lk.FSTABLENAME,len(lk.FSTABLENAME)-5)=m.tb where m.source<>m."to"'
        r=eng.execute(sql+q)
        print(f'update {tb}: {r.rowcount} rows data..')
        sql=f'update lk  set lk.FSBILLID=m."to"  from {tb} lk '
        q=' inner join qnwb_id_map m on lk.FSBILLID=m.source and left(lk.FSTABLENAME,len(lk.FSTABLENAME)-4)=m.tb where m.source<>m."to"'
        r=eng.execute(sql+q)
        print(f'update {tb}: {r.rowcount} rows data..')

def cleanEntry(eng):
    """
    用主子表更新附属子表
    """
    sql="select me,oe from qnwb_tbnames_forentry"
    df=pd.read_sql(sql,eng)
    tbs=df.values.tolist()
    for tb in tbs:
        s1="select * from"
        s2=f'(select a.FID mfid,a.FENTRYID mfentryid,m.source msource,m."to" mto  from {tb[0]} a '
        s3=' inner join qnwb_id_map m on a.FENTRYID=m."to"'
        s4=f" and m.tb='{tb[0]}') t1 inner join"
        s5=f' (select a.FID ofid,a.FENTRYID ofentryid,m.source osource,m."to" oto from {tb[1]} a '
        s6=' inner join qnwb_id_map m on a.FENTRYID=m."to"'
        s7=f" and m.tb='{tb[1]}') t2 on mfid=ofid and msource=osource and mfentryid<>ofentryid"
        sql=s1+s2+s3+s4+s5+s6+s7
        _df=pd.read_sql(sql,eng)
        if _df.empty:
            print(f"{tb[1]} complete")
            continue
        s0=f"select * from {tb[1]}  where exists ( select 1 from ("
        se=" ) t1 where t1.ofentryid=FENTRYID)"
        dff=pd.read_sql(s0+sql+se,eng)
        dff=dff.merge(_df[["ofentryid","mfentryid"]],left_on="FENTRYID",right_on="ofentryid")
        dff.loc[:,"FENTRYID"]=dff["mfentryid"]
        dff=dff.drop(columns=["ofentryid","mfentryid"])
        ss=f"delete from {tb[1]}  where exists ( select 1 from ("
        r=eng.execute(ss+sql+se)
        print(f"{r.rowcount}")
        dff.to_sql("qnwbx_"+tb[1],eng,if_exists="replace",index=False) # ....
        dff.to_sql(tb[1],eng,index=False,if_exists="append")
        print(f"{tb[1]} :{len(dff)} rows updated.")


def cleanWF(eng):
    sql="""
        update t set t.FKEYVALUE=CONVERT(nvarchar(36),m."to") from T_WF_PIBIMAP t 
        inner join qnwb_id_map m on m.tb=CONCAT('T_',t.FOBJECTTYPEID) and m.source=CONVERT(int,FKEYVALUE)  and m.source<>m."to"
        where exists(select 1 from T_WF_PROCINST where t.FPROCINSTID=FPROCINSTID and FCOMPLETETIME is null)
        """
    eng.execute(sql)

def clean12(eng):
    """
    清除导入数据
    """
    #需清除的表来源
    tb_s="qnwb_tbnames_bill"
    tb_imported="qnwb_id_map_12"
    s1=f"select FTABLENAME  from {tb_s}  where FLEVEL=0 and YD is not null"
    tbs=pd.read_sql(s1,eng)["FTABLENAME"].values.tolist()
    for tb in tbs:
        s0=f"delete from {tb}  where FID in ("
        sql=f"select FID from {tb} t inner join {tb_imported} on tb='{tb}' and "+'"to"=t.FID '+" and t.FDATE>'2019-11-30' )"
        print(s0+sql)
        r=eng.execute(s0+sql)
        print(f"{tb} delete {r.rowcount} rows")
    s2=f"select FTABLENAME  from {tb_s}  where FLEVEL=0 and YD is  null"
    tbs=pd.read_sql(s2,eng)["FTABLENAME"].values.tolist()
    for tb in tbs:
        s0=f"delete from {tb}  where FID in ("
        sql=f"select FID from {tb} t inner join {tb_imported} on tb='{tb}' and "+'"to"=t.FID '+" and t.fcreatedate>'2019-11-30' )"
        print(s0+sql)
        r=eng.execute(s0+sql)
        print(f"{tb} delete {r.rowcount} rows")
    s3=f"select FTABLENAME,FPARENT,FPKEY  from {tb_s}  where FLEVEL=1 "
    tbs=pd.read_sql(s3,eng).values.tolist()
    for tb in tbs:
        s0=f"delete from {tb[0]} where FID not in ("
        sql=f"select FID from {tb[1]} )"
        print(s0+sql)
        r=eng.execute(s0+sql)
        print(f"{tb[0]} delete {r.rowcount} rows")
    s4=f"select FTABLENAME,FPARENT,FPKEY  from {tb_s}  where FLEVEL=2 "
    tbs=pd.read_sql(s4,eng).values.tolist()
    for tb in tbs:
        s0=f"delete from {tb[0]} where FENTRYID not in ("
        sql=f"select FENTRYID from {tb[1]} )"
        print(s0+sql)
        r=eng.execute(s0+sql)
        print(f"{tb[0]} delete {r.rowcount} rows")


def getIDMAP(eng):
    df=pd.read_sql("select * from qnwb_tbnames_bill",eng)
    tbs=df.values.tolist()
    for row in tbs:
        t=row[0]
        key=row[2]
        s1=f"insert into qnwb_id_map_all_x select a.*,t.{key} from qnwb_id_map_all a "
        s2=f' left join {t} t on t.{key}=a."to" '+f" where a.tb='{t}'"
        sql=s1+s2
        r=eng.execute(sql)
        print(f"{t} insert into {r.rowcount} rows")
        

if __name__=="__main__":
    clean12(eng)




