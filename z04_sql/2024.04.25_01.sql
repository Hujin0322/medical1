-- * ����, ����, ����
select sysdate-1, sysdate, sysdate+1 from dual;

-- * ����, �� ���� ù ��, �� ���� ���ڸ� ��
select sysdate, trunc(sysdate,'month'),last_day(sysdate) from dual;

--* �� ��¥ �� �� ��, �� ��¥ �� �� ��
select round(sysdate-hire_date,3), trunc(months_between(sysdate, hire_date),2) from employees;

-- trunc �� ���� ���� �� �����뺰 �ο��� Ȯ��.
select trunc(kor,-1)kor,count(kor) from stu_score
group by trunc(kor,-1)
order by kor;

--Q. hire_date���� ���� ����ϱ�.
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') hire_date, count(hire_date) from employees
group by to_char(hire_date,'mm')
order by hire_date;

--Q. hire_date 2008�⵵ ���, �⵵�� �ο��� ���
select to_char(hire_date,'yyyy')hire_date, count(hire_date) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

-- �� ��ȯ: number, character, date
-- number: ��Ģ����O, ��ǥ ǥ��X, ��ȭ ǥ��X
-- char: ��Ģ����X, ��ǥ ǥ��O, ��ȭ ǥ��O
-- date: ��¥�� (+,-) O, ��¥ ��� ���´� ���� �Ұ�.(--> to_char �� ���� �ʿ�)

--Q. ko+2024+0001
-- ������ ���·� �й� �ο� (stu_seq�� ������ 5���� �й� ���)
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,('0000'))) from dual;

--Q. (123,456,789)+(100,000) = 123556789 ���
select to_char(to_number('123,456,789','999,999,999') + to_number('100,000','999,999'),'999,999,999') from dual;

select to_char(salary,'999,999') from employees;

--���� Ÿ���� ��¥ Ÿ������ ����
select 20240425+3 from dual;
select to_char(20240425+3)+3 from dual;
select to_date(20240425+3)+3 from dual;

--���� Ÿ���� ��¥ Ÿ������ ����
select emp_name, hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

--Q. 8���� �Ի��� ��� �̸��� 2��°�� a�� �� �ִ� ��� ���.
select hire_date, emp_name from employees
where emp_name like '_a%' and to_char(hire_date,'yyyy-mm-dd') like '____-08-__';

--1. 1,5,8���� �Ի�
select hire_date from employees
where to_char(hire_date,'mm') = '01' or to_char(hire_date,'mm') = '05' or to_char(hire_date,'mm') = '08';

select hire_date from employees
where to_char (hire_date,'mm') in ('01','05','08');

--2. �̸� �ι�°�� a�� �� �ִ� ��� ���
select emp_name from employees
where emp_name like '_a%';

--3. �Ի���, �̸� ��ġ��
select emp_name, hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
order by hire_date;

--Q. 20070101 ���� �Ի� + ��� �̸� a�� �� �ִ� ��� ���
select emp_name, hire_date from employees
where hire_date > to_date(20070101) and emp_name like '%a%'
order by hire_date;

--���� Ÿ���� ��¥ Ÿ������ ����
select sysdate - to_date('20240401') from dual;

select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;  

select *from m_date;

create table eventDate (
eno number,
e_today date,
e_choice_day date,
e_preiod number
);

--�Է� �� ��¥ Ÿ�Կ� ����(���� - ��¥ ����)�� �Է��ص� �����.
--��¥ - ���� = �Ұ��� --> ���ڸ� ��¥ Ÿ������ �����ؾ� ��.
insert into eventDate values(
seq_mno.nextval, sysdate, '2024-04-01', sysdate - to_date('2024-04-01')
);

select *from eventdate;

-- ���� Ÿ���� ���� Ÿ������ ����
select to_number('20,000','99,999') - to_number('10,000','99,999') from dual;

-- null�� 0���� ġȯ nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo
select manager_id from employees
order by manager_id desc;

--���� Ÿ���� ���� Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;

-------------------------------------------------------------------------------

-- �׷� �Լ�: sum, avg, count(), count(*), min, max


-- �׷� �Լ� count
select count (*) from employees;
--�����: 107
select count(emp_name) from employees;
--null�� ���� �� ���� -106��
select count(manager_id) from employees;

select emp_name, manager_id from employees;

-- sum: �� ��
select sum(salary) from employees;

--avg: ���
select avg(salary) from employees;

--min: �ּҰ�, max: �ִ밪
select min(salary), max(salary) from employees;

--Q. ��պ��� ���� ���� ��� (��������)
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees);

