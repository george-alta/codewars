/* SELECT e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name,
       e.salary AS old_salary,
       e.salary * (1 + pctIncrease(e.department_id)) AS new_salary
  FROM employees   e,
       departments d
 WHERE e.department_id = d.department_id
 ORDER BY 1; */


 SELECT e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name,
       e.salary AS old_salary,
       e.salary * (1 + pctIncrease(e.department_id)) AS new_salary
  FROM Employees AS e 
  JOIN Departments AS d ON e.department_id = d.department_id
 ORDER BY e.employee_id;