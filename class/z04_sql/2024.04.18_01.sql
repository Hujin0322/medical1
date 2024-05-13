--가지고 있는 테이블 검색
select * from tab;

--단축키는 f9로 사용하자
select * from employees;

--table 구조 확인
desc employees;

-- 테이블 생성
create table stu_score (
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2)
);

insert into stu_score ( no, kor, eng, avg) values(
1,100,99,(100+99)/2
);

--모든 칼럼에 값 추가 시 생략 가능
insert into stu_score values(
1,95,98,(95+98)/2
);

insert into stu_score values(
1,80,70.223,(80+70.223)/2
);

select *from stu_score;

commit;

create table num (
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);

--날짜 기본 형태: 24/01/01
--dual: 가상 테이블 (from 뒤에 무조건 table(or dual)) 
select sysdate from dual;

--날짜 포맷 변경: to_char 형변환 -> 포맷 지정
select to_char(sysdate, 'yyyy-mm-dd HH:mi:ss') from dual;

select to_char(sysdate, 'hh:mi:ss') from dual;

select sysdate+100 from dual;

select sysdate - to_date ('24-01-01') from dual;