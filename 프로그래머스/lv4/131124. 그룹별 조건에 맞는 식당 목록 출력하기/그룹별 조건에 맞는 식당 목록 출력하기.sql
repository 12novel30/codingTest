-- 코드를 입력하세요
# select MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
# from MEMBER_PROFILE m left outer join REST_REVIEW r
#     on m.MEMBER_ID = r.MEMBER_ID
# where m.MEMBER_ID in (select MEMBER_ID
#                      from REST_REVIEW 
#                      group by MEMBER_ID
#                      having count(*) = (select count(*)
#                                        from REST_REVIEW
#                                        group by MEMBER_ID
#                                         order by count(*) desc
#                                        limit 1)
#                      )
# order by REVIEW_DATE, REVIEW_TEXT










# MEMBER_NAME, REVIEW_TEXT, REVIEW_DATE
select MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
from member_profile p left outer join rest_review r
on p.member_id = r.member_id
where p.MEMBER_ID in (select MEMBER_ID
                   from rest_review
                   group by member_id
                   having count(*) = (select count(*)
                                              from rest_review
                                              group by member_id
                                                order by count(*) desc
                                              limit 1)
                   )
order by REVIEW_DATE, REVIEW_TEXT







