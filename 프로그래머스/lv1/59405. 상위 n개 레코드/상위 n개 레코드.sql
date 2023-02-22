-- 코드를 입력하세요
with min_datetime (value)
    as (select min(DATETIME)
       from ANIMAL_INS)
SELECT NAME
from ANIMAL_INS, min_datetime
where ANIMAL_INS.DATETIME = min_datetime.value