
--trunc: 버림, round: 반올림
select sysdate, hire_date, sysdate - hire_date, round(sysdate - hire_date,3) from employees;

--어제: sysdate-1, 내일 sysdate+1
select sysdate-1 어제, sysdate 오늘, sysdate+1 내일, sysdate+100 from dual;

-- seq_m_no sequence, 1-9999, 1씩 증가, 5번 반복

create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

--Q. m_yesterday, m_today, m_tomorrow, m_year 날짜 컬럼을 가진 table m_date
-- 어제, 오늘, 내일, 1년 후 날짜를 저장하시오.
create table m_date (
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date
);

insert into m_date values(
seq_m_no.nextval, sysdate-1, sysdate, sysdate+1, sysdate+365
);

select *from m_date;

--abs: 절대값, ceil, floor, round, trunc-자릿수O
select abs(hire_date - sysdate) from employees;

--날짜의 월을 기준으로 반올림
select hire_Date, round(hire_date,'month') from employees;

--날짜의 월을 기준으로 버림
select hire_date, trunc(hire_date,'month'), round(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일 , hire_date from employees
order by hire_date;

select * from channels;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period = '201111';

select trunc(kor,-1) t_kor,count(trunc(kor,-1)) from students
group by trunc(kor,-1)
order by t_kor;

--날짜의 월을 기준으로 버림
select trunc(hire_date,'month')m_hire_date, count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date;

-- drop table stu_score;
-- drop table stu_score;

select *from stu_score
order by no;

update stu_score set name ='관순스'
where no=10;

select *from stu_score
order by no;

update stu_score set avg = (total/3);

-- 2개의 날짜에서 월 간격 확인
select hire_date, floor(months_between (sysdate,hire_date)), trunc(sysdate-hire_date,2) 
from employees;

--개월 추가
select hire_date, add_months(hire_date,6) from employees;

--last day: 해당 달의 마지막날
select hire_date, last_day(hire_date), round(hire_date,'d') from employees;

--날짜를 기준으로 현재, (달의) 처음일, 마지막일
select sysdate 현재일,trunc(sysdate,'month')처음일, last_day(sysdate)마지막일 from dual;

-- 특정 요일의 날짜 확인 
select sysdate, next_day(sysdate,'토요일') from dual;

-- 요일의 처음일: trunc, 'd'/ 다음 요일의 날짜: next_day, '요일'
select sysdate, trunc(sysdate,'d'),next_day(sysdate,'토요일') from dual;

-- board 테이블 default는 입력 없을 시, 자동 입력.
create table board (
bno number(4) primary key, --중복X, null 허용 X --> 기본키로 사용.
id varchar2(30),
btitle varchar2(1000),
bcontent clob, --varchar2(3000자까지 가능), clob(무제한)- varchar2의 타입과 같음
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval, 'aaa', '제목입니다.','내용입니다.',sysdate,0,board_seq.currval,0, 0, '1.jpg'
);

insert into board (bno,id, btitle, bcontent, bgroup, bfile) values(
board_seq.nextval, 'bbb', '이벤트 신청', '이벤트를 신청합니다.', board_seq.currval, '2.jpg'
);

select *from board;

-- 형 변환 - number, character, date
select sysdate from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate, 'yy/mm/dd') from dual;
select to_char(sysdate, 'yyyy') from dual;

--ko20240001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

-- ex)수요일  --> dy:수/ day: 수요일
select to_char(sysdate, 'dy'), to_char(sysdate, 'day') from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

--Q. hire_date, yyyy-mm-dd hh:mi:ss mon day
select to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon day') from employees;

--am,pm: 오전, 오후/ hh24: 24시간으로 표시
select to_char(sysdate, 'pm hh24:mi:ss') from dual;

select *from stu_score;
select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

--Q. 날짜별로 몇 개의 데이터가 들어가 있는지 출력
select c_date, count(c_date) from stu_score
group by c_date
order by c_date;

