import prd_mo
import sal_order
import pln_forecast
import prd_ppbom
import sub_reqorder
import sub_ppbom
import pur_po
import bd
import prd_pick
import stk

def start():
    """
    """
    start_date="2019-11-16"
    
    prd_pick.do4(start_date)
    """
    sal_order.do(start_date)
    sal_order.do2(start_date)
    sal_order.do3(start_date)
    sal_order.do4(start_date)
    sal_order.do5(start_date)
    sal_order.do6(start_date)
    sal_order.do7()
    pln_forecast.do(start_date)
    pur_po.do1(start_date)
    pur_po.do2(start_date)
    pur_po.do3(start_date)
    pur_po.do4(start_date)
    pur_po.do5(start_date)
    pur_po.do6(start_date)
    stk.do1(start_date)
    stk.do2(start_date)
    stk.do3(start_date)
    stk.do4(start_date)
    stk.do5(start_date)
    stk.do6(start_date)
    stk.do7(start_date)
    stk.do8(start_date)
    stk.do9(start_date)
    prd_mo.do(start_date)
    prd_mo.do2(start_date)
    prd_mo.do3(start_date)
    prd_mo.do4(start_date)
    prd_pick.do1(start_date)
    prd_pick.do2(start_date)
    prd_pick.do3(start_date)
    prd_pick.do4(start_date)
    prd_pick.do5(start_date)
    prd_ppbom.do(start_date)
    prd_ppbom.do2(start_date)
    sub_reqorder.do(start_date)
    sub_reqorder.do2(start_date)
    sub_reqorder.do3(start_date)
    sub_reqorder.do4(start_date)
    sub_reqorder.do5(start_date)
    sub_reqorder.do6(start_date)
    sub_ppbom.do(start_date)
    sub_ppbom.do2(start_date)
    """

if __name__=="__main__":
    start()