--Q. �ּ� ������ �޴� ����� ����� �̸� ���
select employee_id, emp_name, salary from employees
where salary = (select min(salary) from employees);

--Q. �ִ� ���� �޴� ��� ���
select employee_id, emp_name, salary from employees
where salary = (select max(salary) from employees);

--�μ���ȣ�� 50���� ����� ��ü ����.
select department_id, salary from employees;

select sum(salary) from employees
where department_id = 100;

select count(*) from stu_score;

-- Q. kor ������ 80�� �̻��� �л� ���
select name,kor from stu_score
where kor>=80;

--Q. ���� ���� ��� �̻�, ���� ���� ��� �̻��� �л� ���
select name, kor, eng from stu_score
where kor>=(select avg(kor) from stu_score) and eng >= (select avg(eng) from stu_score);

create table s_info (
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval,2000
);

insert into s_info values(
stu_seq.nextval,( select count(*) from stu_score
where kor>=(select avg(kor) from stu_score) 
and eng>=(select avg(eng) from stu_score)   )
);

--Q. ���� ����,���� ����, ���� ���� �� �ְ����� �л� ���
select name,kor, eng, math from stu_score
where kor = (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score)
or math = (select max(math) from stu_score);

--Q. employees���� ���� �ִ�, �ּ�, ��� ��� ���
select emp_name, salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select avg(salary) from employees);

--�ִ밪
select emp_name, salary from employees
where salary = (select max(salary) from employees);

--Q. ��հ����� ���� ��� �� �ִ밪 ���
--1). 
select emp_name,salary from employees
where salary = 6400;

--2). 6400 ��� ��հ����� ���� ��� �� �ִ밪 ���

--2-1). ��պ��� ���� �� --> 56��
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc

--2-2). ��պ��� ���� 56�� �� �ִ밪 6400 ���
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc);

--3). ��ħ
select emp_name,salary from employees
where salary = (
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc)
);

--���� �Լ�
--lpad, rpad: ����� ä���
select emp_name, lpad(emp_name,15,'#') from employees;
select emp_name, rpad(emp_name,20,'@') from employees;

--ltrim, rtrim: ���� ���� �ڸ��� ���
select emp_name, ltrim(emp_name, 'Do') from employees;

-- ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

--substr(������, ����, ����): �����Ϳ��� �������� ������ŭ �߶���� 
select emp_name, substr(emp_name, 3,4) from employees;

select job_id from employees;

--Q. job_id�� �� �α��ڿ� �����ȣ�� �����ؼ� ����Ͻÿ�.
select substr(job_id,0,2)||employee_id from employees;

-- length : ���ڿ��� ����
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- ��¥�Լ� +,- ����, ��¥������ ���� ���ϱ�� �ȵ�.
-- ��¥������ +,- ���� ����
select sysdate+1 from dual;

-- ��¥������ - ��¥������ ����
select sysdate - hire_date from employees;

-- ��¥������ + ��¥������ �Ұ���
select sysdate + hire_date from employees;

select sysdate,trunc(sysdate,'month'),round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

-- ������ �߰�,���
select sysdate,add_months(sysdate,-2) from dual;

-- ceil�ø�, floor����, mod������, power����
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

-- ����. ����� �Ի��� ���
select emp_name||to_char(hire_date,' yyyy"��" mm"��" dd"��" day') from employees;


-- ����. �����, �ڸ��� 9�ڸ� ����� 0���� ǥ�� 
-- salar*1400 �տ� ��ȭǥ�ÿ� ��ǥ�� �־� ����Ͻÿ�.
select salary, to_char(salary*1400, 'L000,000,000' ) from employees;

-- �ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ��������¥
--- '2010-10-10'
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;

select * from member;

desc member;

-- DDL(data denfinition language)

-- �÷��߰�, ����, ���� 
-- �� commit,rollank�� �ȵ�. �ٷ� �����. 
alter table member add gender varchar2(6) default 'female' not null;
desc member;

-- �÷����� 
-- �÷��̸�����
alter table member rename column name to stu_name
;

-- Ÿ�Ժ���
alter table member modify(stu_name varchar2(50));

-- ������ �����Ͱ� �����Ϸ��� ũ�⺸�� �������� ����
update member set stu_name='';
alter table member modify(stu_name varchar2(6));
-- �÷��� Ÿ���� �����Ϸ��� �÷������Ͱ� ������̰ų� null�϶� ����
alter table member modify(stu_name number(4));
desc member;
select stu_name from member;


-- �÷����� - commit,rollback �� ����.
-- alter table member drop column phone;


select * from member;

update member set gender = 'male';

commit;