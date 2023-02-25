-- 코드를 입력하세요
# SELECT o.PRODUCT_ID as PRODUCT_ID, PRODUCT_NAME,
#         PRICE*sum(AMOUNT) as TOTAL_SALES
# from FOOD_PRODUCT p natural inner join FOOD_ORDER o
# where date_format(PRODUCE_DATE, '%Y-%m-%d') like '%22-05%'
# group by PRODUCT_ID
# order by TOTAL_SALES desc, PRODUCT_ID









# PRODUCT_ID, PRODUCT_NAME, TOTAL_SALES
select p.PRODUCT_ID as PRODUCT_ID, PRODUCT_NAME, price*sum(amount) as TOTAL_SALES
from food_product p left outer join food_order o
on p.PRODUCT_ID = o.PRODUCT_ID
where month(produce_date) = 5 and year(produce_date) = 2022
group by PRODUCT_ID
order by TOTAL_SALES desc, PRODUCT_ID









