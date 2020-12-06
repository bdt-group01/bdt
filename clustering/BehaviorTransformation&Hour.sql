SELECT 
(CASE 
	WHEN f4 = 'pv' then 1
	WHEN f4 = 'buy' then 2
	WHEN f4 = 'cart' then 3
	WHEN f4 = 'fav' then 4
	ELSE 5
	END),
FROM_UNIXTIME(f5,'%H')
FROM
userBehavior;