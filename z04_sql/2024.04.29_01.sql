--drop table member;

-- 무결성 제약조건: 부적합 자료가 입력되지 않도록 하기 위한 규칙
-- not null, unique, primary key, foreign key, check
-- 테이블 생성
create table member(
memNO number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate 
);

-- 데이터 입력, 출력, 수정, 삭제
insert into member (memno,id,pw,name,gender,mdate) values(
member_seq.nextval,'aaa','1111','홍길동','남자',sysdate
);

insert into member (memno, id, pw, name, gender) values(
member_seq.nextval, 'bbb', '1111', '유관순', '여자'
);

insert into member values (
member_seq.nextval, 'ccc', '1111', '이순신', '남자', sysdate
);

--테이블 생성: 게시판 테이블 구조
create table board (
bno number (4) primary key,
id varchar2 (30), -- 외래키로 등록
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id) -- 외래키(foreign key)의 별칭: fk_id
references member(id) -- member 테이블의 primary key: id 
);

select * from member;

-- primary key 삭제 --> foreign key에 등록된 데이터 우선 모두 삭제.
-- primary key 삭제 시 모두 삭제 방법, 모두 보존 방법
-- 모두 삭제 방법: on delete cascade/ 모두 보존 방법: on update cascade

insert into board (bno, id, btitle, bcontent, bdate, bgroup,bstep, bindent, bhit, bfile) values (
board_seq.nextval, 'aaa', '제목입니다.', '내용입니다.', sysdate, board_seq.currval, 0,0,1,null
);

insert into board values(
board_seq.nextval, 'bbb', '제목입니다2.', '내용입니다2.', sysdate, board_seq.currval, 0,0,1,''
);

insert into board (bno, id, btitle, bcontent, bgroup) values (
board_seq.nextval, 'aaa', '제목입니다3.', '내용입니다3.', board_seq.currval
);

select * from board;

delete board where bno=3;

commit;

delete member where id='aaa'; -- foreign key이므로 board에서 먼저 삭제 필요.

-------------------------------------------------------------------------------

-- decode 조건문 
select emp_name, department_id, 
decode (department_id, 
10,'총무기획부',
20, '마케팅',
30, '구매/생산부',
40, '인사부')
from employees
order by department_id;

select * from stu_score order by avg desc;
-- 90점 - a, 80점- b, 70점 - c
select name, avg, 
decode (avg,
90, 'A',
80, 'B',
70, 'C') as grade
from stu_score
order by avg desc;

select department_id, department_name from departments;

select job_id,salary from employees;

--sh_clerk: salary 15%인상, ad_asst: 10% 인상, mk_rep: 5% 인상
select job_id, salary, 
decode (job_id,
'SH_CLERK', salary+(salary*0.15),
'AD_ASST', salary+(salary*0.1),
'MK_REP', salary+(salary*0.05)) 
as salary_up from employees;

-- job_id 중 clerk이 들어가는 job_id 검색
-- like _ 자릿수, % 모든 것
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
when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then '구매/생산부'
when department_id = 40 then '인사부'
when department_id = 50 then '배송부'
when department_id = 60 then 'IT'
when department_id = 70 then '홍보부'
when department_id = 80 then '영업부'
when department_id = 90 then '기획부'
when department_id = 100 then '자금부'
when department_id = 110 then '경리부'
when department_id = 120 then '재무팀'
when department_id = 130 then '세무팀'
when department_id = 140 then '신용관리팀'
when department_id = 150 then '주식관리팀'
when department_id = 160 then '수익관리팀'
when department_id = 170 then '생산팀'
when department_id = 180 then '건설팀'
when department_id = 190 then '계약팀'
when department_id = 200 then '운영팀'
when department_id = 210 then 'IT 지원'
when department_id = 220 then 'NOC'
when department_id = 230 then 'IT 헬프데스크'
when department_id = 240 then '공공 판매사업팀'
when department_id = 250 then '판매팀'
when department_id = 260 then '채용팀'
when department_id = 270 then '급여팀'
end as department_name
from departments;

-- 월급 출력 (job_id)
-- clerk 포함: 15% 인상,  ad_asst: 10% 인상, mk_rep: 5% 인상, man: 2% 인상
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

--  월급 평균 이하 --> 15% 인상, 평균 이상 --> 5% 인상
select avg(salary) from employees;

-- employees테이블에서 검색 - salary_updown이 없음.
select emp_name,salary,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
employees
)
order by salary_up asc;

-- salary_updown컬럼이 있음.
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

--case 2개 사용
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

-- rank () 함수
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


-- 1000명의 순위를 각각 입력
update stu_score a
set rank = (
select ranks from(
select no, rank() over (order by total desc) as ranks from stu_score
)b
where a.no =b.no
);

