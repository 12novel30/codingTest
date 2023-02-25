-- 코드를 입력하세요
# with f as (
#     SELECT FLAVOR, sum(TOTAL_ORDER) as july_sum
#     from JULY
#     group by FLAVOR
# )
# select FLAVOR
# from FIRST_HALF natural inner join f
# order by TOTAL_ORDER + july_sum desc
# limit 3










select f.FLAVOR as FLAVOR
from first_half f left outer join july j
on f.FLAVOR = j.FLAVOR
group by f.FLAVOR
order by f.total_order + sum(j.total_order) desc
limit 3










