CREATE TABLE bank.contract (
	contract_id INT UNSIGNED auto_increment COMMENT '合同编号' ,
	partA_company_name VARCHAR(100) NOT null COMMENT '甲方',
	partB_company_name VARCHAR(100) NOT null COMMENT '乙方',
	product_name VARCHAR(100) NOT null COMMENT '商品名	',
	total_amt FLOAT NOT null COMMENT '总金额',
	contract_date DATE NOT null COMMENT '签订日期',

	PRIMARY KEY ( `contract_id` )

)
COMMENT '合同信息'
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;
