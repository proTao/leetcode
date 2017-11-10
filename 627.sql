select id, name, 'f' as sex, salary from salary where sex = 'm' 
union 
select id, name, 'm' as sex, salary from salary where sex = 'f';