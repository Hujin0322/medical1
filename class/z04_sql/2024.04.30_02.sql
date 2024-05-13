select * from stu_score
where avg>=90;

-- equi join
-- 사원 번호, 사원명, 부서번호, 부서명 출력/ 이름 두번째 자리에 a/ 월급이 평균 이상인 사람
select employee_id, emp_name, a.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id 
and emp_name like '_a%' 
and salary >= (select avg(salary) from employees);

-- 그리고, 이름 두번째 자리에 a가 들어가는 사원 검색
select emp_name from employees
where emp_name like '_a%';

-- 월급이 평균 이상인 사람만 검색
select salary from employees
where salary >= (select avg(salary) from employees);

select * from employees;  
select * from jobs;

--사원번호, 사원명, 부서번호, 부서명, 직급번호, 직급명 출력
select employee_id, emp_name, e.department_id, department_name, e.job_id, job_title
from employees e, jobs j, departments d
where e.department_id = d.department_id and e.job_id = j.job_id; 

--  사원번호, 사원명, 월급, 최소 월급분(min_salary), 인상분, 직급, 직급타이틀 출력
select employee_id, emp_name, salary, min_salary, round((((salary-min_salary)/salary)*100),2)||'%' , a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id;

-- job_title Manager 글자가 들어가 있는 사원의 
-- 사원번호, 사원명, 직급번호, 직급명, 월급, 최대 월급을 출력하시오.

select employee_id, emp_name, a.job_id, job_title, salary, max_salary 
from employees a, jobs b
where a.job_id = b. job_id and job_title like '%Manager%';

select b.user_id,user_name, user_phone, user_address1,user_address2,user_address3
from deliver_address a , user b
where a.user_id = a.user_id;

create table stu_grade(
greade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A', 90,100
);
insert into stu_grade values(
'B', 80,89
);
insert into stu_grade values(
'C', 70,79
);
insert into stu_grade values(
'D', 60,69
);
insert into stu_grade values(
'F', 0,59
);

commit;

select * from stu_grade;

select avg from stu_score;

--case when then grade 컬럼을 만들어 90점 이상 A, 80점 이상B,,,,학점 출력
select no,name,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

-- non equi join
select no,name, avg, grade 
from stu_score, stu_grade
where avg between low_score and high_score
order by no;

-- stu_score, stu_grade 같은 컬럼이 없음.
-- 2개 테이블 join: non-equi join
select * from stu_score;
select * from stu_grade;

update stu_grade set high_score=62
where grade = 'F';

commit;

-- 월별 매출액을 기준으로 고객 등급
-- 지역별 대출 합계 출력
select * from kor_loan_status;
select region, gubun, sum(loan_jan_amt) 
from kor_loan_status
group by region, gubun 
order by region;

--연도별, 지역별 대출합계금액 그룹
select * from kor_loan_status;
select substr((period),1,4)preiod, region, sum(loan_jan_amt)loan_jan_amt 
from kor_loan_status
group by  substr((period),1,4), region
order by  region;

--부서별 월급 합계를 출력하시오.
select department_id, sum(salary) a
from employees
group by department_id
order by a;

-- 시간대별, 연령대별 판매량 총합을 출력하시오
select * from lotte_product;
select time_cd, age_cd, sum(purh_amt) purh_amt
from lotte_product
group by time_cd, age_cd
order by purh_amt desc;

-- 24/03/01 이후 이름별 금액합계 출력
select name, sum(amount) 
from shop_product
where pdate >= '2024/03/01'
group by name
order by sum(amount);

-- customer_rank 테이블 생성
-- rank: 100만원 미만 = BRONZE, 200만원 미만 = SILVER, 300만원 미만 = GOLD, 300만원 이상 = PLATINIUM
-- name, 3월 이후 sum(amount), rank 출력
-- non equi join으로 출력

create table customer_rank(
rank varchar2(30),
lower_amount number(30),
high_amount number(30));

select * from customer_rank;

insert into customer_rank values(
'PLATINIUM', 300,0
);

--rank는 가상함수 group by에서 가상함수는 불가
select name, s_amount, rank
from 
(select name, sum(amount)s_amount 
from shop_product
where pdate >= '2024/03/01'
group by name), customer_rank
where s_amount between low_amount and high_amount;

-- non-equi join
select no,name,avg,grade from stu_score,stu_grade
where avg between low_score and high_score
order by no;

-- 컬럼명 변경
ALTER TABLE customer_rank RENAME COLUMN low_amount TO lower_amount;

select * from lotte_product
order by std_ym
;
-----------------------------------------------------------------------수정 필요--
-- 순번을 새롭게 부여한 후, 출력 함수
--rownum, row_number(): 검색된 형태에서 번호 붙이기
select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from lotte_product;

select rownum rnum,a.* from lotte_product a;


select rnum,std_ym,sex_cd,age_cd,time_cd,purh_amt 
from 
(select rownum rnum,a.* from lotte_product a) b
where rnum >= 21 and rnum <= 30 ;

select rownum,a.*
from lotte_product a
order by std_ym
;

select rownum,b.*
from ( select * from lotte_product order by std_ym ) b
;

select * from stu_score
order by no;

-- kor 점수가 높은 순으로 21-30까지 출력
-- 순번 21,22,23 ////// 30번 부여
select rnum, no, name, kor, eng, math, total, avg, rank, c_date
from (
select rownum rnum, b.* from 
(select a.* from stu_score a order by kor desc)b)
where rnum >=21 and rnum <=30;

select * from stu_score;

select * from stu_score
where no >= 11 and no <= 20
order by no;

