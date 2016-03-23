---
title: SQLZoo 题目参考代码
layout: post
date: 2016-03-20
categories: SQL
---

# SQLZOO:SELECT basics

## 1

```
select population from world where name='Germany'
```

## 2

```
select name, gdp/population from world where area > 5000000
```

## 3

```
select name, population from world
    where name in ('Ireland', 'Iceland', 'Denmark')
```

## 4

```
SELECT name,
       area
FROM   world
WHERE  area BETWEEN 200000 AND 250000
```

# SQLZOO:SELECT from WORLD Tutorial

## 1

``
SELECT name, continent, population FROM world
```

## 2

```
SELECT name
FROM   world
WHERE  population >= 200000000
```

## 3

```
SELECT name,
       gdp / population
FROM   world
WHERE  population >= 200000000
```

## 4

```
SELECT name,
       population / 1000000
FROM   world
WHERE  continent IN ( 'South America' )
```

## 5

```
SELECT name,
       population
FROM   world
WHERE  name IN ( 'France', 'Germany', 'Italy' )
```

## 6

```
SELECT name
FROM world
WHERE name LIKE '%United%'
```
## 7

```
SELECT name,
       population,
       area
FROM   world
WHERE  area >= 3000000
        OR population > 250000000
```

## 8

```
SELECT name, population, area
FROM world
WHERE (area >= 3000000
		OR population > 250000000)
	AND NOT area >= 3000000
	AND population > 250000000
```

## 9

```
SELECT name, ROUND(population / 1000000, 2), ROUND(GDP / 1000000000, 2)
FROM world
WHERE continent = 'South America'
```

## 10

```
SELECT name, round(gdp / population, -3)
FROM world
WHERE GDP >= 1000000000000
```

## 11

```
SELECT name, CASE WHEN continent = 'Oceania' THEN 'Australasia' ELSE continent END
FROM world
WHERE name LIKE 'N%'
```

## 12

```
SELECT name,
       CASE
         WHEN continent IN ( 'Europe', 'Asia' ) THEN 'Eurasia'
         WHEN continent IN ( 'North America', 'South America', 'Caribbean' ) THEN 'America'
         ELSE continent
       END
FROM   world
WHERE  name LIKE 'A%'
        OR name LIKE 'B%'
```

## 13

```
SELECT name,
       continent,
       CASE
         WHEN continent IN ( 'Eurasia', 'Turkey' ) THEN 'Europe/Asia'
         WHEN continent = 'Oceania' THEN 'Australasia'
         WHEN continent = 'Caribbean' THEN
           CASE
             WHEN name like 'B%' THEN 'North America'
             ELSE 'South America'
           END
else continent
       END
FROM   world
ORDER  BY name ASC
```
# SELECT from Nobel Tutorial

## 1

```
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1950
```

## 2

```
SELECT winner
  FROM nobel
 WHERE yr = 1962
   AND subject = 'Literature'
```

## 3

```
SELECT yr, subject
FROM nobel
WHERE winner = 'Albert Einstein'
```

## 4

```
SELECT winner
FROM nobel
WHERE yr >= 2000
	AND subject = 'Peace'
```

## 5

```
SELECT yr, subject, winner
FROM nobel
WHERE subject = 'Literature'
	AND yr BETWEEN 1980 AND 1989
```

## 6

```
SELECT *
FROM nobel
WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter')
```

## 7

```
SELECT winner
FROM nobel
WHERE winner LIKE 'John %'
```

## 8

```
SELECT *
FROM nobel
WHERE yr = 1984
	AND subject = 'Chemistry'
	OR yr = 1980
	AND subject = 'Physics'
```

## 9

```
SELECT *
FROM nobel
WHERE yr = 1980
	AND subject NOT IN ('Chemistry', 'Medicine')
```

## 10

```
SELECT *
FROM nobel
WHERE yr < 1910
	AND subject = 'Medicine'
	OR yr >= 2004
	AND subject = 'Literature'
```

## 11
```
SELECT *
FROM nobel
WHERE winner = 'Peter Grünberg'
```

## 12

```
SELECT *
FROM nobel
WHERE winner = 'Eugene O''neill'
```

## 13

｀｀｀
SELECT winner, yr, subject
FROM nobel
WHERE winner LIKE 'sir%'
ORDER BY yr DESC, winner ASC
｀｀｀

## 14

```
SELECT winner, subject
FROM nobel
WHERE yr = 1984
ORDER BY subject IN ('Chemistry', 'Physics') ASC, subject, winner
```
# SELECT within SELECT Tutorial


## 1

```
SELECT name
FROM world
WHERE population > (
	SELECT population
	FROM world
	WHERE name = 'Russia'
	)
```

## 2

```
SELECT name
FROM world
WHERE gdp / population > (
		SELECT gdp / population
		FROM world
		WHERE name = 'United Kingdom'
		)
	AND continent = 'Europe'
```

## 3

```
SELECT name, continent
FROM world
WHERE continent IN (SELECT continent
	FROM world
	WHERE name IN ('Argentina', 'Australia'))
ORDER BY name
```

## 4

```
SELECT name, population
FROM world
WHERE population BETWEEN (
	SELECT population + 1
	FROM world
	WHERE name = 'Canada'
	) AND (
	SELECT population - 1
	FROM world
	WHERE name = 'Poland'
	)
```

## 5

```
SELECT name, CONCAT(round(100 * population / (
		SELECT population
		FROM world
		WHERE name = 'Germany'
		), 0), '%')
