# ZillowDBProject
Hello! Welcome to my version of a Zillow Database! To access the database please follow the steps below

Have latest version of Postgres downloaded onto your machine

Open up your local command line and paste link below to access AWS hosted database:

psql -h zillow.cfnpydopbn5f.us-east-2.rds.amazonaws.com -p 5432 -U postgres


user password: zillow123

from here you can access and manipulate database however you please; below are some queries I have created: 

select mortgages.userid, mortgages.loanamount, mortgages.rateamount from mortgages where userid=23534;

select state, avg(mortgages.rateamount) as average_rate from mortgages inner join
states s on mortgages.stateid = s.id group by  state;

select houseid, userid, price from savedhouses inner join houses h on public.savedhouses.houseid = h.id
where price < 500000 and stateid=25 order by price desc;

select count(agentreviews.comments), name from agentreviews left outer join
agents a on agentreviews.agentid = a.id group by name;

QUERY EXPLANATIONS: 

The first query was to find all loan amounts and rates made by a specific user using his id.

The second query to me was the most interesting was to find the average rate for a mortage within each state then grouping them by each state's number. 

The third query was to find all houses saved by users that cost less than $500000 and within the state of Missouri.

The last query I used to count agent reviews and see which agent had the most reviews on them and to group them by their first name. 

