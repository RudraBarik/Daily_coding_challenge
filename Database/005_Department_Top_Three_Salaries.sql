-- Department Top Three Salaries (HARD)
-- https://leetcode.com/problems/department-top-three-salaries/

/*The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
Explanation:

In IT department, Max earns the highest salary, both Randy and Joe earn the second highest salary, and Will earns the third highest salary. There are only two employees in the Sales department, Henry earns the highest salary while Sam earns the second highest salary. */

-- Write your MySQL query statement below
SELECT d.Name as 'Department', e1.Name as 'Employee', e1.Salary 
FROM Employee e1
JOIN Department d 
ON e1.DepartmentId = d.Id
WHERE 
    3 > (SELECT count(distinct (e2.Salary)) 
           from Employee e2
           where e2.Salary > e1.Salary
           and e1.DepartmentId = e2.DepartmentId
          );

/*Output:
{"headers": ["Department", "Employee", "Salary"], "values": [["IT", "Joe", 85000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000], ["IT", "Max", 90000], ["IT", "Randy", 85000], ["IT", "Will", 70000]]}*/