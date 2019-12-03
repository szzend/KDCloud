from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
    """
    委外订单
    """
    tb_h="T_SUB_REQORDER" #单据头表
    tb_L="T_SUB_REQORDER_L"
    tb_e="T_SUB_REQORDERENTRY" #主单据体表
    tb_e1="T_SUB_REQORDERENTRY_A"
    tb_eeL="T_SUB_REQORDERENTRY_L"
    tb_LK="T_SUB_REQORDERENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do2(start_date:str,end_date:str=""):
    """
    委外订单变更单
    """
    tb_h="T_SUB_REQCHANGE" #单据头表
    tb_L="T_SUB_REQCHANGE_L"
    tb_e="T_SUB_REQCHANGEENTRY" #主单据体表
    tb_e1="T_SUB_REQCHANGEENTRY_A"
    tb_eeL="T_SUB_REQCHANGEENTRY_L"
    tb_LK="T_SUB_REQCHANGEENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def updateLK():
    """
    待实现
    """


