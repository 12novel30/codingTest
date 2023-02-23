-- 코드를 입력하세요
SELECT o.ANIMAL_ID as ANIMAL_ID, o.ANIMAL_TYPE as ANIMAL_TYPE, o.NAME as NAME
from ANIMAL_INS i right outer join ANIMAL_OUTS o
        on o.ANIMAL_ID = i.ANIMAL_ID
where SEX_UPON_INTAKE like 'Intact%' and
        (SEX_UPON_OUTCOME like 'Neutered%' or
        SEX_UPON_OUTCOME like 'Spayed%')
order by o.ANIMAL_ID