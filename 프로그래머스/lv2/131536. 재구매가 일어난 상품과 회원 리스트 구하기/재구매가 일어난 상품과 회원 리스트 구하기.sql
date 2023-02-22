-- 코드를 입력하세요
with tmp as
(select USER_ID, PRODUCT_ID, count(SALES_DATE) as count
from online_sale
group by USER_ID, PRODUCT_ID)

select USER_ID, PRODUCT_ID
from tmp
where count > 1
order by USER_ID, PRODUCT_ID desc