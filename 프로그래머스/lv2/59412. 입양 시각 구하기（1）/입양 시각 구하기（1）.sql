-- 코드를 입력하세요
# SELECT date_format(DATETIME, '%k') as HOUR, count(ANIMAL_ID) as COUNT
# from ANIMAL_OUTS
# group by HOUR
# having HOUR between 9 and 19 
# order by date_format(DATETIME, '%H')

SELECT extract(HOUR from DATETIME) as HOUR, count(ANIMAL_ID) as COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR between 9 and 19 
order by HOUR