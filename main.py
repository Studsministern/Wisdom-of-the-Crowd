from bs4 import BeautifulSoup
import requests
import csv
import re
import pandas as pd


def get_guess(comment):
    """
    Find the number from a certain comment
    :param comment: html comment
    :return: the integer found in the comment
    """
    comment_text = re.split(r'[\s.]|st', comment.get_text())
    comment_numbers = []
    for e in comment_text:
        try:
            comment_numbers.append(int(e))
        except ValueError:
            pass

    if len(comment_numbers) > 1:
        return int(str(comment_numbers[0]) + str(comment_numbers[1]))
    elif len(comment_numbers) == 1:
        return comment_numbers[0]


def main():
    # Makes soup of the html page
    url = 'C:/Program Files/GitHub/Wisdom-of-the-Crowd/facebook_data.html'
    page = open(url, encoding='utf8')
    soup = BeautifulSoup(page.read(), 'html.parser')

    # Find all the comments
    comments = soup.find_all('div', {'dir': 'auto'})

    # Get the numbers from every comment
    lines = []
    for comment in comments:
        number = get_guess(comment)
        # Check so every number contains something and isn't too large or too small
        if number is not None and 300000 > number > 1000:
            lines.append(number)

    # Makes a dataframe
    df = pd.DataFrame(lines, columns=['Comment'])
    print(df)

    # Finds the average guess
    average = 0
    for number in lines:
        average += number
    average /= len(lines)
    print('Average: ' + str(average))


if __name__ == '__main__':
    main()
