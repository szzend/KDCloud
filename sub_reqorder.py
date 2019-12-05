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


def do3(start_date:str,end_date:str=""):
    """
    委外领料单处理
    """
    
    tb_h="T_SUB_PICKMTRL" #单据头表
    tb_L="T_SUB_PICKMTRL_L"
    tb_e="T_SUB_PICKMTRLDATA" #主单据体表
    tb_e1="T_SUB_PICKMTRLDATA_A"
    tb_eeL="T_SUB_PICKMTRLDATA_L"
    tb_LK="T_SUB_PICKMTRLDATA_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do4(start_date:str,end_date:str=""):
    """
    委外补料单处理
    """
    
    tb_h="T_SUB_FEEDMTRL" #单据头表
    tb_L="T_SUB_FEEDMTRL_L"
    tb_e="T_SUB_FEEDMTRLENTRY" #主单据体表
    tb_e1="T_SUB_FEEDMTRLENTRY_Q"
    tb_eeL="T_SUB_FEEDMTRLENTRY_L"
    tb_LK="T_SUB_FEEDMTRLENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do5(start_date:str,end_date:str=""):
    """
    委外退料单处理
    """
    
    tb_h="T_SUB_RETURNMTRL" #单据头表
    tb_L="T_SUB_RETURNMTRL_L"
    tb_e="T_SUB_RETURNMTRLENTRY" #主单据体表
    tb_e1="T_SUB_RETURNMTRLENTRY_A"
    tb_eeL="T_SUB_RETURNMTRLENTRY_L"
    tb_LK="T_SUB_RETURNMTRL_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do6(start_date:str,end_date:str=""):
    """
    委外超耗单处理
    """
    
    tb_h="T_SUB_EXCONSUME" #单据头表
    tb_L="T_SUB_EXCONSUME_L"
    tb_e="T_SUB_EXCONSUMEENTRY" #主单据体表
    tb_eeL="T_SUB_EXCONSUMEENTRY_L"
    tb_LK="T_SUB_EXCONSUMEENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def updateLK():
    """
    待实现
    """


