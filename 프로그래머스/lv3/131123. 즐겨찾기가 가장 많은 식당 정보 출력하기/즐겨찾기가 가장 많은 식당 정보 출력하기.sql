-- 코드를 입력하세요
with f as (
    select FOOD_TYPE, max(FAVORITES) as most
    from REST_INFO
    group by FOOD_TYPE
)

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO r natural inner join f
where FAVORITES = most
group by FOOD_TYPE
order by FOOD_TYPE desc