select * from stu_score
order by rank asc;

--컬럼 2개 no, ranks
select no, rank() over (order by total desc) as ranks from stu_score;

commit;

select emp_name, department_id from employees;
select department_id, department_name from departments;

select emp_name,employees.department_id, department_name from employess, departments
where employees.department_id = departments.department_id;

-- 두 테이블 조인해서 출력
select a.department_id, department_name from employees a,departments b
where a.department_id = b.department_id;

-- 그룹함수 sum, avg, count, max, min, stddev 표준편차, variance 분산

-- 월급의 총합
select sum(salary) from employees;

-- 국어 점수 종합 stu_score
select sum(kor) from stu_score;

select count(*) from employees;

select count(*) from employees
where department_id = 50;

-- 커미션을 받는 사원의 수를 구하시오.
select count(commission_pct) from employees;

select count(*) from employees
where commission_pct is not null;

-- 커미션이 있는 사원 검색
select emp_name, commission_pct from employees
where commission_pct is not null;

select e.employee_id from employees e;
select employees.employee_id from employees, departments;
-- group by 뒤엔 별칭 사용X

-- 전체 사원 수
select count(*) from employees;

--department = 50
select count(*) from employees
where department_id = 40;

-- 부서별로 그룹지어 사원수 출력
select department_id,count(department_id) from employees
group by department_id
order by department_id;

-- avg 기준 grade
-- stu_score 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60점 미만 F
select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score; 

-- A 학점 몇 명 (group by는 별칭 사용X --> grade 사용X)
select grade, count(grade) from
( --하나의 테이블로 생각
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

-- total 점수를 91-99 --> 90, 81-89 --> 80
-- trunc(kor,-1)를 group by 사용
select trunc(kor,-1)kor ,count(*) from stu_score
where trunc(kor,-1) =90
group by trunc(kor,-1); 

select k_kor, count(k_kor)k_count from
(select trunc(kor,-1) as k_kor from stu_score)
group by k_kor;

--그룹함수 group by 사용 (*별칭 사용X)
select department_id, count(*) from employees
group by department_id
order by department_id;

select emp_name, count(emp_name) from employees
group by emp_name;

-- 부서별 평균 월급 구하시오.
select department_id, round(avg(salary),2)
from employees
group by department_id
order by department_id;

-- clerk, mep, man별 월급 평균을 구하시오.

--문자열 자르기: substr(job_id, 4)
select substr(job_id,4), count(substr(job_id,4)) from employees
where substr(job_id,4) = 'CLERK'
group by substr(job_id, 4);

select substr(job_id,4), count(substr(job_id,4)) from employees
where substr(job_id,4) = 'CLERK'
group by substr(job_id, 4);

-- 부서별 최대 월급, 최소 월급, 평균 월급 출력
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

-- 부서별 사원수, 커미션을 받는 사원 수 출력

-- 1. 부서별 사원 수 출력
select department_id, count(*) from employees
group by department_id;

-- 2. 부서별 커미션 받는 사원 수 출력
select department_id,count(department_id), count(commission_pct) from employees
group by department_id;

------------------------------------------------------------------------------

-- having 절: broup by에 대한 조건절
-- where: 일반 컬럼의 조건절
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select emp_name, department_id, round(avg(salary),2) from employees
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- emp_name 두번째 글자가 a로 시작하는 것 제외
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- 평균 월급보다 작은 그룹만 출력
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by avg(salary);

-- 부서별 최대 월급이 8000이상인 부서, 최대월급을 출력하시오.
select department_id, max(salary) from employees
where department_id is not null
group by department_id
having max(salary) >= 8000
order by department_id;

--------------------------------------------------------------------------------

--join (RDBMS)
select emp_name, department_id, department_name, salary from employees;

select department_id, department_name from departments;

select count(*) from employees; --107개
select count(*) from departments; -- 27개

-- +조인: 테이블 2개 의미없이 연결만 실행.
-- 107*27 = 2889
select *from employees, departments;

-- inner join: equi join- 동일 칼럼 기준 조인, non-equi join - 동일 칼럼X, 다른 조건 사용 조인.
-- outer join
-- self join

-- equi join: 두 테이블 간 같은 컬럼 비교, 해당 데이터 출력
-- 106개, null 값은 검색되지 않음.
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id;

select department_id, department_name from departments;

select id, name from member;
select id, btitle, bcontent from board;

update member set name = '홍길자'
where id='aaa';

select * from member;

select bno,name,gender,btitle,bcontent, bdate, bgroup, bstep, bhit, bfile from board, member
where member.id = board.id;


