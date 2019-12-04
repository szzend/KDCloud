from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
    """
    采购订单处理
    """
    #T_SAL_ORDERTRACE,T_SAL_ORDERTRACEDETAIL,T_SAL_ORDERDISCDETAIL,T_SAL_ORDERENTRY_CRE 空表
    tb_h="T_PUR_POORDER" #单据头表
    tb_e_1="T_PUR_POORDERCLAUSE"   #采购订单条款信息? FENTRYID FID
    tb_e_2="T_PUR_POORDERFIN"     #(采购订单财务信息)FENTRYID FID
    tb_e_3="T_PUR_POORDERINSTALLMENT"    #(采购订单分期付款))FENTRYID FID  订单明细EntryId FORDERENTRYID
    tb_e="T_PUR_POORDERENTRY" #主单据体表
    tb_eeL="T_PUR_POORDERENTRY_L"
    tb_e1="T_PUR_POORDERENTRY_D"  #采购订单明细_物料交货安排)
    #tb_e2="T_SAL_ORDERENTRY_E"  #采购订单明细_关联信息扩展表
    tb_e3="T_PUR_POORDERENTRY_F"  #采购订单明细_财务信息
    tb_ee_1="T_PUR_POENTRYDELIPLAN"  #采购订单物料交货明细 FDETAILID FENTRYID
    tb_ee_2="T_PUR_POORDERENTRY_TAX"   #采购订单税组合  FDETAILID FENTRYID
    tb_ee_3="T_PUR_POORDERACTUALPAY"  #采购订单分期付款实付信息) FDETAILID FENTRYID ->分期付款
    tb_R="T_PUR_POORDERENTRY_R"   #采购订单明细_关联信息
    tb_LK="T_PUR_POORDERENTRY_LK" #采购订单明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e_1)
    b.pEntry(tb_h,tb_e_2)
    b.pEntry(tb_h,tb_e_3)
    b.pEntry(tb_e_3,tb_ee_3,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_h,tb_e1)
    #b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_h,tb_e3)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_ee_2,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do2(start_date:str,end_date:str=""):
    """

    """
    tb_h="T_PUR_POCHANGE"
    tb_e="T_PUR_POCHANGEENTRY"
    tb_LK="T_PUR_POCHANGEENTRY_LK"
    tb_ee_1="T_PUR_POCHANGEENTRYDELIPLAN"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


