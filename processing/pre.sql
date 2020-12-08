-- duplication reduction
DELETE FROM userbehavior WHERE (user,item,category,behavior,time)
IN 
(SELECT user,item,category,behavior,time 
	FROM (SELECT user,item,category,behavior,time 
				FROM userbehavior 
				GROUP BY user,item,category,behavior,time 
				HAVING COUNT(*)>1) s1) 
AND id NOT IN (SELECT id FROM 
							(SELECT id FROM userbehavior 
												 GROUP BY user,item,category,behavior,time 
												 HAVING COUNT(*)>1) s2);
-- missing valuse reduction
SELECT count(user),count(item),count(category),count(behavior),count(time) FROM userbehavior;

-- abnormal values reduction
DELETE FROM userbehavior where time >'1512230400' or Date <'1511539200';
