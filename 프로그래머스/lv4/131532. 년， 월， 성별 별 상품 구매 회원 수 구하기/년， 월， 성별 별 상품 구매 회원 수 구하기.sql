-- 코드를 입력하세요
SELECT extract(YEAR from SALES_DATE) as YEAR,
        extract(MONTH from SALES_DATE) as MONTH,
        GENDER,
        count(distinct USER_ID) as USERS
from USER_INFO natural inner join ONLINE_SALE
where GENDER is not null
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER