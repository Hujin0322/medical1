--drop table member;

-- ���Ἲ ��������: ������ �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check
-- ���̺� ����
create table member(
memNO number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate 
);

-- ������ �Է�, ���, ����, ����
insert into member (memno,id,pw,name,gender,mdate) values(
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);

insert into member (memno, id, pw, name, gender) values(
member_seq.nextval, 'bbb', '1111', '������', '����'
);

insert into member values (
member_seq.nextval, 'ccc', '1111', '�̼���', '����', sysdate
);

--���̺� ����: �Խ��� ���̺� ����
create table board (
bno number (4) primary key,
id varchar2 (30), -- �ܷ�Ű�� ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id) -- �ܷ�Ű(foreign key)�� ��Ī: fk_id
references member(id) -- member ���̺��� primary key: id 
);

select * from member;

-- primary key ���� --> foreign key�� ��ϵ� ������ �켱 ��� ����.
-- primary key ���� �� ��� ���� ���, ��� ���� ���
-- ��� ���� ���: on delete cascade/ ��� ���� ���: on update cascade

insert into board (bno, id, btitle, bcontent, bdate, bgroup,bstep, bindent, bhit, bfile) values (
board_seq.nextval, 'aaa', '�����Դϴ�.', '�����Դϴ�.', sysdate, board_seq.currval, 0,0,1,null
);

insert into board values(
board_seq.nextval, 'bbb', '�����Դϴ�2.', '�����Դϴ�2.', sysdate, board_seq.currval, 0,0,1,''
);

insert into board (bno, id, btitle, bcontent, bgroup) values (
board_seq.nextval, 'aaa', '�����Դϴ�3.', '�����Դϴ�3.', board_seq.currval
);

select * from board;

delete board where bno=3;

commit;

delete member where id='aaa'; -- foreign key�̹Ƿ� board���� ���� ���� �ʿ�.

-------------------------------------------------------------------------------

-- decode ���ǹ� 
select emp_name, department_id, 
decode (department_id, 
10,'�ѹ���ȹ��',
20, '������',
30, '����/�����',
40, '�λ��')
from employees
order by department_id;

select * from stu_score order by avg desc;
-- 90�� - a, 80��- b, 70�� - c
select name, avg, 
decode (avg,
90, 'A',
80, 'B',
70, 'C') as grade
from stu_score
order by avg desc;

select department_id, department_name from departments;

select job_id,salary from employees;

--sh_clerk: salary 15%�λ�, ad_asst: 10% �λ�, mk_rep: 5% �λ�
select job_id, salary, 
decode (job_id,
'SH_CLERK', salary+(salary*0.15),
'AD_ASST', salary+(salary*0.1),
'MK_REP', salary+(salary*0.05)) 
as salary_up from employees;

-- job_id �� clerk�� ���� job_id �˻�
-- like _ �ڸ���, % ��� ��
select job_id from employees
where job_id like '%CLERK%';

select name, avg from stu_score;

select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
else 'F'
end as grade 
from stu_score;

select department_id, department_name from departments;

select department_id from employees
order by department_id;

select department_id,
case 
when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then '����/�����'
when department_id = 40 then '�λ��'
when department_id = 50 then '��ۺ�'
when department_id = 60 then 'IT'
when department_id = 70 then 'ȫ����'
when department_id = 80 then '������'
when department_id = 90 then '��ȹ��'
when department_id = 100 then '�ڱݺ�'
when department_id = 110 then '�渮��'
when department_id = 120 then '�繫��'
when department_id = 130 then '������'
when department_id = 140 then '�ſ������'
when department_id = 150 then '�ֽİ�����'
when department_id = 160 then '���Ͱ�����'
when department_id = 170 then '������'
when department_id = 180 then '�Ǽ���'
when department_id = 190 then '�����'
when department_id = 200 then '���'
when department_id = 210 then 'IT ����'
when department_id = 220 then 'NOC'
when department_id = 230 then 'IT ��������ũ'
when department_id = 240 then '���� �ǸŻ����'
when department_id = 250 then '�Ǹ���'
when department_id = 260 then 'ä����'
when department_id = 270 then '�޿���'
end as department_name
from departments;

-- ���� ��� (job_id)
-- clerk ����: 15% �λ�,  ad_asst: 10% �λ�, mk_rep: 5% �λ�, man: 2% �λ�
select job_id, salary,
case 
when job_id like '%CLERK%' then salary+(salary*0.15)
when job_id = 'AD_ASST' then salary+(salary*0.1)
when job_id like '%REP%' then salary+(salary*0.05)
when job_id like '%MAN%' then salary+(salary*0.02)
else salary
end as new_salary
from employees
order by new_salary desc;

--  ���� ��� ���� --> 15% �λ�, ��� �̻� --> 5% �λ�
select avg(salary) from employees;

-- employees���̺��� �˻� - salary_updown�� ����.
select emp_name,salary,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
employees
)
order by salary_up asc;

-- salary_updown�÷��� ����.
select emp_name,salary,salary_updown,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
select emp_name,salary,
case
when salary >= 6461 then 'down'
when salary < 6461 then 'up'
end as salary_updown
from employees
order by salary asc
)
order by salary_up asc;
select emp_name,salary,
case
when salary >= 6461 then 'down'
when salary < 6461 then 'up'
end as salary_updown
from employees
order by salary asc;

select emp_name, salary,
case
when salary >= 6461 then 'down'
when salary < 6461 then 'up'
end as salary_down
from employees
order by salary desc;

--case 2�� ���
select emp_name, salary,
case
when salary >= (select avg(salary) from employees) then 'up'
when salary < (select avg(salary) from employees) then 'down'
end as salary_updown
,
case
when salary <= (select avg(salary) from employees) then salary+(salary*0.15)
when salary > (select avg(salary) from employees) then salary +(salary*0.05)
end as new_salary
from employees 
order by salary_updown;

