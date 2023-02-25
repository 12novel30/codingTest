-- 코드를 입력하세요
# SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
# from BOOK, AUTHOR
# where book.AUTHOR_ID = author.AUTHOR_ID
#     and CATEGORY = '경제'
# order by PUBLISHED_DATE

















select BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book b left outer join author a
    on b.author_id = a.author_id
where category = '경제'
order by published_date




