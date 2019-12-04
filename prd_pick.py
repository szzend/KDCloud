from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
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
    b.pEntry(tb_h,tb_e1)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

