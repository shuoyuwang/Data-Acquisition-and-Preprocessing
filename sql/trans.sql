

CREATE TABLE bank.trans_details (
	trans_id INT UNSIGNED auto_increment COMMENT '序号' ,
	trans_date DATE NOT null COMMENT '交易日期',
	trans_place VARCHAR(500) NOT null COMMENT '交易地点',
	trans_type VARCHAR(50) NOT null COMMENT '交易方式',
	DC_flg VARCHAR(50) NOT null COMMENT '收支标志',
	trans_amt FLOAT NOT null COMMENT '交易金额',
	balance FLOAT NOT null COMMENT '余额',
	PRIMARY KEY ( `trans_id` )
)
COMMENT '银行交易流水信息'
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

