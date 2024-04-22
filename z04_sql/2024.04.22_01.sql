select *from employees;

select employee_id, emp_name from employees;

select salary from employees;

--타입: number +,-,*,/ 가능
--별칭: as 별칭 (as 생략 가능)
select salary, salary*1400 as k_sal, salary*1400*12 y_sal from employees;

select *from stu_score;

insert into stu_score values(
7,'홍길자',100,100,96,291,97,1
);

commit;

select department_id from employees;

-- null 값(null value = nvl) --> 0으로 변경
select nvl(department_id,0) from employees;

select *from employees;

-- 월급+(월급*커미션)(커미션에 null값 존재)
-- 대소문자 구별하여 있는 그대로 키워드 출력(특수문자 포함): "" 
select commission_pct from employees; 
select salary, salary + (salary*nvl(commission_pct,0))as "Real_sal" from employees;

--한글 사용 가능
select salary as 년봉 from employees;

---
select *from departments;

--부서번호, 부서 이름 출력
select department_id, department_name from departments;

--여러 개의 데이터를 1개로 합쳐서 넘겨야 할 경우 --> concat: 합침 (||''||)
--홍길동, 유관순, 이순신, 강감찬, 김구 --> split(","): ,로 분리

select *from stu_score;
--concat ||''||
select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total from stu_score;
select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

--중복 제거: distinct
--값 제외 출력: where 컬럼 is not 값
select distinct department_id from employees where department_id is not null;

--manager_id
select distinct manager_id from employees where manager_id is not null;

select *from employees;
select employee_id, salary from employees
where employee_id = 200 or employee_id = 201 or employee_id = 202;

select *from employees
where employee_id >= 200 and employee_id <= 203;

select *from employees
where employee_id <= 150 or employee_id >= 200;

--다르다: <>, !=, ^=

--Q. department_id 10,30,50에 해당되는 사원 출력
select employee_id, department_id, salary from employees
where department_id = 10 or department_id = 30 or department_id = 50;

--Q. 월급 6000 ~ 9000 이하인 사원 출력
-- 정렬 order by 컬럼: 순차정렬 - asc / 역순정렬 - desc
select * from employees
where salary >=6000 and salary <=9000
order by salary asc;

--Q. 월급이 6000, 7000, 8000 인 사원 출력
select employee_id, department_id, salary from employees
where salary = 6000 or salary = 7000 or salary = 8000;

--Q. 부서번호가 50이면서, 월급이 8000이상인 사원 출력
select employee_id, department_id, salary from employees
where department_id = 50 and salary >= 8000;

--Q. stu_score에서 홍길동 출력
select *from stu_score
where name = '홍길동'; --문자는 무조건: '', 변수 이름 그대로 출력: ""

--순차 정렬
select hire_date from employees
order by hire_date asc;

--역순정렬
select hire_date from employees
order by hire_date desc;

select emp_name,hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc;

select hire_date, hire_date+100 from employees;
-- 반올림 round
select round(sysdate - hire_date,2) from employees;

--문자 합치기는 + 연산자 불가능, || 명령어 사용
select emp_name || email from employees;

--입사일 05년 이상, 06년 이하이면서 월급이 6000달러 이상인 사원을 입사일 역순정렬로 출력
select emp_name, hire_date, salary from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >= 6000
order by hire_date desc;

-- !=, <>, ^=, not
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id;

-- salary 5000이상 and 9000이하
select emp_name, salary from employees
where salary >=  5000 and salary <= 9000
order by salary;

--평균이 99점 이상인 학생을 검색
select *from stu_score
where avg >= 99
order by avg;

select *from students;

update students set name = '관순스' 
where no = 10;

commit;

--students
-- 국어: 70점 이상, 평균: 75점 이상
select *from students
where kor >= 70 and avg >= 75;

-- 국어: 80점, 70점, 90점 출력
select *from students
where kor =70 or kor =80 or kor = 90;

update students set kor = 100
where no = 1;

rollback;

select *from students;

--수정
update students set kor = 100, total = 100+eng+math, avg = (100+eng+math)/3
where no =1;

-- 국어 점수 70 ~90 이상 학생 출력
select *from students
where kor >= 70 and kor <= 90;

--100명
select *from students;

-----------------------------------------------------------------------------

--27명, between a and b: a와 b사이 (포함) 검색
select kor from students
where kor between 70 and 90;

--not between a and b
--73명 not between a and b: a보다 크거나, b보다
select kor from students
where kor not between 70 and 90;

--날짜도 between a and b
select hire_Date from employees
order by hire_date;

--입사일이 99년보다 크거나 같고, 01년도보다 작거나 같은 사원 
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_Date asc;

--in: 연산 동일한 필드가 여러 개의 값 중에 하나를 검색할 경우
select name, kor from students
where kor not in(80,70,90);

-----------------------------------------------------------------------------

--이름 검색
select *from students
where name = '홍길동';

-- like 검색: 특정 단어가 포함되어 있는 것 검색
-- 홍%: 홍으로 시작되는 단어를 검색
select *from students
where name like '홍%';

-- %순:  순으로 끝나는 단어 검색
select * from students
where name like '%순';

--%길%: '길'포함된 단어 검색
select * from students
where name like '%길%';

-- _: 한 칸 공간을 사용, 길 앞에 1개의 단어가 있으면서 '길'이 포함된 단어 검색
select *from students
where name like '_길%';

-- 세번째 칸에 t가 들어있는 모든 이름 검색
select name from students
where name like '__t%';

--길이 4자리면서, 3번째에 r이 들어가 있는 이름 검색
--1번 방법:
select name from students
where name like '__r_';

--2번 방법:
select * from students
where name like '__r%' and length(name) = 4;

--길이 4자리만 출력
select * from students
where length(name) = 4;

-- 이름이 'A'로 시작되는 학생 검색
select no,name from students
where name like 'A%';

--이름에 'a'가 들어가 있는 학생 검색
select no,name from students
where name like '%a%';

-- 대소문자 구분없이 a가 들어가 있는 학생 검색
-- 소문자 치환 (lower), 대문자 치환 (upper), 첫글자 대문자 (initcap)
select no, name from students
where lower(name) like '%a%';

--a가 포함되지 않은 이름 검색
select no,name from students
where lower(name) not like '%a%';

--manager_id = 100인 사원 검색
select employee_id, emp_name, manager_id from employees
where manager_id = 100;

-- null은 등가비교가 안됨.
select employee_id, emp_name, manager_id from employees
where manager_id = null;

-- null 검색: is null
select employee_id, emp_name, manager_id from employees
where manager_id is null;

--null 빼고 검색: is not null
select * from employees
where manager_id is not null;

-----------------------------------------------------------------------------

select *from stu_score;

select * from stu_score
order by name asc;

select * from students;

-- kor로 역순정렬 후, 동일값은 eng로 순차정렬
select * from students
order by kor desc, eng asc;

-- total로 역순정렬
select * from students
order by total desc;

--컬럼 추가
alter table students add rank number(3);

--컬럼 타입
desc students;

select * from students;

update students set rank=0;

commit;

-- 등수 (total 기준 역순 정렬)
select no,rank() over (order by total desc) as rank from students;

-- 수정
update students set rank=13 
where no=1;

select * from students;

--이중 query = 이중 select (s1 table과 s2 table) 
update students s1 set s1.rank = (select ranks
from (select no, rank() over (order by total desc) as ranks from students) s2
where s1.no = s2.no);

update students s1 set rank = 13
where no = 1;

select *from (select * from students where avg >= 80)
where kor >= 70;

