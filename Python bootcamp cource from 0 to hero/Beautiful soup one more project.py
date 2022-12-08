import requests
import bs4

link = 'http://quotes.toscrape.com/page/{}/'
authors = set()
quotes = set()
for n in range(1, 11):
    consist = requests.get(link.format(n))
    soup = bs4.BeautifulSoup(consist.text, 'lxml')
    all_authors = soup.select('.author')
    all_quotes = soup.select('.text')
    for author in all_authors:
        authors.add(author.text)
    for quote in all_quotes:
        quotes.add(quote.text)

print(authors)
print(quotes)