FROM world
WHERE continent = 'Europe'
```

## 6

```
SELECT name
FROM world
WHERE gdp > ALL (SELECT gdp
	FROM world
	WHERE gdp > 0
		AND continent = 'Europe')
```

## 7

```
SELECT continent, name, area
FROM world x
WHERE area >= ALL (SELECT area
	FROM world y
	WHERE x.continent = y.continent
		AND area > 0)
```

## 8

```
SELECT continent, name
FROM world x
WHERE name <= ALL (SELECT name
	FROM world y
	WHERE x.continent = y.continent
	ORDER BY name ASC)
```

## 9

```
SELECT population
FROM world y
WHERE world.continent = y.continent
```

## 10

```
SELECT name, continent
FROM world x
WHERE population / 3 > ALL (SELECT population
	FROM world y
	WHERE x.continent = y.continent
		AND x.name != y.name)
```

# SUM and COUNT

## 2

```
SELECT DISTINCT continent
FROM world
```

## 3

```
SELECT SUM(gdp)
FROM world
WHERE continent = 'Africa'
```

## 4

```
select count(*) from world where area >= 1000000
```

## 5

```
SELECT SUM(population)
FROM world
WHERE name IN ('France', 'Germany', 'Spain')
```

## 6

```
SELECT continent, COUNT(name)
FROM world
GROUP BY continent
```

## 7

```
SELECT continent, COUNT(name)
FROM world
WHERE population >= 10000000
GROUP BY continent
```

## 8

```
SELECT continent
FROM world
GROUP BY continent
HAVING SUM(population) > 100000000
```

# The JOIN operation

## 2

```
SELECT DISTINCT id, stadium, team1, team2
FROM goal, game
WHERE goal.matchid = '1012'
	AND goal.matchid = game.id
```


## 3

```
SELECT player, teamid, stadium, mdate
FROM game JOIN goal ON goal.teamid = 'GER'
AND goal.matchid = game.id
```

## 4

```
SELECT team1, team2, player
FROM game JOIN goal ON goal.player LIKE 'Mario%'
AND goal.matchid = game.id
```

## 5

```
SELECT player, teamid, coach, gtime
FROM goal JOIN eteam ON eteam.id = goal.teamid
AND goal.gtime <= 10
```

## 6

```
SELECT mdate, teamname
FROM game JOIN eteam ON eteam.coach = 'Fernando Santos'
AND game.team1 = eteam.id
```

## 7

```
SELECT player
FROM game JOIN goal ON stadium = 'National Stadium, Warsaw'
AND matchid = id
```

## 8

```
SELECT DISTINCT player
FROM game JOIN goal ON matchid = id
AND teamid != 'GER'
AND (team1 = 'GER'
	OR team2 = 'GER')
```

## 9

```
SELECT teamname, COUNT(*)
FROM goal JOIN eteam ON teamid = id
GROUP BY teamname
``

## 10

```
SELECT stadium, COUNT(*)
FROM goal JOIN game ON matchid = id
AND (teamid = team1
	OR teamid = team2)
GROUP BY stadium
```

## 11

```
SELECT matchid, mdate, COUNT(*)
FROM game JOIN goal ON matchid = id
AND team1 = 'POL'
OR team2 = 'POL'
AND id = matchid
GROUP BY matchid
```

## 12

```
SELECT matchid, mdate, COUNT(*)
FROM goal JOIN game ON matchid = id
AND teamid = 'GER'
GROUP BY matchid
```

# More JOIN operations

## 7

```
SELECT name
FROM actor JOIN casting ON actorid = id
WHERE movieid = 11768
```

## 8

```
SELECT name
FROM movie JOIN casting ON movieid = movie.id JOIN actor ON actor.id = actorid
WHERE title = 'Alien'
```

## 9

```
SELECT title
FROM casting JOIN actor ON actor.id = actorid JOIN movie ON movie.id = movieid
WHERE name = 'Harrison Ford'
```

## 11

```
SELECT title, name
FROM movie JOIN casting ON movie.id = movieid
AND ord = 1 JOIN actor ON actor.id = actorid
WHERE yr = 1962
```

## 12

```
SELECT yr, COUNT(1)
FROM actor JOIN casting ON id = actorid JOIN movie ON movie.id = movieid
WHERE name = 'John Travolta'
GROUP BY yr
HAVING COUNT(1) > 2
```

## 13

```
SELECT title, name
FROM actor JOIN casting ON id = actorid JOIN movie ON movie.id = movieid
WHERE movieid IN (SELECT movieid
		FROM actor JOIN casting ON id = actorid JOIN movie ON movie.id = movieid
		WHERE name = 'Julie Andrews')
	AND ord = 1
```

## 14

```
SELECT name
FROM movie JOIN casting ON movieid = id JOIN actor ON actor.id = actorid
WHERE ord = 1
GROUP BY name
HAVING COUNT(1) >= 30
ORDER BY name
```

## 15

```
这里已经没错了，但是标准答案给出的排序条件不完全，所以一直对不上。

SELECT title, COUNT(1)
FROM movie JOIN casting ON id = movieid
WHERE yr = 1978
GROUP BY movieid
ORDER BY COUNT(1) DESC
```

## 16

```
SELECT DISTINCT name
FROM movie JOIN casting ON id = movieid JOIN actor ON actorid = actor.id
WHERE movieid IN (SELECT movieid
		FROM movie JOIN casting ON id = movieid JOIN actor ON actorid = actor.id
		WHERE name = 'Art Garfunkel')
	AND name != 'Art Garfunkel'
```




