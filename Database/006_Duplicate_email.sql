/*Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
*/

select Email from(
select count(*),Email from Person group by Email having count(*) > 1
) P

/*Runtime: 187 ms, faster than 72.77% of MySQL online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
*/

