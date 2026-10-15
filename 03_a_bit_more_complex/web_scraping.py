import requests
import bs4

r = requests.get("https://openlibrary.org/")
r.raise_for_status()

data = r.text
structure = bs4.BeautifulSoup(data, "html.parser")
title = structure.find("title").text
book_information = structure.find_all("img",class_="bookcover")

def book_info(url_image, book_name):
    return url_image, book_name

my_list = []

for image in book_information:
    url_image = image.get("src")
    if url_image.startswith("data:image"):
        continue
    book_name = image.get("alt")


    my_list.append(book_info(url_image, book_name))

print(title)

for image,name in my_list:
    print("book_cover_URL","http",image,end="    ",sep =":")
    print("book_name_and_author:",name)