--------------------------------------------------------------------------------

select * from stu_score;

select total, rank from stu_score
order by total desc;

-- rank () �Լ�
select total, rank from stu_score
order by total desc;

update stu_score set rank = 1
where total =291;

select total,rank, rank() over (order by total desc) as ranks from stu_score;
select no,rank() over (order by total desc) as ranks from stu_score;
select total,rank from stu_score
order by total desc;
update stu_score set rank = 1
where total=291;


-- 1000���� ������ ���� �Է�
update stu_score a
set rank = (
select ranks from(
select no, rank() over (order by total desc) as ranks from stu_score
)b
where a.no =b.no
);

select * from stu_score
order by rank asc;

--�÷� 2�� no, ranks
select no, rank() over (order by total desc) as ranks from stu_score;

commit;

select emp_name, department_id from employees;
select department_id, department_name from departments;

select emp_name,employees.department_id, department_name from employess, departments
where employees.department_id = departments.department_id;

-- �� ���̺� �����ؼ� ���
select a.department_id, department_name from employees a,departments b
where a.department_id = b.department_id;

-- �׷��Լ� sum, avg, count, max, min, stddev ǥ������, variance �л�

-- ������ ����
select sum(salary) from employees;

-- ���� ���� ���� stu_score
select sum(kor) from stu_score;

select count(*) from employees;

select count(*) from employees
where department_id = 50;

-- Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�.
select count(commission_pct) from employees;

select count(*) from employees
where commission_pct is not null;

-- Ŀ�̼��� �ִ� ��� �˻�
select emp_name, commission_pct from employees
where commission_pct is not null;

select e.employee_id from employees e;
select employees.employee_id from employees, departments;
-- group by �ڿ� ��Ī ���X

-- ��ü ��� ��
select count(*) from employees;

--department = 50
select count(*) from employees
where department_id = 40;

-- �μ����� �׷����� ����� ���
select department_id,count(department_id) from employees
group by department_id
order by department_id;

-- avg ���� grade
-- stu_score 90�� �̻� A, 80�� �̻� B, 70�� �̻� C, 60�� �̻� D, 60�� �̸� F
select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score; 

-- A ���� �� �� (group by�� ��Ī ���X --> grade ���X)
select grade, count(grade) from
( --�ϳ��� ���̺�� ����
select avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
)
group by grade
order by grade asc;

-- total ������ 91-99 --> 90, 81-89 --> 80
-- trunc(kor,-1)�� group by ���
select trunc(kor,-1)kor ,count(*) from stu_score
where trunc(kor,-1) =90
group by trunc(kor,-1); 

select k_kor, count(k_kor)k_count from
(select trunc(kor,-1) as k_kor from stu_score)
group by k_kor;

--�׷��Լ� group by ��� (*��Ī ���X)
select department_id, count(*) from employees
group by department_id
order by department_id;

select emp_name, count(emp_name) from employees
group by emp_name;

-- �μ��� ��� ���� ���Ͻÿ�.
select department_id, round(avg(salary),2)
from employees
group by department_id
order by department_id;

-- clerk, mep, man�� ���� ����� ���Ͻÿ�.

--���ڿ� �ڸ���: substr(job_id, 4)
select substr(job_id,4), count(substr(job_id,4)) from employees
where substr(job_id,4) = 'CLERK'
group by substr(job_id, 4);

select substr(job_id,4), count(substr(job_id,4)) from employees
where substr(job_id,4) = 'CLERK'
group by substr(job_id, 4);

-- �μ��� �ִ� ����, �ּ� ����, ��� ���� ���
select department_id, count(salary), sum(salary),max(salary), min(salary), round(avg(salary),2) 
from employees
group by department_id
order by department_id;

select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- �μ��� �����, Ŀ�̼��� �޴� ��� �� ���

-- 1. �μ��� ��� �� ���
select department_id, count(*) from employees
group by department_id;

-- 2. �μ��� Ŀ�̼� �޴� ��� �� ���
select department_id,count(department_id), count(commission_pct) from employees
group by department_id;

------------------------------------------------------------------------------

-- having ��: broup by�� ���� ������
-- where: �Ϲ� �÷��� ������
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select emp_name, department_id, round(avg(salary),2) from employees
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- emp_name �ι�° ���ڰ� a�� �����ϴ� �� ����
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- ��� ���޺��� ���� �׷츸 ���
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by avg(salary);

-- �μ��� �ִ� ������ 8000�̻��� �μ�, �ִ������ ����Ͻÿ�.
select department_id, max(salary) from employees
where department_id is not null
group by department_id
having max(salary) >= 8000
order by department_id;

--------------------------------------------------------------------------------

--join (RDBMS)
select emp_name, department_id, department_name, salary from employees;

select department_id, department_name from departments;

select count(*) from employees; --107��
select count(*) from departments; -- 27��

-- +����: ���̺� 2�� �ǹ̾��� ���Ḹ ����.
-- 107*27 = 2889
select *from employees, departments;

-- inner join: equi join- ���� Į�� ���� ����, non-equi join - ���� Į��X, �ٸ� ���� ��� ����.
-- outer join
-- self join

-- equi join: �� ���̺� �� ���� �÷� ��, �ش� ������ ���
-- 106��, null ���� �˻����� ����.
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id;

select department_id, department_name from departments;

select id, name from member;
select id, btitle, bcontent from board;

update member set name = 'ȫ����'
where id='aaa';

select * from member;

select bno,name,gender,btitle,bcontent, bdate, bgroup, bstep, bhit, bfile from board, member
where member.id = board.id;


