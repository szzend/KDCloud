from BillWorker import BillWorker

def do1(start_date:str,end_date:str=""):
    """
    供应商联系人
    """
    tb_h="T_BD_COMMONCONTACT"   #(供应商（客户）联系人) 主键FCONTACTID
    tb_L="T_BD_COMMONCONTACT_L"
    b=BillWorker()
    b.pHead_b(tb_h,start_date,end_date,fieldId="FCONTACTID")
    b.pEntry(tb_h,tb_L,headId="FCONTACTID",entryId="FPKID")
    b.to_sql()

def do2(start_date:str,end_date:str=""):
    """
    供应商
    """
    tb_h="t_bd_supplier".upper()   #供应商 主键FSupplierId
    tb_L="t_bd_supplier_l".upper()
    tb_e="t_bd_supplierbase".upper()    #供应商基本属性
    tb_e1="t_bd_supplierbusiness".upper()   #供应商商务属性)
    tb_e_1="t_bd_suppliercontact".upper()   #供应商联系人FContactId 
    tb_e_2="t_bd_supplierfinance".upper()   #供应商财务属性
    tb_e_3="t_bd_supplierlocation".upper()  #供应商组织属性FLocationId
    b=BillWorker()
    b.pHead_b(tb_h,start_date,end_date,fieldId="FSUPPLIERID")
    b.pEntry(tb_h,tb_L,headId="FSUPPLIERID",entryId="FPKID")
    b.pEntry(tb_h,tb_e,headId="FSUPPLIERID")
    b.pEntry(tb_h,tb_e1,headId="FSUPPLIERID")
    b.pEntry(tb_h,tb_e_1,headId="FSUPPLIERID",entryId="FCONTACTID")
    b.pEntry(tb_h,tb_e_2,headId="FSUPPLIERID")
    b.pEntry(tb_h,tb_e_3,headId="FSUPPLIERID",entryId="FLOCATIONID")
    b.to_sql()


def do3(start_date:str,end_date:str=""):
    """
    客户
    """
    tb_h="T_BD_CUSTOMER"   #客户) 主键FCUSTID
    tb_L="T_BD_CUSTOMER_L"
    tb_e="T_BD_CUSTCONTACT"    #客户联系人FCUSTID FENTRYID
    tb_e1="T_BD_CUSTLOCATION"   #客户地点FCUSTID FENTRYID
    tb_e_1="T_BD_CUSTOMER_F"   #客户扩展表_财务 此表无主键，以外键代替
    tb_e_2="T_BD_CUSTOMEREXT"   #客户扩展表FCUSTID FENTRYID
    tb_e_3="T_BD_CUSTORDERORG"  #客户订货组织 FCUSTID FENTRYID
    b=BillWorker()
    b.pHead_b(tb_h,start_date,end_date,fieldId="FCUSTID")
    b.pEntry(tb_h,tb_L,headId="FCUSTID",entryId="FPKID")
    b.pEntry(tb_h,tb_e,headId="FCUSTID")
    b.pEntry(tb_h,tb_e1,headId="FCUSTID")
    b.pEntry(tb_h,tb_e_1,headId="FCUSTID",entryId="FCUSTID")
    b.pEntry(tb_h,tb_e_2,headId="FCUSTID")
    b.pEntry(tb_h,tb_e_3,headId="FCUSTID")
    b.to_sql()

