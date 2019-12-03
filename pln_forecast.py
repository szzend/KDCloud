from BillWorker import BillWorker

def do(start_date:str,end_date:str=""):
    """
    """
    tb_h="T_PLN_FORECAST"
    tb_L="T_PLN_FORECAST_L"
    tb_e="T_PLN_FORECASTENTRY"
    tb_eeL="T_PLN_FORECASTENTRY_L"
    tb_LK="T_PLN_FORECASTENTRY_LK"
    b=BillWorker()
    b.pHead(tb_h,start_date,end_date)
    b.pEntry(tb_h,tb_L,entryId="FPKID")
    b.pEntry(tb_h,tb_e)
    b.pEntry(tb_e,tb_eeL,headId="FENTRYID",entryId="FPKID")
    b.pEntry(tb_e,tb_LK,headId="FENTRYID",entryId="FLINKID")  #源单各id映射待后续更正
    b.to_sql()

