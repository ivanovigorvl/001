import bs4  
import requests  
      
#парсинг статьи из википедии про арифмометр "Феликс"
#https://ru.wikipedia.org/wiki/Феликс_(арифмометр)

#1. Печатаем название страницы
#2. Получаем все ссылки на странице
#3.Запись полученных данных в файл "parsing.txt"


res = requests.get("https://ru.wikipedia.org/wiki/Феликс_(арифмометр)")  
print("The object type:",type(res))  
      
# Convert the request object to the Beautiful Soup Object  
soup = bs4.BeautifulSoup(res.text,'html5lib')  
print("The object type:",type(soup) )
print(soup.title.text) #печатаем название страницы

soup.select('.mw-headline') 
for i in soup.select('.mw-headline'): 
    print(i.text,end = ',')

for link in soup.find_all("a"): #получаем все ссылки на странице
    print("Inner Text is: {}".format(link.text)) 
    print("Title is: {}".format(link.get("title"))) 
    print("href is: {}".format(link.get("href"))) 


#запись полученных данных в файл "parsing.txt"

filename = "parsing.txt"  
f = open(filename,"w")  

with open("parsing.csv", "w") as file:      
    for link in soup.find_all("a"):
        f.write('%s\n' %link)
      
f.close()
