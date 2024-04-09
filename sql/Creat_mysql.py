import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='bank', charset='utf8')
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/bank')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 将数据存入数据库
# sql_insert = "insert into trans_details(trans_id,trans_date,trans_place,trans_type,DC_flg,trans_amt,balance) values (%d,%s,%s,%s,%s,%f,%f) % (1,'2019-06-25','aa','bb','1',18900.00,57.26)"
# for item in data:
#     sql_insert = f"insert into trans_details(trans_id,trans_date,trans_place,trans_type,DC_flg,trans_amt,balance) values({np.int(item[0])},{item[1]},{item[2]},{item[3]},{item[4]}, {np.float(item[5])},{np.float(item[6])})"

'''--------------交通银行--------------------'''
df_trans_detail_JT = pd.read_excel('./银行流水excel/交通银行/优化交通银行版式_00.xlsx', index_col=None, skiprows=1)
columns = ['trans_id', 'trans_date', 'trading_place', 'trans_type', 'DC_flg', 'trans_amt', 'balance']
df_trans_detail_JT.columns = columns
df_trans_detail_JT['trans_date'] = df_trans_detail_JT['trans_date'].apply(
    lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
pd_JT = pd.read_excel(
    './银行流水excel/交通银行/5-10-2-3-5 交通银行-6222600410005074298-20190101-20201117-侯中军-密码119515_1-61(1)_页面_01.xlsx',
    index_col=None)
pd_JT1 = pd.read_excel(
    './银行流水excel/交通银行/5-10-2-3-5 交通银行-6222600410005074298-20190101-20201117-侯中军-密码119515_1-61(1)_页面_02.xlsx',
    index_col=None)
columns = ["trans_id", "trans_date", "trans_time", 'trans_type', 'DC_flg', 'trans_amt', 'balance',
           'payment_receipt_account', 'payment_receipt_account_name', 'trading_place', 'accounting_fluid_numbe',
           'abstract']
pd_JT.columns = columns
pd_JT2 = pd.read_excel('./银行流水excel/交通银行/1.xlsx', index_col=None)
columns = ['trans_date', 'trading_place', 'trans_type', 'DC_flg', 'trans_amt', 'balance']
pd_JT2.columns = columns
df_trans_detail_JT = pd.concat([df_trans_detail_JT, pd_JT, pd_JT2])
df_trans_detail_JT['trans_id'] = range(1, len(df_trans_detail_JT) + 1)
df_trans_detail_JT['trans_date'] = pd.to_datetime(df_trans_detail_JT['trans_date'])
df_trans_detail_JT.reindex()

'''--------------光大银行--------------------'''
df_trans_detail_GD = pd.read_excel('./银行流水excel/光大银行/优化光大银行版式_00.xlsx', index_col=None)
df_trans_detail_GD.insert(3, "交易地点", '')

for i in range(1, 5):
    filename = f'./银行流水excel/光大银行/优化光大银行版式_0{str(i)}.xlsx'
    df_GD = pd.read_excel(filename, index_col=None)
    df_GD.insert(2, "交易流水号", '')
    df_GD.insert(7, '对方账号', '')
    df_GD.insert(8, '对方名称', '')
    df_GD.reindex(columns=df_trans_detail_GD.columns)
    # df_GD.rename(index={0 :"客户账号",5: "转出金额",9:"及要"})
    df_GD.rename(columns={"交易摘要": "摘要", "卡号": "客户账号", "支出金额": "转出金额"}, inplace=True)
    df_trans_detail_GD = pd.concat([df_trans_detail_GD, df_GD])

columns = ['customer_account', 'trans_date', 'accounting_fluid_numbe', 'trading_place', 'transfer_in_amt',
           'transfer_out_amt', 'balance', 'abstract', 'payment_receipt_account', 'payment_receipt_account_name']
df_trans_detail_GD.columns = columns
df_trans_detail_GD['trans_date'] = df_trans_detail_GD['trans_date'].apply(
    lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
df_trans_detail_GD['trans_date'] = pd.to_datetime(df_trans_detail_GD['trans_date'])
df_trans_detail_GD['customer_account'] = df_trans_detail_GD['customer_account'].fillna('')
df_trans_detail_GD.reindex()

'''--------------北京银行--------------------'''
df_trans_detail_BJ = pd.read_excel('./银行流水excel/北京银行/优化北京银行版式_00.xlsx', index_col=None)
for i in range(1, 5):
    filename = f'./银行流水excel/北京银行/优化北京银行版式_0{str(i)}.xlsx'
    df_BJ = pd.read_excel(filename, index_col=None)
    if i == 1:
        df_BJ.insert(6, "收支", '')
        df_BJ.reindex(columns=df_trans_detail_BJ.columns)
    df_trans_detail_BJ = pd.concat([df_trans_detail_BJ, df_BJ])

columns = ['trans_date', 'abstract', 'DC_flg', 'incurred_amt', 'balance', 'payment_receipt_account_name',
           'payment_receipt_account']
df_trans_detail_BJ.columns = columns
df_trans_detail_BJ['payment_receipt_account'] = df_trans_detail_BJ['payment_receipt_account'].fillna('')
df_trans_detail_BJ['trans_date'] = df_trans_detail_BJ['trans_date'].apply(
    lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
df_trans_detail_BJ['trans_date'] = pd.to_datetime(df_trans_detail_BJ['trans_date'])
df_trans_detail_BJ.reindex()

'''--------------建设银行--------------------'''
df_trans_detail_JS = pd.read_excel('./银行流水excel/建设银行/优化建设银行版式_00.xlsx', index_col=None)
df_trans_detail_JS[['payment_receipt_account', 'payment_receipt_account_name']] = df_trans_detail_JS[
                                                                                      '对方账号与户名'].str.partition(
    '/').iloc[:, 0::2]
df_trans_detail_JS.drop(columns=['对方账号与户名'], inplace=True)
# df_trans_detail_JS = pd.read_excel('./银行流水excel/建设银行/1.xlsx', index_col=None)
columns = ['trans_id', 'abstract', 'currencyid', 'remit', 'trans_date', 'trans_amt', 'balance', 'trading_place',
           'payment_receipt_account', 'payment_receipt_account_name']
df_trans_detail_JS.columns = columns
for i in range(1, 6):
    filename = f'./银行流水excel/建设银行/{str(i)}.xlsx'
    df_JS = pd.read_excel(filename, index_col=None, skiprows=1)
    columns = ['trans_date', 'voucher_type', 'voucher_code', 'abstract', 'payment_receipt_account_name',
               'borrower_incurred_amt', 'lender_incurred_amt', 'currency_type', 'borrower_or_load', 'balance',
               'accounting_fluid_numbe']
    df_JS.columns = columns
    df_trans_detail_JS = pd.concat([df_trans_detail_JS, df_JS])
df_JS1 = pd.read_excel(f'./银行流水excel/建设银行/img_0.xlsx', index_col=None, skiprows=2)
columns = ['trans_date', 'voucher_type', 'voucher_code', 'abstract', 'payment_receipt_account_name',
           'borrower_incurred_amt', 'lender_incurred_amt', 'borrower_or_load', 'balance', 'accounting_fluid_numbe']
df_JS1.columns = columns
df_trans_detail_JS = pd.concat([df_trans_detail_JS, df_JS1])
# df_trans_detail_JS.dropna(how='all',inplace=True)
df_trans_detail_JS['trans_id'] = range(1, len(df_trans_detail_JS) + 1)
df_trans_detail_JS['trans_date'] = df_trans_detail_JS['trans_date'].apply(
    lambda x: pd.to_datetime(str(int(x)), format='%Y-%m-%d'))
df_trans_detail_JS['trans_date'] = pd.to_datetime(df_trans_detail_JS['trans_date'])
df_trans_detail_JS.reindex()

'''--------------民生银行--------------------'''

df_trans_detail_MS = pd.read_excel('./银行流水excel/民生银行/民生-4017_01.xlsx', index_col=None)
df_trans_detail_MS['对方户名/账号'].fillna('', inplace=True)
df_trans_detail_MS[['payment_receipt_account', 'payment_receipt_account_name']] = df_trans_detail_MS[
                                                                                      '对方户名/账号'].str.partition(
    '/').iloc[:, 0::2]
df_trans_detail_MS.drop(columns=['对方户名/账号'], inplace=True)
columns = ['trans_date', 'abstract', 'voucher_type', 'voucher_code', 'borrower_incurred_amt', 'lender_incurred_amt',
           'balance', 'accounting_fluid_numbe', 'payment_receipt_account', 'payment_receipt_account_name',
           'payment_receipt_second_name']
df_trans_detail_MS.columns = columns
df_trans_detail_MS['trans_date'] = df_trans_detail_MS['trans_date'].apply(
    lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
df_MS = pd.read_excel('./银行流水excel/民生银行/1.xlsx', index_col=None)
columns = ['trans_date', 'voucher_type', 'voucher_code', 'abstract', 'payment_receipt_account_name',
           'borrower_incurred_amt', 'lender_incurred_amt', 'currency_type', 'borrower_or_load', 'balance',
           'accounting_fluid_numbe']
df_MS.columns = columns
df_MS['trans_date'] = df_trans_detail_MS['trans_date'].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
df_trans_detail_MS = pd.concat([df_trans_detail_MS, df_MS])
df_trans_detail_MS.reindex()

'''--------------合同--------------------'''
df_contract = pd.read_excel('./合同.xls', index_col=None)
columns = ['contract_id', 'partA_company_name', 'partB_company_name', 'product_name', 'total_amt', 'contract_date']
df_contract.columns = columns
'''--------------发票--------------------'''
df_receipt = pd.read_excel('./发票.xls', index_col=None)
columns = ['receipt_date', 'taxpayer_id', 'stock_name', 'saller_name', 'purchase_amt']
df_receipt.columns = columns
### 将数据存入数据库
# pd.io.sql.to_sql(df, 'example', con=engine, index=False, if_exists='replace')
df_trans_detail_JT.to_sql('trans_detail_jt', con=engine, if_exists='append', index=False)
df_trans_detail_GD.to_sql('trans_detail_gd', con=engine, if_exists='append', index=False)
df_trans_detail_BJ.to_sql('trans_detail_bj', con=engine, if_exists='append', index=False)
df_trans_detail_JS.to_sql('trans_detail_js', con=engine, if_exists='append', index=False)
df_trans_detail_MS.to_sql('trans_detail_ms', con=engine, if_exists='append', index=False)
df_contract.to_sql('contract', con=engine, if_exists='append', index=False)
df_receipt.to_sql('receipt', con=engine, if_exists='append', index=False)

print("Write to MySQL successfully!")
# 实现查询功能
pd_JT = pd.read_sql("trans_detail_jt", con=engine)
pd_GD = pd.read_sql("trans_detail_gd", con=engine)
pd_BJ = pd.read_sql("trans_detail_bj", con=engine)
pd_JS = pd.read_sql("trans_detail_js", con=engine)
pd_MS = pd.read_sql("trans_detail_ms", con=engine)

df_JT = pd_JT.query("DC_flg in ('收(Cr)','贷Cr')")
df_JT = df_JT.filter(["trans_date", 'trans_amt'])
df_JT.insert(0, column='trans_year', value=pd.DatetimeIndex(df_JT['trans_date']).year)
df_JT['trans_amt'] = df_JT['trans_amt'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df_JT['trans_amt'] = df_JT['trans_amt'].astype("float")
df_JT = df_JT.groupby(['trans_year']).agg({'trans_amt': np.sum})
df_JT = df_JT.reset_index()
print('----------交通银行----------')
print(df_JT)

df_GD = pd_GD.filter(["trans_date", 'transfer_in_amt'])
df_GD.insert(0, column='trans_year', value=pd.DatetimeIndex(df_GD['trans_date']).year)
df_GD['transfer_in_amt'] = df_GD['transfer_in_amt'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df_GD['transfer_in_amt'] = df_GD['transfer_in_amt'].astype("float")
df_GD = df_GD.groupby(['trans_year']).agg({'transfer_in_amt': np.sum})
df_GD = df_GD.reset_index()
print('----------光大银行----------')
print(df_GD)

df_BJ = pd_BJ.filter(["trans_date", 'incurred_amt'])
df_BJ.insert(0, column='trans_year', value=pd.DatetimeIndex(df_BJ['trans_date']).year)
df_BJ['incurred_amt'] = df_BJ['incurred_amt'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df_BJ['incurred_amt'] = df_BJ['incurred_amt'].astype("float")
df_BJ = df_BJ.groupby(['trans_year']).agg({'incurred_amt': np.sum})
df_BJ = df_BJ.reset_index()
print('----------北京银行----------')
print(df_BJ)

df_JS = pd_JS.filter(["trans_date", 'trans_amt'])
df_JS.insert(0, column='trans_year', value=pd.DatetimeIndex(df_JS['trans_date']).year)
df_JS['trans_amt'] = df_JS['trans_amt'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df_JS['trans_amt'] = df_JS['trans_amt'].astype("float")
df_JS = df_JS.groupby(['trans_year']).agg({'trans_amt': np.sum})
df_JS = df_JS.reset_index()
print('----------建设银行----------')
print(df_JS)

df_MS = pd_MS.filter(["trans_date", 'lender_incurred_amt'])
df_MS.insert(0, column='trans_year', value=pd.DatetimeIndex(df_MS['trans_date']).year)
df_MS['lender_incurred_amt'] = df_MS['lender_incurred_amt'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df_MS['lender_incurred_amt'] = df_MS['lender_incurred_amt'].astype("float")
df_MS = df_MS.groupby(['trans_year']).agg({'lender_incurred_amt': np.sum})
df_MS = df_MS.reset_index()
print('----------民生银行----------')
print(df_MS)
# 使用execute方法执行SQL语句
sql = ''
# cursor.execute(sql_insert)
# 使用 fetchone 方法获取一条数据
# data = cursor.fetchone()

# 输出查询结果
# print(data)
# 关闭数据源
db.close()
