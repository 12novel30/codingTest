-- 코드를 입력하세요
select MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE m left outer join REST_REVIEW r
    on m.MEMBER_ID = r.MEMBER_ID
where m.MEMBER_ID in (select MEMBER_ID
                     from REST_REVIEW 
                     group by MEMBER_ID
                     having count(*) = (select count(*)
                                       from REST_REVIEW
                                       group by MEMBER_ID
                                        order by count(*) desc
                                       limit 1)
                     )
order by REVIEW_DATE, REVIEW_TEXT