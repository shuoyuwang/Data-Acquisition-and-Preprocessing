CREATE TABLE bank.bank_trade_details (
	trade_id INT UNSIGNED auto_increment COMMENT '序号' ,
	trade_date DATE NOT null COMMENT '交易日期',
	trade_addr VARCHAR(500) NOT null COMMENT '交易地点',
	trade_way VARCHAR(50) NOT null COMMENT '交易方式',
	payments_sign VARCHAR(50) NOT null COMMENT '收支标志',
	trade_amt FLOAT NOT null COMMENT '交易金额',
	remain_amt FLOAT NOT null COMMENT '余额',
	PRIMARY KEY ( `trade_id` )
)
COMMENT '银行交易流水信息'
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

