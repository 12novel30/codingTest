-- 코드를 입력하세요
# SELECT i.ANIMAL_ID as ANIMAL_ID, i.NAME as NAME
# from ANIMAL_INS i left outer join ANIMAL_OUTS o
#     on i.ANIMAL_ID = o.ANIMAL_ID
# where i.DATETIME > o.DATETIME
# order by i.DATETIME










# ANIMAL_ID, NAME
select i.ANIMAL_ID as ANIMAL_ID, i.NAME as NAME
from animal_ins i left outer join animal_outs o
    on i.animal_id = o.animal_id
where o.datetime < i.datetime
order by i.datetime











