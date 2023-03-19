-- # write your SQL statement here: 
-- you are given a table 'seven_wonders_science' with columns 'id', 'compasses', 'gears' and 'tablets'
-- return a table with columns 'id', 'compasses', 'gears' and 'tablets' and your result in a column named 'res'


SELECT id, compasses, gears, tablets,
MIN (compasses, gears, tablets) * 7 + (SQUARE(compasses)+SQUARE(gears)+SQUARE(tablets))
AS res
FROM seven_wonders_science

SELECT id,
       compasses,
       gears,
       tablets,
      (LEAST(compasses, gears, tablets) * 7 + POW(compasses, 2) + POW(gears, 2) + POW(tablets, 2))::INT AS res
  FROM seven_wonders_science