-- 문자형(to_char): 사칙연산(+,-,*,/)X. 자릿수 표시O, 쉼표 표시O, 날짜 형태 표시O.
-- 숫자형: 사칙연산 가능 --> 컬럼별 사칙연산O. 자릿수표시(ex. 0001 --> 1로 출력됨)X, 쉼표 표시X.
-- 날짜형: (+,-) 연산O, months-between(날짜1,날짜2): 달 계산, 날짜 유형 지정 출력X

-- 문자형 안에 있는 데이터가 숫자면 자동으로 형변환해서 계산
-- 문자형 안에 문자가 있으면 자동형변환 불가.
select 10 a, 100 b, (10+100) ab, 20+to_char(100), 10+'100' from dual; --가능
select 10 a, 100 b, (10+100) ab, to_char(100), 10+'100원' from dual; --불가

select 12340000,to_char (12340000), length(to_char(12340000,'99,999,999')) from dual;

--'0000' 빈자리수를 0으로 채움, '9999' 빈자리 그대로 둠.
select length(12340000),to_char (12340000), to_char(12340000,'999,999,999'),
length(to_char(12340000,'999,999,999')) from dual;

--L은 원화 표시
select 12340000, to_char(12340000,'L999,999,9999') from dual;

--$는 $표시 그대로
select 12340000, to_char(12340000,'$999,999,9999') from dual;

--소수점 자리 표시
select 1234.1234, to_char(1234.1234, '000,999.99') from dual;

-- 10개 자릿수 표시
-- 공백 제거해서 자릿수 확인 trim
select length(trim(to_char(12345,'0000000000'))), length(trim(to_char(12345,'999,999,999'))) from dual;

select length('안녕하세요,') from dual;
select length(1234000) from dual;

--Q. 123,456,789/ 100,000 값 더하기
--123,456,789 + 100,000 = 값을 출력하시오. 천 단위 표시
select 123456789+100000 from dual;

--1. 123,456,789에 있는 쉼표 제거 --> replace('123,456,789',',','')
--2. 타입을 number 형으로 변경 --> to_number(~)
--3. 더하기
--4. 문자형 타입으로 변경 후 원화, 쉼표 표시
select to_char(to_number(replace('123,456,789',',','')) + to_number(replace('100,000',',','')), 'L999,999,999') 
from dual;

select to_number('0000123') from dual;

-- 날짜형
-- 문자형 +,- 불가.
select '2024-04-24' - '2024-04-23' from dual;
select to_date('2024-04-24') - to_date('2024-04-01') from dual;
select to_date('2024/04/24') - to_date('2024/04/01') from dual;
select to_date('24-04-24') - to_date('24-04-01') from dual;
select to_date(20240401) - to_date(20240423) from dual;

--Q. 20240401 --> 2024-04-01
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

select hire_date from employees
where hire_date >= '20080101';

select c_date from stu_score
where c_date = '2024/04/05'
;

select sysdate - hire_date from employees;
select sysdate - to_date('2024/04/01') from dual;

--Q. 20,000 / 10,000 문자형 10,000출력하시오.
select to_char(to_number('20,000','99,999') - to_number('10,000','99,999'),'99,999') from dual;
select to_char(to_number(replace('20,000',',','')) - to_number(replace('10,000',',','')),'999,999')
from dual;

--Q. 실제 월급 = 월급 + (월급*커미션), 실제월급 출력
--nvl(데이터,0)
select salary, salary+(salary*nvl(commission_pct,0)),commission_pct from employees;

--commission_pct null값만 출력하시오. --> is null
select commission_pct from employees
where commission_pct is null;

--
select manager_id from employees
order by manager_id desc;

--Q. manager_id가 null이면 0 --> nvl(데이터,0)
select nvl(manager_id,0) from employees;

--Q. manager_id가 null이면 ceo로 입력
select nvl(to_char(manager_id),'ceo') from employees;

