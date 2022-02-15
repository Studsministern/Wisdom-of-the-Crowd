# Wisdom-of-the-Crowd
Project created with PyCharm

Applying the concept of "Wisdom of the Crowd" on a Facebook comment section. This is done to find the average response to guessing competitions which should, in theory, be close to the correct answer. For more information about this subject, see the links below.

The comments are added manually, by inspecting the website and using "Copy outerHTML" on the part of the HTML code that contains all comments. A .html file is then created, containing the HTML code. BeautifulSoup and some filtering is used to find each person's guess. This approach is used in order not to break any of the Facebook web scraping rules listed in [/robots.txt](https://facebook.com/robots.txt). 

# Links
Learned about Wisdom of the Crowd from Daniel Kahneman's book ["Thinking, Fast and Slow"](https://www.amazon.com/Thinking-Fast-Slow-Daniel-Kahneman/dp/0374533555).

More information about Wisdom of the Crowd can be found on Wikipedia: [Wisdom of the Crowd](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd).
