CREATE TABLE bank.receipt (
	receipt_date DATE COMMENT '开票日期' ,
	taxpayer_id VARCHAR(50) NOT null COMMENT '纳税人识别号',
	stock_name VARCHAR(200) NOT null COMMENT '货物名称',
	saller_name VARCHAR(100) NOT null COMMENT '卖方名称',
	purchase_amt FLOAT NOT null COMMENT '购买金额'
)
COMMENT '发票信息'
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;
