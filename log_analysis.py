#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect("dbname=news")
cur = conn.cursor()

print("What are the most popular three articles of all time?")
cur.execute("select title as article, count(*) as views from articles \
join log on log.path like '/article/' || articles.slug group by 1 \
order by 2 desc limit 3;")
data = cur.fetchall()
for article in data:
	print(article[0] + " - " + str(article[1]))

print("")

print("Who are the most popular article authors of all time?")
cur.execute("select name as author, count(*) as views from authors \
join articles on authors.id = articles.author join log on \
log.path like '/article/' || articles.slug group by 1 \
order by 2 desc limit 20;")
data = cur.fetchall()
for author in data:
    print(author[0] + " - " + str(author[1]))

print("")

print("On which days did more than 1% of requests lead to errors?")
cur.execute("select day, cast(failed_requests_perc as decimal(16,2)) as \
failed_requests_perc from log_analysis where failed_requests_perc > 1;")
data = cur.fetchall()
for day in data:
    print(str(day[0]) + " - " + str(day[1]) + "%")

conn.close()
