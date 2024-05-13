-- [ 1 ] 사원정보(Employees) 테이블에서
-- 사원번호, 이름, 급여, 부서, 입사일, 상사의 사원번호를 출력하시오.
-- 이때 이름은 이름과 직급을 연결하여 Name이라는 별칭으로 출력하시오(107행).
select employee_id, emp_name||' '||job_id "Name", salary, department_id, hire_date, manager_id
from employees;

--[ 2 ] 사원정보(Employees) 테이블에서
-- 사원의 이름과 성은 Name, 업무는 Job, 급여는 Salary, 연봉에 $100 보너스를 추가하여 계산한 값은 Increase Ann_Salary,
-- 급여에 $100 보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력하시오(107행).
select emp_name "Name", job_id "Job", salary "Salary", ((salary+100)*12) "Increase Salary"
from employees;

--[ 3 ] H R 부서에서 예산 편성 문제로 급여 정보 보고서를 작성하려고 한다. 
-- 사원정보(Employees) 테이블에서 급여가 $7,000~$10,000 범위 이외인 사람의 이름과 성(Name으로 별칭) 및 급여를 급여가 적은 순서로 출력하시오(75행).
select emp_name "Name", salary from employees
where salary < 7000 or salary > 10000
order by salary;

-- 7000보다 크고 10000보다 작은 사원
select emp_name, salary from employees
where salary not between 7000 and 10000;

--[ 4 ] 사원의 성(emp_name) 중에 ‘e’ 및 ‘o’ 글자가 포함된 사원을 출력하시오. 이때 머리글은 ‘e or o Name’이라고 출력하시오(8행).
-- 성만 잘라내기?
select emp_name "e or o Name" from employees
where lower(emp_name) like '%e%' or lower(emp_name) like '%o%';

--[ 5 ] 이번 분기에 60번 IT 부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다. 
-- 이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다. 
-- 60번 IT 부서 사원의 급여를 12.3% 인상하여 정수만(반올림) 표시하는 보고서를 작성하시오. 
-- 보고서는 사원번호, 성과 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력하시오(5행).
select employee_id, emp_name "Name", salary, round((salary+(salary*0.123))) "Increase Salary"  
from employees
where department_id = 60;


--[ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 보고서에 사원의 이름과 성(Name으로 별칭), 급여, 수당여부에 따른 연봉을 포함하여 출력하시오. 
-- 수당여부는 수당이 있으면 “Salary + Commission”, 수당이 없으면 “Salary only”라고 표시하고, 별칭은 적절히 붙이시오. 또한 출력 시 연봉이 높은 순으로 정렬하시오(107행).
-- 방법1: case - when, then
select emp_name "Name", salary, (salary*nvl(commission_pct,0)) comm_salary,
case
when commission_pct is null then 'Salary only'
when commission_pct is not null then to_char(salary*commission_pct)
end as "Salary + Commission"
from employees
order by salary desc;

-- 방법2: decode
select emp_name "Name", salary, commission_pct,
decode(department_id,
'10', 'A',
'20','B') as dept
from employees
order by salary desc;

-- 방법3: nvl2 (commission_pct, 'Salary only'(A1) , 'Salary + Commission'(A2))
-- null이 아닐 경우 A1, null일 경우 A2


--[ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최댓값, 급여 최솟값을 집계하고자 한다.
-- 계산된 출력값은 여섯 자리와 세 자리 구분기호, $ 표시와 함께 아래와 같이 출력하시오. 
-- 단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 출력 시 머리글은 다음 그림처럼 별칭(alias) 처리하시오(11행).
-- ****함수와 컬럼 같이 쓰고 싶으면 group by 넣기!!!****
select * from employees;

select department_id, to_char(sum(salary),'$999,999') sum , to_char(avg(salary),'$999,999') avg , 
to_char(max(salary),'$999,999') max ,to_char(min(salary),'$999,999') min 
from employees
where department_id is not null
group by department_id
order by department_id;

--[ 8 ] 사원들의 업무별 전체 급여 평균이 $10,000보다 큰 경우/를 조회하여 업무별 급여 평균을 출력/하시오. 
-- 단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오(7행).
-- ****함수와 컬럼 같이 쓰고 싶으면 group by 넣기!!!****
-- 방법 1
select * from (
select department_id, round(avg(salary))avg from employees
where job_id not like '%CLERK%'
group by department_id)
where avg > 10000
order by avg desc;

-- 추천 방법 2: having 절
select department_id, round(avg(salary))avg from employees
where job_id not like '%CLERK%'
group by department_id
having -- (그룹 컬럼의 조건 넣는 곳)
avg(salary) > 10000
order by avg desc;

--[ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
--(예) 홍길동은 허균에게 보고한다 → Eleni Zlotkey report to Steven King
--어떤 사원이 누구에게 보고하는지 위 예를 참고하여 출력하시오. 단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하고, 상사의 이름과 성은 대문자로 출력하시오(107행).
-- outer join (+)
select upper(a.emp_name) "상사",  b.emp_name "사원" 
from employees a, employees b
where a.employee_id(+) = b.manager_id;

--[ 10 ] Employees, Departments 테이블의 구조를 파악한 후 (사원 수가 다섯 명 이상인 부서)의 부서이름과 사원 수를 출력하시오. 
-- 이때 사원 수가 많은 순으로 정렬하시오(5행).
select * from employees;
select * from departments;

--방법1
select b.department_name, a.department_id, a.count
from (select * from (select department_id, count(department_id)count 
from employees 
group by department_id)
where count >= 5) a, departments b
where a.department_id = b.department_id
order by a.count desc;

-- 방법 2: having 절
select b.department_name, a.department_id, count 
from (select department_id, count(department_id)count from employees 
group by department_id
having count(department_id) >= 5)a, departments b
where a.department_id = b.department_id
order by count desc;

-- [ 추가 ] HR 부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고 있다.
-- Tucker가 포함된 사원보다 급여를 많이 받고 있는 사원의 이름, 업무, 급여를 출력하시오(15행).
select b.emp_name, b.job_id, b.salary from 
(select emp_name, job_id, salary 
from employees
where emp_name like '%Tucker%')a, employees b
where a.salary < b.salary;



-- [ 추가 ] 모든 사원의 소속부서 평균연봉을 계산하여 사원별로 이름, 업무,
-- 급여, 부서번호, 부서평균연봉(Department Avg Salary로 별칭)을 출력하시오(107행).
select b.emp_name, b.job_id, b.salary, a.*
from (
select department_id, round(avg(salary))"Department Avg Salary"
from employees
group by department_id)a, employees b
where a.department_id(+) = b.department_id;

select emp_name from(
select * from employees 
where salary > (select avg(salary) from employees)
)
where emp_name like '%a%';
