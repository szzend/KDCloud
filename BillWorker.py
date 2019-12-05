import fun
import pandas as pd

class BillWorker:
    """

    """
    def __init__(self, *args, **kwargs):
        self.data_todo={}       #用于保存已处理好的待补入的数据
        self.data_map={}        #用于保存待写入数据表的主键映射数据
    def pHead(self,headTb:str,start_date:str,end_date="",fieldId:str="FID"):
        """
        处理单据头
        """
        head=fun.getBillHeaderFromSourceByCreateDate(headTb,start_date,end_date)
        if head.empty:
            print(f"表{headTb}在指定期间无数据...")
            return
        billNo=fun.getKeyBillNo(headTb)
        head=head[~head["FBILLNO"].isin(billNo["FBILLNO"])]  #过滤掉目标表中已经存在的单据编号
        if head.empty:
            print(f"单据头表:{headTb}无需新增数据")
            return
        fid=head[head[fieldId].isin(billNo[fieldId])][fieldId] #找出冲突的主键FID
        if not fid.empty:   #有冲突主键时须记录映射并修改数据表
            _source=fid.sort_values().to_list()
            _m=pd.DataFrame({"source":_source,"to":[i for i in range(9000,len(_source)+9000)]})   #从9000开始对重复键做映射
            _df=head.merge(_m,how="left",left_on=fieldId,right_on="source") 
            _s=_df["to"].fillna(_df[fieldId]).astype('int32')  #填充非映射键
            _map=pd.DataFrame({"source":_df[fieldId],"to":_s})
            _map.loc[:,"tb"]=headTb
            _map.loc[:,"field"]=fieldId
            _df.loc[:,fieldId]= _s    
            _df=_df.drop(columns=["source","to"])
            self.data_todo[headTb]=_df
            self.data_map[headTb]=_map
        else:       #无冲突主键则直接添加到待处理
            self.data_todo[headTb]=head
            _map=pd.DataFrame({"source":head[fieldId],"to":head[fieldId]})
            _map.loc[:,"tb"]=headTb
            _map.loc[:,"field"]=fieldId
            self.data_map[headTb]=_map
        print(f"单据头表:{headTb}预处理完成")


    def pEntry(self,headTb:str,entryTb:str,headId:str="FID",entryId:str="FENTRYID"):
        """
        headTb为主表，entryTb为子表。默认主键分别为FID及FENTRYID
        """
        if headTb not in self.data_map.keys():  #无数据需处理，返回
            return
        _id=self.data_map[headTb]["source"]
        _data=fun.getEntriesById(entryTb,headId,_id) #源表数据
        if _data.empty:
            print(f"{entryTb}表中无新增数据..")
            return
        _pk_t=fun.getPK(entryTb,entryId)  #目标表中主键
        _pk_t=_pk_t[_pk_t[entryId].isin(_data[entryId])][entryId]
        if not _pk_t.empty:
            #注意列赋值时会进行索引对齐
            _source=_pk_t.sort_values().to_list()
            _m=pd.DataFrame({"source":_source,"to":[i for i in range(6000,len(_source)+6000)]})   #从6000开始对重复键做映射
            _df=_data.merge(_m,how="left",left_on=entryId,right_on="source") 
            _s=_df["to"].fillna(_df[entryId]).astype('int32')  #填充非映射键
            _map=pd.DataFrame({"source":_df[entryId],"to":_s})
            _map.loc[:,"tb"]=entryTb
            _map.loc[:,"field"]=entryId
            self.data_map[entryTb]=_map
            _df.loc[:,entryId]=_s
            _df=_df.drop(columns=["source","to"])
            #替换主表主键映射
            _m2=self.data_map[headTb][["source","to"]]
            _df=_df.merge(_m2,how="left",left_on=headId,right_on="source") #不会存在合并列中出现N/A
            _df.loc[:,headId]=_df["to"]
            _df=_df.drop(columns=["source","to"])
            self.data_todo[entryTb]=_df
        else:
            _map=pd.DataFrame({"source":_data[entryId],"to":_data[entryId]})
            _map.loc[:,"tb"]=entryTb
            _map.loc[:,"field"]=entryId
            self.data_map[entryTb]=_map
            #替换主表主键映射
            _m2=self.data_map[headTb][["source","to"]]
            _df=_data.merge(_m2,how="left",left_on=headId,right_on="source") #不会存在合并列中出现N/A
            _df.loc[:,headId]=_df["to"]
            _df=_df.drop(columns=["source","to"])
            self.data_todo[entryTb]=_df


    def to_sql(self,toTb:str="qnwb_id_map"):
        """
        将数据写到目标表，并将映射数据写到目标数据源指定表
        """
        eng=fun.eng_t
        with eng.begin() as conn:
            for tb in self.data_todo.keys():
                print(f"开始写入表:{tb}...")
                self.data_todo[tb].to_sql(name=tb, con=conn, if_exists='append',index=False)
            for tb in self.data_map.keys():
                print(f"写入表键映射:{tb}...")
                self.data_map[tb].to_sql(name=toTb,con=conn, if_exists='append',index=False)


    def pHead_b(self,headTb:str,start_date:str,end_date="",fieldId:str="FID",fNo:str="FNUMBER"):
        """
        处理基础资料型单据头
        """
        head=fun.getBillHeaderFromSourceByCreateDate(headTb,start_date,end_date)
        if head.empty:
            print(f"表{headTb}在指定期间无数据...")
            return
        billNo=fun.getKeyBillNo(headTb,key=fieldId,field=fNo)
        head=head[~head[fNo].isin(billNo[fNo])]  #过滤掉目标表中已经存在的单据编号
        if head.empty:
            print(f"单据头表:{headTb}无需新增数据")
            return
        fid=head[head[fieldId].isin(billNo[fieldId])][fieldId] #找出冲突的主键FID
        if not fid.empty:   #有冲突主键时须记录映射并修改数据表
            _source=fid.sort_values().to_list()
            _m=pd.DataFrame({"source":_source,"to":[i for i in range(9000,len(_source)+9000)]})   #从9000开始对重复键做映射
            _df=head.merge(_m,how="left",left_on=fieldId,right_on="source") 
            _s=_df["to"].fillna(_df[fieldId]).astype('int32')  #填充非映射键
            _map=pd.DataFrame({"source":_df[fieldId],"to":_s})
            _map.loc[:,"tb"]=headTb
            _map.loc[:,"field"]=fieldId
            _df.loc[:,fieldId]= _s    
            _df=_df.drop(columns=["source","to"])
            self.data_todo[headTb]=_df
            self.data_map[headTb]=_map
        else:       #无冲突主键则直接添加到待处理
            self.data_todo[headTb]=head
            _map=pd.DataFrame({"source":head[fieldId],"to":head[fieldId]})
            _map.loc[:,"tb"]=headTb
            _map.loc[:,"field"]=fieldId
            self.data_map[headTb]=_map
        print(f"单据头表:{headTb}预处理完成")