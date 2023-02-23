-- 코드를 입력하세요
with f as (
    SELECT BOOK_ID, AUTHOR_ID, CATEGORY, PRICE*sum(SALES) as summation
    from BOOK natural inner join BOOK_SALES 
    where SALES_DATE like '2022-01-%'
    group by BOOK_ID
)
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(summation) as PRICETOTAL_SALES
from AUTHOR a natural inner join f
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID, CATEGORY desc