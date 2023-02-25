-- 코드를 입력하세요
# SELECT o.ANIMAL_ID as ANIMAL_ID, o.NAME as NAME
# from ANIMAL_OUTS o left outer join ANIMAL_INS i
#     on o.ANIMAL_ID = i.ANIMAL_ID -- natural 쓰면 id 없는 애들까지 다 사라짐
# where i.ANIMAL_ID is null
# order by o.ANIMAL_ID
















select o.ANIMAL_ID as ANIMAL_ID, o.NAME as NAME
from animal_outs o left outer join animal_ins i 
    on o.animal_id = i.animal_id
where i.datetime is null










