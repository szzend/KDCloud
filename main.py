import prd_mo
import sal_order
import pln_forecast
import prd_ppbom
import sub_reqorder
import sub_ppbom

def start():
    """
    """
    start_date="2019-11-16"
    #pln_forecast.do(start_date) #预测单处理
    #sal_order.do(start_date)    #销售订单处理

    #prd_mo.do(start_date)      #生产订单处理
    #prd_ppbom.do(start_date)    #生产用料清单处理
    #prd_ppbom.do2(start_date)
    #sub_reqorder.do(start_date)
    #sub_reqorder.do2(start_date)
    sub_ppbom.do(start_date)
    sub_ppbom.do2(start_date)

if __name__=="__main__":
    start()
