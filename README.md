# Data-Analysis-Pipeline
The goal of this project is to compare the results of two soccer national team during the last 30 years with their current ranking FIFA. 

To get the results of the last 30 years I took a database from kaggle (https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017) with all the international results since the XIX century and have excluded all those results previous to 1990 including only the games of the tournaments that are recognized by the FIFA organization.

I have cleaned the database and have made a function to assign points to the national teams depending on the score of the game, then I had to split the database in two databases with the average of the points they get by match, one database for the local teams and another one for the away teams and merge it into a new database. Then, I have sumed the averages of the home and away results and ranked the teams according to the results of the sum.

To compare this database with the ranking FIFA I had to do web scraping in the official web page of FIFA organization (https://www.fifa.com/fifa-world-ranking/ranking-table/men/) to get the current ranking FIFA.

To get the result of the comparison there is two arguments (country1, country2) in capital letters, in the terminal you can write the first country name after the command (--c1) and the second country after the command(--c2) and the pipeline will return the ranking of the two national teams during the last 30 years and their current ranking in the FIFA clasification.

The structure of the repository is the following:
- Input: Where is the original database from Kaggle.
- Pruebas: Folder where are the jupyter notebooks I have used to check the output of the functions.
- src: Folder where are all the functions I have used in the project.
- main: The program to use in terminal and look for the output.