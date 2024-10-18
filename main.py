from request import req
from count_words import capybara
page=req('https://ru.wikipedia.org/wiki/Капибара')
page=capybara('Капибара', page)
print(page)