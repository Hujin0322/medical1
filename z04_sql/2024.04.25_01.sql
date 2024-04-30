-- * 어제, 오늘, 내일
select sysdate-1, sysdate, sysdate+1 from dual;

-- * 오늘, 이 달의 첫 일, 이 달의 마자막 일
select sysdate, trunc(sysdate,'month'),last_day(sysdate) from dual;

--* 두 날짜 간 일 수, 두 날짜 간 달 수
select round(sysdate-hire_date,3), trunc(months_between(sysdate, hire_date),2) from employees;

-- trunc 일 단위 버린 뒤 점수대별 인원수 확인.
select trunc(kor,-1)kor,count(kor) from stu_score
group by trunc(kor,-1)
order by kor;

--Q. hire_date에서 월만 출력하기.
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') hire_date, count(hire_date) from employees
group by to_char(hire_date,'mm')
order by hire_date;

--Q. hire_date 2008년도 출력, 년도별 인원수 출력
select to_char(hire_date,'yyyy')hire_date, count(hire_date) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

-- 형 변환: number, character, date
-- number: 사칙연산O, 쉼표 표시X, 원화 표시X
-- char: 사칙연산X, 쉼표 표시O, 원화 표시O
-- date: 날짜별 (+,-) O, 날짜 출력 형태는 변경 불가.(--> to_char 로 변경 필요)

--Q. ko+2024+0001
-- 시퀀스 형태로 학번 부여 (stu_seq를 가지고 5명의 학번 출력)
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,('0000'))) from dual;

--Q. (123,456,789)+(100,000) = 123556789 출력
select to_char(to_number('123,456,789','999,999,999') + to_number('100,000','999,999'),'999,999,999') from dual;

select to_char(salary,'999,999') from employees;

--숫자 타입을 날짜 타입으로 변경
select 20240425+3 from dual;
select to_char(20240425+3)+3 from dual;
select to_date(20240425+3)+3 from dual;

--숫자 타입을 날짜 타입으로 변경
select emp_name, hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

--Q. 8월에 입사한 사원 이름에 2번째에 a가 들어가 있는 사람 출력.
select hire_date, emp_name from employees
where emp_name like '_a%' and to_char(hire_date,'yyyy-mm-dd') like '____-08-__';

--1. 1,5,8월에 입사
select hire_date from employees
where to_char(hire_date,'mm') = '01' or to_char(hire_date,'mm') = '05' or to_char(hire_date,'mm') = '08';

select hire_date from employees
where to_char (hire_date,'mm') in ('01','05','08');

--2. 이름 두번째에 a가 들어가 있는 사람 출력
select emp_name from employees
where emp_name like '_a%';

--3. 입사일, 이름 합치기
select emp_name, hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
order by hire_date;

--Q. 20070101 이후 입사 + 사원 이름 a가 들어가 있는 사람 출력
select emp_name, hire_date from employees
where hire_date > to_date(20070101) and emp_name like '%a%'
order by hire_date;

--문자 타입을 날짜 타입으로 변경
select sysdate - to_date('20240401') from dual;

select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;  

select *from m_date;

create table eventDate (
eno number,
e_today date,
e_choice_day date,
e_preiod number
);

--입력 시 날짜 타입에 문자(형태 - 날짜 형태)를 입력해도 저장됨.
--날짜 - 문자 = 불가능 --> 문자를 날짜 타입으로 변경해야 함.
insert into eventDate values(
seq_mno.nextval, sysdate, '2024-04-01', sysdate - to_date('2024-04-01')
);

select *from eventdate;

-- 문자 타입을 숫자 타입으로 변경
select to_number('20,000','99,999') - to_number('10,000','99,999') from dual;

-- null을 0으로 치환 nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo
select manager_id from employees
order by manager_id desc;

--숫자 타입이 문자 타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;

-------------------------------------------------------------------------------

-- 그룹 함수: sum, avg, count(), count(*), min, max


-- 그룹 함수 count
select count (*) from employees;
--결과값: 107
select count(emp_name) from employees;
--null값 존재 시 제외 -106개
select count(manager_id) from employees;

select emp_name, manager_id from employees;

-- sum: 총 합
select sum(salary) from employees;

--avg: 평균
select avg(salary) from employees;

--min: 최소값, max: 최대값
select min(salary), max(salary) from employees;

