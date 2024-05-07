select * from stu_score
where name like '_a%';

select * from board;

select board.id, member.name from board,member;

select a.*, b.name from board a, member b
where a.id = b.id;

select bno, a.id, name, btitle, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile 
from board a, member b
where a.id = b.id;

select no, name, total, avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

select * from stu_score;

select employee_id, emp_name, salary, salary+(salary*nvl(commission_pct,0)) salary2, to_char((salary*1410),'L999,999,999') kor_salary 
from employees;

select department_id, round(avg(salary),2), max(salary), min(salary) from employees
group by department_id;

-- 홍이라고 검색하면 홍에 관련된 학생 모두 출력하도록 하시오.
select * from stu_score
where name like '%홍%';