create table daum_movie(
 dno number(4),
 title varchar2(100),
 img varchar2(100),
 audience number(10),
 ddate date
)
;

-- img 크기 변경
alter table daum_movie modify img varchar2(300);


select * from daum_movie;
create table coupang(
 cno number(4),
 title varchar2(100),
 img varchar2(300),
 price number(10),
 grade number(10),
 eval_num number(10)
)
;

alter table coupang modify title varchar2(500);

select * from coupang;

create table mmdate (
mdate date
);

insert into mmdate values (TO_DATE('2024-06-27 06:00:00','yyyy-mm-dd HH24:MI:SS') );
select * from coupang;
select * from daum_movie;