--Q. 평균보다 높은 연봉 출력 (이중쿼리)
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees);

--Q. 최소 월급을 받는 사람의 사번과 이름 출력
select employee_id, emp_name, salary from employees
where salary = (select min(salary) from employees);

--Q. 최대 월급 받는 사람 출력
select employee_id, emp_name, salary from employees
where salary = (select max(salary) from employees);

--부서번호가 50번인 사원만 전체 월급.
select department_id, salary from employees;

select sum(salary) from employees
where department_id = 100;

select count(*) from stu_score;

-- Q. kor 점수가 80점 이상인 학생 출력
select name,kor from stu_score
where kor>=80;

--Q. 국어 점수 평균 이상, 영어 점수 평균 이상인 학생 출력
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

--Q. 국어 점수,영어 점수, 수학 점수 각 최고점인 학생 출력
select name,kor, eng, math from stu_score
where kor = (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score)
or math = (select max(math) from stu_score);

--Q. employees에서 월급 최대, 최소, 평균 사원 출력
select emp_name, salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select avg(salary) from employees);

--최대값
select emp_name, salary from employees
where salary = (select max(salary) from employees);

--Q. 평균값보다 낮은 사원 중 최대값 출력
--1). 
select emp_name,salary from employees
where salary = 6400;

--2). 6400 대신 평균값보다 낮은 사원 중 최대값 출력

--2-1). 평균보다 낮은 값 --> 56명
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc

--2-2). 평균보다 낮은 56명 중 최대값 6400 출력
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc);

--3). 합침
select emp_name,salary from employees
where salary = (
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc)
);

--문자 함수
--lpad, rpad: 빈공백 채우기
select emp_name, lpad(emp_name,15,'#') from employees;
select emp_name, rpad(emp_name,20,'@') from employees;

--ltrim, rtrim: 지정 문자 자르고 출력
select emp_name, ltrim(emp_name, 'Do') from employees;

-- ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

--substr(데이터, 순서, 갯수): 데이터에서 순서부터 갯수만큼 잘라오기 
select emp_name, substr(emp_name, 3,4) from employees;

select job_id from employees;

--Q. job_id의 앞 두글자와 사원번호를 결합해서 출력하시오.
select substr(job_id,0,2)||employee_id from employees;

-- length : 문자열의 길이
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- 날짜함수 +,- 가능, 날짜데이터 끼리 더하기는 안됨.
-- 날짜데이터 +,- 숫자 가능
select sysdate+1 from dual;

-- 날짜데이터 - 날짜데이터 가능
select sysdate - hire_date from employees;

-- 날짜데이터 + 날짜데이터 불가능
select sysdate + hire_date from employees;

select sysdate,trunc(sysdate,'month'),round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

-- 개월수 추가,축소
select sysdate,add_months(sysdate,-2) from dual;

-- ceil올림, floor버림, mod나머지, power제곱
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

-- 퀴즈. 사원명 입사일 출력
select emp_name||to_char(hire_date,' yyyy"년" mm"월" dd"일" day') from employees;


-- 퀴즈. 사원명, 자리수 9자리 빈공백 0으로 표시 
-- salar*1400 앞에 원화표시와 쉼표를 넣어 출력하시오.
select salary, to_char(salary*1400, 'L000,000,000' ) from employees;

-- 자신의 생일과 자신의 생일이 속한 달의 마지막날짜
--- '2010-10-10'
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;

select * from member;

desc member;

-- DDL(data denfinition language)

-- 컬럼추가, 수정, 삭제 
-- 위 commit,rollank이 안됨. 바로 저장됨. 
alter table member add gender varchar2(6) default 'female' not null;
desc member;

-- 컬럼수정 
-- 컬럼이름변경
alter table member rename column name to stu_name
;

-- 타입변경
alter table member modify(stu_name varchar2(50));

-- 기존의 데이터가 변경하려는 크기보다 작을때만 가능
update member set stu_name='';
alter table member modify(stu_name varchar2(6));
-- 컬럼의 타입을 변경하려면 컬럼데이터가 빈공백이거나 null일때 가능
alter table member modify(stu_name number(4));
desc member;
select stu_name from member;


-- 컬럼삭제 - commit,rollback 이 없음.
-- alter table member drop column phone;


select * from member;

update member set gender = 'male';

commit;