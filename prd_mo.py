from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
    tb_h="T_PRD_MO" #单据头表
    tb_L="T_PRD_MO_L"
    tb_e="T_PRD_MOENTRY" #主单据体表
    tb_e1="T_PRD_MOENTRY_A"
    tb_e2="T_PRD_MOENTRY_Q"
    tb_eeL="T_PRD_MORPTENTRY_L"
    tb_LK="T_PRD_MOENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def updateLK():
    """
    待实现
    """





"""
import fun
import pandas as pd

headTb1="T_PRD_MO"  #主键FID FBILLNO  生产订单
headTb2="T_PRD_MO_L"    #主键FPKID 外键FID  生产订单多语言表

#主键FENTRYID 外键FID   生产订单表体
#其他外键：
#来源单据ID FSRCBILLID   4种来源单据类型 FSRCBILLTYPE ：SAL_SaleOrder,PLN_PLANORDER,PLN_FORECAST,PRD_MO
#来源单据分录内码 FSRCBILLENTRYID
#销售订单 FSALEORDERID
#销售订单分录内码 FSALEORDERENTRYID
entryTb1="T_PRD_MOENTRY"
entryTb2="T_PRD_MOENTRY_L"  #主键FPKID 外键FENTRYID 生产订单表体多语言 
entryTb3="T_PRD_MOENTRY_A"  #主键FENTRYID 外键FID 生产订单表体，表体拆分，该表主要存储下推选单相关数量等信息
entryTb4="T_PRD_MOENTRY_Q"  #主键FENTRYID 外键FID 明细数量表
lkTb1="T_PRD_MOENTRY_LK"    #主键FLINKID  外键FENTRYID 生产订单反写规则表  其他外键： 源单单据内码 FSBILLID ,源单分录内码 FSID 源单类型同上

################################### 对单据头表处理 ##########################
fidMap=pd.DataFrame()      #用于保存单据头主键映射
head=pd.DataFrame()
billNo=pd.DataFrame()
head=fun.getBillHeaderFromSourceByCreateDate(headTb1,'2019-11-16')
billNo=fun.getKeyBillNo(headTb1)
head=head[~head["FBILLNO"].isin(billNo["FBILLNO"])]  #过滤掉目标表中已经存在的单据编号
fid=head[head["FID"].isin(billNo["FID"])]["FID"] #找出冲突的主键FID
if len(fid)>0:
   fidMap=pd.DataFrame({"to":[i for i in range(9000,len(fid)+9000)]})   #从9000开始对重复键做映射
   fidMap["FID"]=fid
   fidMap["tb"]=headTb1

################################ 对主单据体表处理 ############################
fentryidMap=None    #用于保存单据体主键映射
entry1=fun.getEntriesById(entryTb1,"FID",head["FID"])
fentryId=fun.getPK(entryTb1,"FENTRYID")
fentryId=fentryid[fentryid["FENTRYID"].isin(entry1["FENTRYID"])]
if len(fentryid)>0:
    fentryidMap=pd.DataFrame({"to":[i for i in range(6000,len(fentryid)+6000)]})  #从6000开始对重复键做映射
    fentryidMap["FENTRYID"]=fentryId
    fentryidMap["tb"]=entryTb1

############################### 对单据头语言表处理 ###################################
s_tb2=fun.getEntriesById(headTb2,"FID",billNo["FID"])

"""