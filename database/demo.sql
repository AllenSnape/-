create table users(
	id int primary key,
	username varchar(18) not null,
	password varchar(20) not null,
	sex char(1) not null,
	name varchar(18) not null,
	email varchar(25) not null,
	phone varchar(15) not null,
	authority varchar(20) not null,
	borndate date,
	safety_id int,
	mystatement char(1) not null default 'y'
);

create table good(
	id int primary key,
	name varchar(50) not null,
	type_id int not null,
	price double(10,2) not null,
	amount double(10,2) not null,
	unit varchar(10) not null, 
	supplier_id int not null, 
	barcode varchar(20) not null,
	photopath varchar(100),
	goodinfo_id int not null,
	mystatement char(1) not null default 'y'
);

create table goodinfo(
	id int primary key,
	borndate date not null,
	bornaddress varchar(100) not null,
	keeptime int not null,
	ingredient varchar(255) not null,
	qs varchar(20) not null,
	gb varchar(20) not null,
	notes varchar(255),
	sale double not null default 0,
	liked int not null default 0
);

create table mytype(
	id int primary key,
	name varchar(20) not null,
	mystatement char(1) not null default 'y'
);

create table supplier(
	id int primary key,
	name varchar(30),
	owner varchar(18),
	phone varchar(15) not null,
	backup_phone varchar(15),
	email varchar(25),
	qq varchar(15),
	address varchar(200) not null,
	notes varchar(255),
	mystatement char(1) not null default 'y'
);

create table safety(
	id int primary key,
	cardnum varchar(50),
	cardname varchar(50),
	alipaynum varchar(50),
	alipayname varchar(18),
	mystatement char(1) not null default 'y'
);

create table shoppingcar(
	id int primary key,
	user_id int not null,
	good_id int not null,
	amount double not null,
	mystatement char(1) not null default 'y'
);

--add constraints for tables
alter table good add constraint FK_type_ID foreign key(type_id) references mytype(id);
alter table good add constraint FK_supplier_ID foreign key(supplier_id) references supplier(id);
alter table users add constraint FK_safety_ID foreign key(safety_id) references safety(id);
alter table good add constraint FK_goodinfo_ID foreign key(goodinfo_ID) references goodinfo(id);
alter table shoppingcar add constraint FK_user_id foreign key(user_id) references users(id);
alter table shoppingcar add constraint FK_good_id foreign key(good_id) references good(id);

--insert infos
insert into safety(id) values(1000);
insert into users values(1000,'xiaoming','xiaoming','m','小明','123@qq.com','110','admin','1997-10-25',1000,default);\g

insert into mytype values(1000,'allen',default);
insert into supplier values(1000,null,null,'110',null,null,null,'China',null,default);
insert into good values(1000,'allen',1000,100,100,'个',1000,'1997-01-01','China Sichuan DaZhou',0,'513001199801010859','C','00-000','00-000','','',default);





--remove constraints of tables
alter table good drop foreign key FK_ID;\g

--delete column
alter table good drop column borndate;

--add column
alter table good add column borndate date not null;

--change name of column
alter table good change borndata borndate date not null;

--modify the column
alter table good modify borndate varchar(20) not null;

--solve the mess code
--1. In mysql system , input "set names utf8;"
--2. While creating database ,input like "create database xx CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';"
--3. THis point is the most inportant one, 
	--first get the root-authority of Ubuntu,input "su root", then input password of root
	--input "gedit /etc/mysql/my.cnf"
	--add info :
		below version_5.5 of mysql
			"[client]" append "default-character-set=utf8"
			"[mysqld]" append "default-character-set=utf8" , if this one is putting errors ,
				then only "[mysqld]" append "default-character-server=utf8"
		above version_5.5 or in version_5.5 of mysql
			"[client]" append "default-character-set=utf8"
			"[mysqld]" append "default-storage-engine=INNODB"
			"[mysqld]" append "character-set-server=utf8"
			"[mysqld]" append "collation-server=utf8_general_ci"





