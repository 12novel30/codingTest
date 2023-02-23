-- 코드를 입력하세요
SELECT o.PRODUCT_ID as PRODUCT_ID, PRODUCT_NAME,
        PRICE*sum(AMOUNT) as TOTAL_SALES
from FOOD_PRODUCT p natural inner join FOOD_ORDER o
where date_format(PRODUCE_DATE, '%Y-%m-%d') like '%22-05%'
group by PRODUCT_ID
order by TOTAL_SALES desc, PRODUCT_ID