from bs4 import BeautifulSoup
import csv
import urllib.request


url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

req = urllib.request.urlopen(url).read()
infy = BeautifulSoup(req,'html.parser')
#print(infy)
references = infy.findAll("sup", {"class": "reference"})
if references:
    for r in references:
        r.extract()


with open("transformed.csv", "w", newline='') as output:
    file = csv.writer(output)
      
    file.writerow(["Game", "Year", "Winning Team", "Score", "Losing Team", "venue"]) 
    table = infy.findAll("table", { "class" : "wikitable" })[1]




    for tablerows in table.findAll("tr"):
        tablecol = tablerows.findAll("td")
        if len(tablecol) == 9:

            Game = str(tablecol[0].get_text(strip=True)).split('!', 1)[1]
            Year = str(tablecol[1].get_text(strip=True)).split(',', 1)[1]
        
            a = str(tablecol[2].get_text(strip=True)).split('!', 1)[0]
            if "X 20" in a:
                continue
            
            WinningTeam = a.strip()
            WinningTeam=WinningTeam[:-2]
                
            
            
            Score = str(tablecol[3].get_text(strip=True)).split('!', 1)[1]
            if ")"in Score:
                p=Score.split('(')
                q=p[0]
                r=p[1]
                r=r[:-1]
                Score=q+r
            Score = Score.strip()
            c = str(tablecol[4].get_text(strip=True)).split('!', 1)[1]
            d = str(c).split('(',1)[0]
            LosingTeam = d[:-1]
            
            
            
            venue = str(tablecol[5].get_text(strip=True)).split('!', 1)[1]
            City = str(tablecol[6].get_text(strip=True))
            Attendence = str(tablecol[7].get_text(strip=True))
            Ref= str(tablecol[8].get_text(strip=True))
            file.writerow([Game, Year, WinningTeam, Score, LosingTeam, venue])

        


   
    
