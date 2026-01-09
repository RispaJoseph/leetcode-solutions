-- Write your PostgreSQL query statement below  
select current.id
from weather current
join weather previous
on current.recorddate=previous.recorddate+1
where current.temperature>previous.temperature
