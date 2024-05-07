-- 2개의 테이블: department_id
select * from employees;
select * from departments;

select employee_id, emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id;

-- 홍길동 학생의 학생성적의 모든 내용과 전화번호, 이메일, 과, 학년
-- name으로 연결
select no, name, kor, eng, math, total, avg, rank, c_date from stu_score
where name = '홍길동';

select id, name, phone, email, major, grade from students 
where name = '홍길동';

select no, id, a.name, phone, email, major, grade, kor, eng, math, total, avg, rank, c_date 
from stu_score a, students b
where a.name = '홍길동' and a.name=b.name;

select * from stu_score order by no;
desc stu_Score;
select count(*) from stu_score;
select count(*) from students;
select * from students;

alter table students  add no number(30);
insert into students(no) select no from stu_score;

select rnum from 
(select rownum rnum, a.* from students a);

--rownum 만들어서 번호를 no에 넣기 
update students b set no = (
(select rownum rnum from students)a)
where a.id = b.id;

-- 에러
update students b 
set (b.no) = (select rownum, id from students)a
where a.id = b.id;

--drop table students;

-- equi join
-- 2개 테이블 join --> 1개의 동일한 컬럼 있어야 함.
-- 동일 컬럼은 중복이 없어야 함. 2개 중 하나의 컬럼은 primary key로 존재해야 함.
select a.id, a.name, phone, total, avg from students a, stu_score b
where a. id = b. id;

-- self join
-- 동일한 테이블 2개를 가지고 서로 join
select a.employee_id, a.emp_name, a.department_id, a.job_id, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id
order by department_id;

desc stu_score;

desc students;

-- drop table students;

select * from students;
select * from stu_score
order by rank;

update stu_score a
set rank = (select ranks from (
select no,id, rank() over (order by total desc)as ranks, rank, total 
from stu_score) b
where a.no = b.no);

-- rank
select ranks from (
select no,id, rank() over (order by total desc)as ranks, rank, total from stu_score) b ;

select * from students;

select * from member
order by no;

alter table member add no number;

--member 테이블의 no에 rnum 추가
--1. rank,id
select rank, id from member;

--2. rnum 가져오기
select rnum from (select rownum rnum,id from member);

--3. 조건
select rnum from (select rownum rnum,id from member) b
where a. id = b. id;

--4. member 테이블에 rnum 추가
update member a 
set no = (select rnum from 
(select rownum rnum , id from member)b
where a.id = b.id);

update stu_score set rank = 0;

commit;

select total,rank from stu_score
order by total desc;

-- over+(order by)
select total, rank() over (order by total desc) ranks from stu_score;
select row_number() over (order by total desc) rnum,total from stu_score;

-- stu_score에 rank 순위를 업데이트하시오.
update stu_score a set rank = (
select ranks from (select no, rank() over (order by total desc) ranks from stu_score) b 
where a. no = b. no);

--row_number() over()

select * from stu_score;

-- 방법1.
select * from
(
select rownum rnum, a.* from 
(select * from stu_score order by total desc)a)
where rnum >= 11 and rnum <= 20;

-- 방법2.
select * from (
select row_number() over(order by total desc) rnum,a.* from stu_score a)
where rnum >= 11 and rnum <= 20;

--outer join-------------------------------------------------------------------
select employee_id, emp_name, manager_id from employees
order by employee_id;

select * from employees;

--self join manager_id, 이름 가져오기
-- 값 미충족 시에도 출력되도록 outer join 이용
-- null 값이 있는 반대편 항목에 (+)기호를 넣으면 됨.
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id(+);

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz';

-- equi join, |outer join --> null값도 출력 원할 때| 
-- employees 테이블 부서번호 = 10~110
-- departments 테이블 부서 번호 = 10~270
select emp_name, b.department_id, department_name 
from employees a, departments b
where a.department_id(+) = b.department_id
order by department_id;

select department_id from departments;


select * from employees cross join departments;
select * from employees, departments;

select a.department_id, department_name
from employees a, departments b
where a.department_id = b. department_id;

select a.department_id, department_name
from employees a inner join departments b
on a.department_id = b.department_id;

-- ANSI inner join - using 이용 
select employee_id, emp_name, department_id, department_name
from employees join departments 
using (department_id);

--natural join
select a.*, department_name
from employees a, departments b 
where a.departnemt = b.;

select * from employess natural join departmentsb;

--ansi outer join: left outer join, right outer join, full outer join
select a.emp_name, a.manager_id, b.emp_name from employees a
full outer join employees b
on a.manager_id = b. employee_id;

-- 기본 sql left outer join, right outer join, full outer join 붙가
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id(+) = b.employee_id;

select count(*) from stu_score 
where id like '%a%'
order by no;

--row_number() over()
select * from (
select row_number() over (order by no) rnum, a.* from stu_score a
where id like '%a%') where rnum >= 1 and rnum <= 10;

-- 테이블명: melon, 순번: melon_seq, 순위: rnak, 변동 순위: v_rank, 이미지: img, 
-- 제목:title, 가수:singer, 좋아요 수: likeNum(,X)
create table melon(
mno number primary key,
rank number,
v_rank number,
img varchar2(130),
title varchar2(100),
singer varchar2(100),
likeNum number
);

--drop table melon;

select * from melon;

create table yanolja(
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number);

alter table yanolja modify img varchar2(300);