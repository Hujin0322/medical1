select * from students;

select * from students
order by name asc;

--drop table students;

--���̺� �÷� �߰�
alter table students add rank number(3);

select * from students;

update students set rank=0;

commit;

select *from students;

select rank() over(order by total desc) rank 
from students;

update students set total=0;

select total, rank from students;

update students set total = (kor+eng+math);

update students a set rank = (select ranks 
from (select no, rank() over (order by total desc) ranks
from students) b where a.no = b.no);

select total, rank from students
order by asc;

--1. update ����
update students a set rank = (rank);

--2.no, rank() ����
(select no, rank() over (order by total desc) ranks from students) b;

--3. update������ rank()������ no �÷����� ��, rank�÷� �˻�
update students a set rank = (
select ranks from (students) b
where a.no = b.no
);

--4. students ���̺��� ranks�� �� �ִ� ���̺��� �־���.
update students a set rank = (
select ranks from (select no, rank() over (order by total desc) ranks from students) b
where a.no=b.no
);

--��������
select no, total, rank from students
order by total desc;

--��������
select no, total, rank from students
order by no asc;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

select max(hire_date)- min(hire_date) from employees
order by hire_date;

select max(kor) - min (kor) from students;
select max(kor),max(eng),max(math) from students;

--Q. �Ի��Ϸ� ��������
select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date desc;

--Q. �޿� ���� �޴� ����� ���, ������ ��������� ��������
select employee_id, emp_name, job_id, hire_date, salary from employees
order by salary, emp_name desc;

select * from employees;

--�����Լ�
--abs
select -10, abs(-10) from dual;

--floor: ����, �ڸ��� ���� �Ұ�
select 34.789, floor(34.789) as f, round(34.789) as r from dual;

--round(���, �ڸ���) ex) round (34.178,2) 2�ڸ����� ǥ��
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
select round(avg, 2) avg from students;

select 34.5678, round (34.5678,-1) from dual;

--trunc: ������ �ڸ��� ���� ����. 
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;

--ceil: �ø�, �ڸ��� ���� �Ұ�
select ceil(34.123) from dual;

--Q. ���� ���� �ϴ��� �����ؼ� ���
select trunc(kor,-1) kor from students
order by kor;

--Q. ����, ����, ���� ������ �ϴ��� �����ؼ� ���� ����Ͻÿ�.
select trunc(kor,-1) kor, trunc(eng,-1) eng, trunc(math,-1) math, 
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) total 
from students;

--mod ������
select round(100/7,2) from dual;
select mod(10,7) from dual;

--������
select 10/7 from dual;

--Q. �����ȣ�� ¦���� ���� ����Ͻÿ�.
select employee_id from employees
where mod(employee_id,2)=0;

--��
select floor(10/7) from dual;
--������
select mod(10,7) from dual;

--Q. �й��� 3�� ����� �л��� ���
select no,name from students
where mod(no,3)=0;

-------------------------------------------------------------------------------

--������
create sequence seq_no
increment by 1  -- 1�� ����
start with 1    -- 1���� ����
minvalue 1      -- �ּҰ� 1
maxvalue 9999   -- �ִ밪 9999
nocycle         -- ��ȯX
nocache         -- ĳ�� ���X
;
-- nextval: ������ ��ȣ 1�� ����
select seq_no.nextval from dual;

-- currval: ������ ��ȣ Ȯ��
select seq_no.currval from dual;

--drop table member;

--drop table mem3;

create table member (
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno 
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle 
nocache
;

select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval,'eee','1111','�豸','010-5555-5555'
);

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

-- '0000' �ڸ���
select 's'||to_char(seq_mno.nextval,'0000') from dual;

--Q. �ѱ����б� ko20240001
-- ������ seq_kono 1 - 9999
create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- trim(): ��������
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'0000'))as stuno from dual;

-- �Խ���
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

--Q. ������ seq_deptno ���� 1001, ���� 10, �ּҰ� 1, �ִ밪 99999, 5�� ����
create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
cycle
nocache;

select seq_deptno.nextval from dual;
select seq_deptno.currval from dual;

create table emp01(
empno number(4) primary key,
ename varchar(30),
hire_date date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

alter sequence emp_seq
increment by 1001;

insert into emp01 values(
emp_seq.nextval, '�̼���', sysdate
);

select *from emp01;

commit;

--Q. ������� �Ի��� �ϼ��� �Բ� ��� (�ø�)
select employee_id, emp_name, job_id, hire_date, ceil(sysdate - hire_date)||'��' 
from employees
order by hire_date desc;

--Q. �����ȣ, �����, ����, �Ի��� ������������ ����
select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

select emp_name from employees;

--Q. ���ް� ����� ���ļ� ���
select job_id||employee_id from employees;

--substr: ���ڿ� �ڸ��� �Լ�, substr(���, ���� ��ġ, ����)
select substr(job_id,0,2) from employees;
select emp_name, substr(emp_name,1,3) from employees;
select substr('abcde',2,3) from dual;

--Q. job_id �� 2�� ���ڿ� ��� 5�ڸ� ex) SH00198
select substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

-- ��¥ �Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;

-- �� ��¥ ������ ������ Ȯ��
select MONTHS_BETWEEN(SYSDATE,hire_date) ����, sysdate - hire_date �� from employees;

-- ���� �� �߰�
select sysdate, add_months(sysdate,2) from dual;

-- �Է��� �������� ���� ���� �˷���.
select next_day(sysdate,'������') from dual;

-- �Է��� �������� ���� ������ ���� �˷���.
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;