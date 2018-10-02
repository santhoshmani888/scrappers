# Web-scrap-using-python
Wikitable scrap

The Super Bowl is an annual American football game that determines the champion of the
National Football League (NFL) . In this assignment, you are given the source file superbowl.html
which is the HTML source code of the whole Wikipedia webpage. This data is in HTML format, and
we would like to transform it into a more usable format. There are few tables in the mentioned web
page; however, the objective is to use python and the BeautifulSoup library to scrape the data from
the second table and save it into a CSV file result.csv . Each line in result.csv should contain 6
fields: Game number, year, winning team, score, losing team, and venue. Note that the number after
every team (and venue) indicates the number of times that the team (or venue) has been in the
Super Bowl.
First, extract relevant portion of superbowl.html . Note that an HTML table is divided into rows with
the <tr> tag, and each row is divided into data cells with the <td> tag. Using the converted HTML file,
write a python script transform.py to pull data out of the relevant HTML portion (second table) and
save it into a CSV file, named result.csv which should match the output shown below. As shown
below, the CSV file headings should match those of the table’s and the rest rows in the file would be
the first 50 rows of the mentioned table on Wikipedia .
