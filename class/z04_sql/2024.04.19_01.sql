select * from employees;
--list dict [{}] --> json형태로 들어옴
--오라클과 파이썬 연결
--모두 다 오라클db와 연결 가능
--하나의 통로, 관리, 중복 제거, 안정성, 보안성 보장 --> DB에 저장하는 이유

--회원정보 테이블 생성
create table member(
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

--select, delete, insert, create  --> rollback 가능, 나머지는 불가

--데이터 입력
insert into member (id,pw,name,phone) values (
'aaa','1111','홍길동','010-1111-1111'
);

insert into member values (
'bbb','1111','유관순','010-2222-2222'
);

insert into member(id,name,phone) values (
'ccc','이순신','010-3333-3333'
);

--칼럼 생략 시 칼럼 수와 맞춰서 입력해야 함.
/*컬럼 수 부족 에러
insert into member values (
'ddd','강감찬','010-4444-4444'
);
*/

select id,pw,name,phone from member;
--오라클에서 null값 = 무한대 값

--commit 전까진 rollback 할 경우 임시저장소에 있는 데이터 삭제됨.
commit;

--임시저장소에 들어가 있는 데이터만 rollback 가능.
rollback;

select *from member;

insert into member values (
'ddd','1111','강감찬','010-4444-4444'
);

select *from member;

--수정
update member set pw='2222' where id='ccc';

rollback;

--모든 테이블 확인
select *from stu_score;

--테이블 타입 확인
desc member;

-- 오라클 타입
-- number-숫자, date-날짜, char-고정문자, varchar2-가변문자, clob-대용량문자

--number: 정수, 실수
--number(4): -9999~9999

create table mem (
no number, --데이터 길이 미지정
no2 number(4),
no3 number(4,2) --소수점 표시/없으면 정수로 인식
);

insert into mem (no) values ( 1234567890 );
insert into mem (no2) values (9999);
insert into mem (no2) values (1.11); --1만 인식, 소수점은 지워짐
insert into mem (no2) values (-9999);

insert into mem (no3) values (11.11);
insert into mem (no3) values (111); --오류: 111.00으로 인식

select * from mem;
commit;

create table mem2(
no number(4,2),
mdate date,
mdate2 timestamp --date: 년,월,일,시,분,초까지 저장 가능 = timestamp 밀리초까지 저장 가능함.
);

insert into mem2(mdate) values ('2024-04-19');
insert into mem2(mdate) values (sysdate); --sysdate: 현재 시간
insert into mem2(mdate2) values (sysdate);
insert into mem2 (mdate,mdate2) values (sysdate, sysdate+30);

select * from mem2;
select to_char(mdate,'yyyy/mm/dd hh:mi:ss') from mem2;
select to_char(mdate2,'yyyy/mm/dd hh:mi:ss:ff') from mem2;

--create, insert만 임시 저장, select는 보여주기만 가능, commit까지 해야 완전 저장
select mdate,mdate+30 from mem2;

select * from employees;

select sysdate - hire_date from employees;

create table mem3 (
no number(4,3),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);

--char, varchar2
--char: 고정 문자
insert into mem3 (tel) values ('11112222');
insert into mem3 (tel) values ('22223333');
insert into mem3 (tel) values ('111');
insert into mem3 (tel) values ('123456789');
insert into mem3 (tel) values ('홍');

--varchar2: 가변 문자
insert into mem3 (name) values ('11112222');
insert into mem3 (name) values ('홍길동'); --한글:: 3크기
insert into mem3 (name) values ('신사임당'); --12 자리 필요
INSERT INTO MEM3 (NAME) VALUES ('AAA');
insert into mem3 (name) values ('aaa');

commit;

-- select, from 2개의 키워드로 구성 됨
-- * 모든 컬럼을 출력
-- sql구문: 대소문자 구분X, 데이터는 대소문자 구분.
select * from mem3 where name = 'aaa';
select * from mem3 where name = 'AAA';
select name from mem3 where lower(name) = 'aaa';

select emp_name, department_id from employees;

--distinct: 중복 제외
select distinct department_id from employees;

select * from departments;

select department_id, department_name from departments;

select * from departments;
select * from employees;
select * from jobs;
select * from products;

select * from mem3;
select no, mdate2, tel, name, mdate from mem3;

select * from employees;
--Q. 사원번호, 사원이름, 급여, 입사일자
select employee_id, emp_name, salary, hire_date from employees;

--desc: 타입 확인
desc employees;

select * from stu_score;
drop table stu_score;

create table stu_score (
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values (
1,'홍길동',100,100,100,300,100,1
);

insert into stu_score values (
5,'김구',100,100,100,300,100,1
);

commit;

select * from stu_score;