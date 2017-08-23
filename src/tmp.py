from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('Minitable.html'),'html.parser')
ids_collected = []
classes = ['red', 'blue']

def find_by_class(soup, class_name):
    return soup.find_all('td', {'class': class_name})

for cl in classes:
    elems = find_by_class(soup, cl)
    for el in elems:
        ids_collected.append(int(re.sub(r'\D', "", el['onclick'])))

# print ids_collected
# print set(ids_collected)
# print sorted(ids_collected)
print len(ids_collected)