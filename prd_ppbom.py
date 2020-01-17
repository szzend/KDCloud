from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
    """
    生产订单用料清单
    """
    tb_h="T_PRD_PPBOM" #单据头表
    tb_L="T_PRD_PPBOM_L"
    tb_e="T_PRD_PPBOMENTRY" #主单据体表
    tb_e1="T_PRD_PPBOMENTRY_C"
    tb_e2="T_PRD_PPBOMENTRY_Q"
    tb_eeL="T_PRD_PPBOMENTRY_L"
    tb_LK="T_PRD_PPBOMENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    #b.pEntry(tb_h,tb_e1)
    #b.pEntry(tb_h,tb_e2)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntryX(tb_e,tb_e2,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do2(start_date:str,end_date:str=""):
    """
    生产订单用料清单变更单
    """
    tb_h="T_PRD_PPBOMCHANGE" #单据头表
    tb_L="T_PRD_PPBOMCHANGE_L"
    tb_e="T_PRD_PPBOMCHANGEENTRY" #主单据体表
    tb_e1="T_PRD_PPBOMCHANGEENTRY_C"
    tb_e2="T_PRD_PPBOMCHANGEENTRY_Q"
    tb_eeL="T_PRD_PPBOMCHANGEENTRY_L"
    tb_LK="T_PRD_PPBOMCHANGEENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    #b.pEntry(tb_h,tb_e1)
    #b.pEntry(tb_h,tb_e2)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntryX(tb_e,tb_e2,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def updateLK():
    """
    待实现
    """


