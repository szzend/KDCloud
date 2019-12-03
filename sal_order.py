from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
    """
    """
    #T_SAL_ORDERTRACE,T_SAL_ORDERTRACEDETAIL,T_SAL_ORDERDISCDETAIL,T_SAL_ORDERENTRY_CRE 空表
    tb_h="T_SAL_ORDER" #单据头表
    tb_e_1="T_SAL_ORDERCLAUSE"   #销售订单条款信息? FENTRYID FID
    tb_e_2="T_SAL_ORDERFIN"     #(销售订单财务信息)FENTRYID FID
    tb_e_3="T_SAL_ORDERPLAN"    #(销售订单收款计划)FENTRYID FID  订单明细EntryId FORDERENTRYID
    tb_e="T_SAL_ORDERENTRY" #主单据体表
    tb_e1="T_SAL_ORDERENTRY_D"  #销售订单明细_物料交货安排)
    tb_e2="T_SAL_ORDERENTRY_E"  #销售订单明细_关联信息扩展表
    tb_e3="T_SAL_ORDERENTRY_F"  #销售订单明细_财务信息
    tb_ee_1="T_SAL_ORDERENTRYDELIPLAN"  #销售订单物料交货明细 FDETAILID FENTRYID
    tb_ee_2="T_SAL_ORDERENTRYTAX"   #销售订单税组合  FDETAILID FENTRYID
    tb_ee_3="T_SAL_ORDERPLANENTRY"  #销售订单收款计划明细 FDETAILID FENTRYID ->收款计划
    tb_R="T_SAL_ORDERENTRY_R"   #销售订单明细_关联信息
    tb_LK="T_SAL_ORDERENTRY_LK" #销售订单明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e_1)
    b.pEntry(tb_h,tb_e_2)
    b.pEntry(tb_h,tb_e_3)
    b.pEntry(tb_e_3,tb_ee_3,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_h,tb_e3)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_ee_2,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()