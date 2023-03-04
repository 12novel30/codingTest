-- 코드를 입력하세요
# SELECT left(PRODUCT_CODE, 2) as CATEGORY, count(PRODUCT_ID) as PRODUCTS
# from PRODUCT
# group by CATEGORY
# order by CATEGORY




select left(product_code,2) as CATEGORY, count(*) as PRODUCTS
from product
group by CATEGORY
order by product_code