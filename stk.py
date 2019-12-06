from BillWorker import BillWorker

def do1(start_date:str,end_date:str=""):
    """
    采购入库单处理
    """
    #T_STK_INSTOCKENTRY_C，T_STK_INSTOCKENTRY_CA，T_STK_INSTOCKENTRY_CE，T_STK_INSTOCKENTRY_CF，T_STK_INSTOCKENTRY_CH
    tb_h="T_STK_INSTOCK" #单据头表
    tb_e_1="T_STK_INSTOCKENTRY_I"   #入库单分录，库存需求拆分表) FENTRYID FID
    tb_e_2="T_STK_INSTOCKFIN"     #(采购入库单财务信息)FENTRYID FID
    tb_e="T_STK_INSTOCKENTRY" #主单据体表
    #tb_eeL="T_PUR_POORDERENTRY_L"
    tb_e3="T_STK_INSTOCKENTRY_F"  #采购入库单明细_财务信息
    tb_ee_1="T_STK_INSTOCKDISCDETAIL"  #入库单折扣明细表) FDETAILID FENTRYID
    tb_ee_2="T_STK_INSTOCKENTRY_TAX"   #采购入库单税组合  FDETAILID FENTRYID
    tb_ee_3="T_STK_INSTOCKPURCOST"  #入库单明细采购费用) FDETAILID FENTRYID 
    #tb_R="T_PUR_POORDERENTRY_R"   #采购入库单明细_关联信息
    tb_LK="T_STK_INSTOCKENTRY_LK" #采购入库单明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e_1)
    b.pEntry(tb_h,tb_e_2)
    b.pEntry(tb_e,tb_ee_3,headId="FENTRYID",entryId="FDETAILID")
    #b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    #b.pEntry(tb_h,tb_e2)
    b.pEntry(tb_h,tb_e3)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_ee_2,headId="FENTRYID",entryId="FDETAILID")
    #b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do2(start_date:str,end_date:str=""):
    """
    批号调整单处理
    """
    tb_h="T_STK_LOTADJUST" #单据头表
    tb_e="T_STK_LOTADJUSTENTRY" #主单据体表
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.to_sql()


def do3(start_date:str,end_date:str=""):
    """
    其他入库单处理
    """
    tb_h="T_STK_MISCELLANEOUS" #单据头表
    tb_e="T_STK_MISCELLANEOUSENTRY" #主单据体表
    tb_R="T_STK_MISCELLANEOUSENTRY_R"   #明细_关联信息
    tb_LK="T_STK_MISCELLANEOUSENTRY_LK" #明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do4(start_date:str,end_date:str=""):
    """
    其他出库单处理
    """
    tb_h="T_STK_MISDELIVERY" #单据头表
    tb_e="T_STK_MISDELIVERYENTRY" #主单据体表
    tb_R="T_STK_MISDELIVERYENTRY_R"   #明细_关联信息
    tb_LK="T_STK_MISDELIVERYENTRY_LK" #明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do5(start_date:str,end_date:str=""):
    """
    受托加工材料入库单处理
    """
    tb_h="T_STK_OEMINSTOCK" #单据头表
    tb_e="T_STK_OEMINSTOCKENTRY" #主单据体表
    tb_R="T_STK_OEMINSTOCKENTRY_R"   #关联信息
    tb_LK="T_STK_OEMINSTOCKENTRY_LK" #明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do6(start_date:str,end_date:str=""):
    """
    库存盘亏单)处理
    """
    tb_h="T_STK_STKCOUNTLOSS" #单据头表
    tb_e="T_STK_STKCOUNTLOSSENTRY" #主单据体表
    tb_LK="T_STK_STKCOUNTLOSSENTRY_LK" #明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do7(start_date:str,end_date:str=""):
    """
    库存盘盈单)处理
    """
    tb_h="T_STK_STKCOUNTGAIN" #单据头表
    tb_e="T_STK_STKCOUNTGAINENTRY" #主单据体表
    tb_LK="T_STK_STKCOUNTGAINENTRY_LK" #明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do8(start_date:str,end_date:str=""):
    """
    直接调拨/分步式调入单处理
    """
    tb_h="T_STK_STKTRANSFERIN" #单据头表
    tb_e="T_STK_STKTRANSFERINENTRY" #主单据体表
    tb_e_1="T_STK_STKTRANSFERINENTRY_T" #调入单分录扩展表
    tb_e_2="T_STK_STKTRANSFERINENTRY_E" #调入单分录扩展表2）
    tb_R="T_STK_STKTRANSFERINENTRY_R"   #关联信息
    tb_LK="T_STK_STKTRANSFERINENTRY_LK" #明细关联表 
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e_1)
    b.pEntry(tb_h,tb_e_2)
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do9(start_date:str,end_date:str=""):
    """
    组装拆卸单处理
    """
    tb_h="T_STK_ASSEMBLY" #单据头表
    tb_e="T_STK_ASSEMBLYPRODUCT" #主单据体表
    tb_R="T_STK_ASSEMBLYPRODUCT_R"   #明细_关联信息
    tb_LK="T_STK_ASSEMBLYPRODUCT_LK" #明细关联表 
    tb_ee_1="T_STK_ASSEMBLYSUBITEM"  #组装/拆卸单子件表 FDETAILID FENTRYID
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_R)
    b.pEntry(tb_e,tb_ee_1,headId="FENTRYID",entryId="FDETAILID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()