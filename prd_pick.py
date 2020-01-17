from BillWorker import BillWorker

def do1(start_date:str,end_date:str=""):
    """
    生产领料单处理
    """
    #T_PRD_PICKMTRLDATA_C T_PRD_PICKMTRLDATA_CE 核算表不引入
    tb_h="T_PRD_PICKMTRL" #单据头表
    tb_L="T_PRD_PICKMTRL_L"
    tb_e="T_PRD_PICKMTRLDATA" #主单据体表
    tb_e1="T_PRD_PICKMTRLDATA_A"
    tb_eeL="T_PRD_PICKMTRLDATA_L"
    tb_LK="T_PRD_PICKMTRLDATA_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    #b.pEntry(tb_h,tb_e1)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

def do2(start_date:str,end_date:str=""):
    """
    生产退料单处理
    """
    #T_PRD_RETURNMTRLENTRY_C T_PRD_RETURNMTRLENTRY_CE 核算表不引入
    tb_h="T_PRD_RETURNMTRL" #单据头表
    tb_L="T_PRD_RETURNMTRL_L"
    tb_e="T_PRD_RETURNMTRLENTRY" #主单据体表
    tb_e1="T_PRD_RETURNMTRLENTRY_A"
    tb_eeL="T_PRD_RETURNMTRLENTRY_L"
    tb_LK="T_PRD_RETURNMTRLENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    #b.pEntry(tb_h,tb_e1)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do3(start_date:str,end_date:str=""):
    """
    生产退库单处理
    """
    #T_PRD_RESTOCKENTRY_C T_PRD_RESTOCKENTRY_CE T_PRD_RESTOCKENTRY_CF 核算表不引入
    tb_h="T_PRD_RESTOCK" #单据头表
    tb_L="T_PRD_RESTOCK_L"
    tb_e="T_PRD_RESTOCKENTRY" #主单据体表
    tb_e1="T_PRD_RESTOCKENTRY_A"
    tb_eeL="T_PRD_RESTOCKENTRY_L"
    tb_LK="T_PRD_RESTOCKENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    #b.pEntry(tb_h,tb_e1)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do4(start_date:str,end_date:str=""):
    """
    生产入库单处理
    """
    #T_PRD_INSTOCKENTRY_C T_PRD_INSTOCKENTRY_CE T_PRD_INSTOCKENTRY_CF 核算表不引入
    tb_h="T_PRD_INSTOCK" #单据头表
    tb_L="T_PRD_INSTOCK_L"
    tb_e="T_PRD_INSTOCKENTRY" #主单据体表
    tb_e1="T_PRD_INSTOCKENTRY_A"
    tb_eeL="T_PRD_INSTOCKENTRY_L"
    tb_LK="T_PRD_INSTOCKENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()


def do5(start_date:str,end_date:str=""):
    """
    生产补料单处理
    """
    #T_PRD_FEEDMTRLDATA_C T_PRD_FEEDMTRLDATA_CE 核算表不引入
    tb_h="T_PRD_FEEDMTRL" #单据头表
    tb_L="T_PRD_FEEDMTRL_L"
    tb_e="T_PRD_FEEDMTRLDATA" #主单据体表
    tb_e1="T_PRD_FEEDMTRLDATA_Q"
    tb_eeL="T_PRD_FEEDMTRLDATA_L"
    tb_LK="T_PRD_FEEDMTRLDATA_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    #b.pEntry(tb_h,tb_e1)
    b.pEntryX(tb_e,tb_e1,tb_h)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()
