-- 코드를 입력하세요
# SELECT CAR_ID	CAR_TYPE	FEE
with f as (
    SELECT CAR_ID, CAR_TYPE, daily_fee
    from CAR_RENTAL_COMPANY_CAR natural inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where CAR_TYPE in('세단', 'SUV') and
            CAR_ID not in (select CAR_ID
                          from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                          where END_DATE > '2022-11-01' and start_date < '2022-12-01')
)
select CAR_ID, CAR_TYPE,
        round(daily_fee*(100-discount_rate)/100*30) as FEE
from f natural inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where duration_type = '30일 이상'
group by CAR_ID
having FEE>=500000 AND FEE<2000000
order by FEE desc, CAR_TYPE, CAR_ID desc