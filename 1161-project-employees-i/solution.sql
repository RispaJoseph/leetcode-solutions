-- Write your PostgreSQL query statement below
select project_id,round(avg(experience_years)::numeric,2) as average_years
from Project p
left join Employee e on e.employee_id=p.employee_id
Group by project_id order by project_id;
