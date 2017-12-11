This program uses the authors, articles and log tables in the news database to analyze data and answer the following 3 questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

Steps to run this program and see it's result:

Clone this Repository on your local computer
Go to the project directory
Run the statement "python3 log_analysis.py"

The news database contains a view which was created as follows:

create view log_analysis
as
select
date_trunc('day',time) as day
, count(*) as total_requests
, sum(case when status = '404 NOT FOUND' then 1 else 0 end) as failed_requests
, sum(case when status = '200 OK' then 1 else 0 end) as succeeded_requests
, sum(case when status = '404 NOT FOUND' then 1 else 0 end)::float / count(*)::float * 100 as failed_requests_perc
, sum(case when status = '200 OK' then 1 else 0 end)::float / count(*)::float * 100 as succeeded_requests_perc
from log 
group by 1
;
