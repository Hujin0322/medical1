select * from employees;
--list dict [{}] --> json���·� ����
--����Ŭ�� ���̽� ����
--��� �� ����Ŭdb�� ���� ����
--�ϳ��� ���, ����, �ߺ� ����, ������, ���ȼ� ���� --> DB�� �����ϴ� ����

--ȸ������ ���̺� ����
create table member(
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

--select, delete, insert, create  --> rollback ����, �������� �Ұ�

--������ �Է�
insert into member (id,pw,name,phone) values (
'aaa','1111','ȫ�浿','010-1111-1111'
);

insert into member values (
'bbb','1111','������','010-2222-2222'
);

insert into member(id,name,phone) values (
'ccc','�̼���','010-3333-3333'
);

--Į�� ���� �� Į�� ���� ���缭 �Է��ؾ� ��.
/*�÷� �� ���� ����
insert into member values (
'ddd','������','010-4444-4444'
);
*/

select id,pw,name,phone from member;
--����Ŭ���� null�� = ���Ѵ� ��

--commit ������ rollback �� ��� �ӽ�����ҿ� �ִ� ������ ������.
commit;

--�ӽ�����ҿ� �� �ִ� �����͸� rollback ����.
rollback;

select *from member;

insert into member values (
'ddd','1111','������','010-4444-4444'
);

select *from member;

--����
update member set pw='2222' where id='ccc';

rollback;

--��� ���̺� Ȯ��
select *from stu_score;

--���̺� Ÿ�� Ȯ��
desc member;

-- ����Ŭ Ÿ��
-- number-����, date-��¥, char-��������, varchar2-��������, clob-��뷮����

--number: ����, �Ǽ�
--number(4): -9999~9999

create table mem (
no number, --������ ���� ������
no2 number(4),
no3 number(4,2) --�Ҽ��� ǥ��/������ ������ �ν�
);

insert into mem (no) values ( 1234567890 );
insert into mem (no2) values (9999);
insert into mem (no2) values (1.11); --1�� �ν�, �Ҽ����� ������
insert into mem (no2) values (-9999);

insert into mem (no3) values (11.11);
insert into mem (no3) values (111); --����: 111.00���� �ν�

select * from mem;
commit;

create table mem2(
no number(4,2),
mdate date,
mdate2 timestamp --date: ��,��,��,��,��,�ʱ��� ���� ���� = timestamp �и��ʱ��� ���� ������.
);

insert into mem2(mdate) values ('2024-04-19');
insert into mem2(mdate) values (sysdate); --sysdate: ���� �ð�
insert into mem2(mdate2) values (sysdate);
insert into mem2 (mdate,mdate2) values (sysdate, sysdate+30);

select * from mem2;
select to_char(mdate,'yyyy/mm/dd hh:mi:ss') from mem2;
select to_char(mdate2,'yyyy/mm/dd hh:mi:ss:ff') from mem2;

--create, insert�� �ӽ� ����, select�� �����ֱ⸸ ����, commit���� �ؾ� ���� ����
select mdate,mdate+30 from mem2;

select * from employees;

select sysdate - hire_date from employees;

create table mem3 (
no number(4,3),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);

--char, varchar2
--char: ���� ����
insert into mem3 (tel) values ('11112222');
insert into mem3 (tel) values ('22223333');
insert into mem3 (tel) values ('111');
insert into mem3 (tel) values ('123456789');
insert into mem3 (tel) values ('ȫ');

--varchar2: ���� ����
insert into mem3 (name) values ('11112222');
insert into mem3 (name) values ('ȫ�浿'); --�ѱ�:: 3ũ��
insert into mem3 (name) values ('�Ż��Ӵ�'); --12 �ڸ� �ʿ�
INSERT INTO MEM3 (NAME) VALUES ('AAA');
insert into mem3 (name) values ('aaa');

commit;

-- select, from 2���� Ű����� ���� ��
-- * ��� �÷��� ���
-- sql����: ��ҹ��� ����X, �����ʹ� ��ҹ��� ����.
select * from mem3 where name = 'aaa';
select * from mem3 where name = 'AAA';
select name from mem3 where lower(name) = 'aaa';

select emp_name, department_id from employees;

--distinct: �ߺ� ����
select distinct department_id from employees;

select * from departments;

select department_id, department_name from departments;

select * from departments;
select * from employees;
select * from jobs;
select * from products;

select * from mem3;
select no, mdate2, tel, name, mdate from mem3;

select * from employees;
--Q. �����ȣ, ����̸�, �޿�, �Ի�����
select employee_id, emp_name, salary, hire_date from employees;

--desc: Ÿ�� Ȯ��
desc employees;

select * from stu_score;
drop table stu_score;

create table stu_score (
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values (
1,'ȫ�浿',100,100,100,300,100,1
);

insert into stu_score values (
5,'�豸',100,100,100,300,100,1
);

commit;

select * from stu_score;
