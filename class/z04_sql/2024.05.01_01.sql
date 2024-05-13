-- drop table students;

select * from students
where name= '김구' ;

select * from students;

update students set id='aaa',name='홍길동', gender='M' 
where id='Nerte';

update students set id='bbb', name='유관순', gender='F'
where id='Faydra';

update students set id='ccc', name='이순신', gender ='M'
where id='Gregoor';

update students set id='ddd', name='강감찬', gender ='M'
where id='Brigida';

update students set id='eee', name='김구', gender ='M'
where id='Xylina' and name='Armin';

update students set id='fff', name='김유신', gender ='M'
where id='Ulric';

update students set id='ggg', name='홍길자', gender ='F'
where id='Basilius';

update students set id='hhh', name='홍길순', gender ='F'
where id='Jana';

-- rollback;

-- commit;

--rownum: 순차적 번호 생성
select rownum, a.* from students a
order by grade;

--1. select 구문 자체 실행
select a.* from students a;

--2. rownum 함수 실행
select rownum, a.* from students a;

--3. order by 실행
select rownum, a.*from students a
order by grade;

--1. select /2. order by / 3. rownum
select * from students 
order by grade;

-- rownum 붙이고 싶은 테이블은 (students를 grade로 정렬한 테이블)=a
select rownum, a.*from 
(select * from students 
order by grade)a;

select * from stu_score; 
-- (평균 85점 이상이면서 no가 500번보다 큰 수)a 테이블에 rownum 붙이기
select rownum, a.* from(
select * from stu_score
where avg>= 85 and no >= 500
order by no)a;

-- equi join: 같은 컬럼이 2개의 테이블에 존재하여 2개의 컬럼을 이용해 검색하는 방법
-- non-equi join: 같은 컬럼이 없으면서 2개의 테이블을 사용해 검색하는 방법
-- sum(amount) --> 가상 컬럼
select name, s_amount, rank from 
(select name, sum(amount)as s_amount from shop_product
where pdate >= '2024-03-01'
group by name
), customer_rank
where s_amount between lower_amount and high_amount;

select name, sum(amount)as s_amount from shop_product
where pdate >= '2024-03-01'
group by name;

select * from customer_rank;
select * from shop_product;

-- non equi join
select name, avg from stu_score;

select name, avg, grade from stu_score, stu_grade
where avg between low_score and high_score;

select * from stu_grade;

--shop_product, customer_rank --> non-equi join
select  * from customer_rank;

select rownum, a.* from students a
order by id;

select *from 
(select rownum rnum, a.* from 
(select * from students order by id)a)
where rnum >= 11 and rnum <= 20;

select * from (
select row_number() over (order by id)as rnum, a.* 
from students a)
where rnum >= 11 and rnum <= 20;

--self join
select a.employee_id, emp_name, department_id, a.manager_id, department_name
from employees a, departments b
where a.department_id = b.department_id and a.manager_id = b.manager_id
order by department_id;

-- cross join: 의미없는 연결
-- self join과 equi join 함께 사용
-- equi join: 2개의 테이블에 같은 컬럼을 가지고 검색
select a.employee_id, a.emp_name, a.department_id, department_name, a.manager_id, b.emp_name 
from employees a, employees b, departments c
where a.manager_id = b.employee_id and a.department_id = c.department_id
order by a.employee_id;

-- self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;

-- self join
-- Guy Himuro과 동일한 부서에 근무하는 사람을 출력하시오.
-- 컬럼: 사원명, 부서번호, 같이 근무하는 사원의 부서번호, 같이 근무하는 사원명
-- 1. john 부서 출력
select department_id from employees
where emp_name='Guy Himuro';

--2. 같은 부서번호인 사람.
-- 방법1
select * from employees;
select a.department_id, b.department_id, b.emp_name
from (select department_id from employees
where emp_name='Guy Himuro')a, employees b
where a.department_id = b.department_id;

--방법2
select e1.emp_name, e1.department_id, e2.emp_name
from employees e1,  employees e2
where e1.department_id = e2.department_id and e1.emp_name = 'Guy Himuro';

select * from member;

insert into member values(
member_seq.nextval, 'ggg', 1111, '홍길순', '여자', sysdate
);

commit;
rollback;
desc member;

select * from member;

update member set name='홍길동' where id = 'aaa';

select * from employees
where emp_name like '%홍%'
order by emp_name;

select b.employee_id, a.department_id, c.department_name, b.emp_name 
from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name like '%__%' 
and a.department_id = c.department_id;

select * from member order by id;

select * from member;

--테이블 생성
create table mem(
id varchar2(30) primary  key, 
pw number, 
name varchar(30), 
mdate date
);

-- drop table mem;

create table yeogi (
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number
);

select * from yeogi;