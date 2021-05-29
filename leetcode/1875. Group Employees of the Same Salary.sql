# Write your MySQL query statement below

select employee_id, name,salary, DENSE_RANK() OVER (ORDER BY salary asc) as team_id  from employees
where salary in (
select salary from employees group by salary having count(salary)>1
)