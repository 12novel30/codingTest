-- 코드를 입력하세요
# SELECT PRODUCT_CODE, PRICE * sum(SALES_AMOUNT) as SALES
# from PRODUCT natural inner join OFFLINE_SALE
# group by PRODUCT_CODE
# order by SALES desc, PRODUCT_CODE













# PRODUCT_CODE, SALES
select PRODUCT_CODE, price*sum(sales_amount) as SALES
from product p left outer join offline_sale s
on p.product_id = s.product_id
group by p.product_id
order by sales desc, PRODUCT_CODE










