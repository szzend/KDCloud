from BillWorker import BillWorker

def do1(start_date:str,end_date:str=""):
    """
    采购订单处理
    """

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
    采购订单变更单处理
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


def do3(start_date:str,end_date:str=""):
    """
    收料通知单处理
    """
    tb_h="T_PUR_RECEIVE" #单据头表采购收料单)
    tb_e_2="T_PUR_RECEIVEFIN"     #(采购订单财务信息)FENTRYID FID
    tb_e="T_PUR_RECEIVEENTRY" #主单据体表
    tb_eeL="T_PUR_RECEIVEENTRY_L"
    tb_e2="T_PUR_RECEIVEENTRY_S"  #收料单分录交货入库表
    tb_e3="T_PUR_RECEIVEENTRY_F"  #收料单据分录财务表)
    tb_ee_1="T_PUR_RECEIVEDISCDETAIL"  #收料单折扣明细表) FDETAILID FENTRYID
    tb_ee_2="T_PUR_RECEIVEENTRY_TAX"   #收料单税组合)  FDETAILID FENTRYID
    tb_R="T_PUR_RECEIVEENTRY_R"   #收料单明细关联信息
    tb_LK="T_PUR_RECEIVEENTRY_LK" #收料单明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e_2)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_h,tb_e3)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_ee_2,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do4(start_date:str,end_date:str=""):
    """
    采购申请单处理
    """
    tb_h="T_PUR_REQUISITION" #单据头表采购申请单)
    tb_e="T_PUR_REQENTRY" #主单据体表
    tb_eeL="T_PUR_REQENTRY_L"
    tb_e2="T_PUR_REQENTRY_S"  #采购申请物料明细_货源
    tb_R="T_PUR_REQENTRY_R"   #采购申请单明细关联信息
    tb_LK="T_PUR_REQENTRY_LK" #采购申请单明细关联表) 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do5(start_date:str,end_date:str=""):
    """
    采购退料单处理
    """
    tb_h="T_PUR_MRB" #单据头表
    tb_e="T_PUR_MRBENTRY" #主单据体表
    tb_e_1="T_PUR_MRBENTRY_I"   #退料单明细_库存扩展） FENTRYID FID
    tb_e_2="T_PUR_MRBFIN"     #(退料单财务信息)FENTRYID FID
    tb_eeL="T_PUR_MRBENTRY_L"
    tb_e3="T_PUR_MRBENTRY_F"  #采购退料单明细_财务信息
    tb_ee_1="T_PUR_MRBDISCDETAIL"  #入库单折扣明细表) FDETAILID FENTRYID
    tb_ee_2="T_PUR_MRBENTRY_TAX"   #采购退料单税组合  FDETAILID FENTRYID
    tb_ee_3="T_PUR_MRBENTRYCOST"  #入库单明细采购费用) FDETAILID FENTRYID 
    #tb_R="T_PUR_POORDERENTRY_R"   #采购入库单明细_关联信息
    tb_LK="T_PUR_MRBENTRY_LK" #采购退料单明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e_1)
    b.pEntry(tb_h,tb_e_2)
    b.pEntry(tb_e,tb_ee_3,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    #b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_h,tb_e3)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_ee_2,headId="FENTRYID",entryId="FDETAILID")
    #b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do6(start_date:str,end_date:str=""):
    """
    采购调价表处理
    """
    tb_h="T_PUR_PAT"
    tb_e="T_PUR_PATENTRY"
    tb_LK="T_PUR_PATENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()
