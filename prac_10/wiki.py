"""
CP1404
Simple program that asks the user to search in wikipedia
and returns a summary of that page
Lukas Arnold
"""

import wikipedia


phrase = input("\nWhat would you like to search on Wikipedia?")

while phrase != " ":
    try:
        web_page = wikipedia.page(phrase)
        print("Title: {}".format(web_page.title))
        print("Summary: {}".format(web_page.content))
        print("URL: {}".format(web_page.url))

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    phrase = input("\nWhat would you like to search on Wikipedia?")

