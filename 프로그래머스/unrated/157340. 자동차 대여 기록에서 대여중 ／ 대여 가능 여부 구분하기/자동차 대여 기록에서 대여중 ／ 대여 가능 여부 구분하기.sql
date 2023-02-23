-- 코드를 입력하세요
with f as (
    select CAR_ID,
            case
                when START_DATE <= '2022-10-16' and END_DATE >= '2022-10-16'
                then true
                else false
            end as boolean
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)
select CAR_ID,
        case
            when sum(boolean) >= 1
            then '대여중'
            else '대여 가능'
        end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY c natural inner join f
group by CAR_ID
order by CAR_ID desc