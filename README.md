# Data-Analysis-Pipeline
The goal of this project is to compare the results of the last 30 years of a soccer national team with its corresponding current ranking FIFA. 

To get the results of the last 30 years I took a database from kaggle (https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017) with all the results since the XIX century and have selected only those results from 1990 including only the games of the tournaments that are recognized by the FIFA organization.

I have cleaned the database and have made a function to assign points to the national teams depending on the score of the game, then I had to split the database in two with the mean of the points they get by match, one database for the local teams and another one for the away teams and merge it into a new database. I have sumed the means of the home and away results and ranked the teams according to the results of the sum.

To compare this database with the ranking FIFA I had to do web scrapping in the web page of FIFA organization (https://www.fifa.com/fifa-world-ranking/ranking-table/men/) to get the current ranking FIFA.

To get the result of the comparation there is only one argument (country) in capital letters, in the terminal you can write the country name after the command (--country) and the pipeline will return the ranking of the national team during the last 30 years and the current ranking in the FIFA clasification.
