from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
# print(articles)
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
print(article_upvotes)

# find the highest value index
# for v in article_upvotes:
#     high_vote = article_upvotes[0]
#     if v > high_vote:
#         high_vote = v
#     high_vote_index = article_upvotes.index(high_vote)

largest_number =max(article_upvotes)
high_vote_index =article_upvotes.index(largest_number)
print(high_vote_index)

print(f"The highest voted title is: {article_texts[high_vote_index+1]}")
print(f"The highest voted title link is: {article_links[high_vote_index+1]}")
print(f"The highest votes is: {article_upvotes[high_vote_index]}")

print(len(article_upvotes))
print(len(article_texts))
print(len(article_links))



# import lxml

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText()) prints the text
#     # to print or get the link/href
#     print(tag.get("href"))
#
# heading =soup.find(name="h1", id="name")
# print(heading)
#
# section_head =soup.find(name="h3", class_="heading") #class_ so that it dont clash with "class" that is a reserved word to create class
# print(section_head.get("class"))
#
# company_url =soup.select_one(selector="p a")
# print(company_url)
#
# name =soup.select_one(selector="#name") #select an id use #
# print(name)
#
# headings = soup.select(".heading") # . for getting class
# print(headings)
