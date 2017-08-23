from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('Minitable.html'),'html.parser')
onclick = soup.findAll('td', onclick=True)
for elm in onclick:
    match = re.search(r"showgoallist\(([0-9]+)\)", str(elm))
    print match.group(1)
