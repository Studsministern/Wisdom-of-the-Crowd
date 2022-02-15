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
    # Splits on blank spaces (\s), dots (.) and all letters ([a-ö]+)
    comment_text = re.split(r'[\s.]|[a-ö]+', comment.get_text(), flags=re.IGNORECASE)
    comment_numbers = []
    for e in comment_text:
        try:
            comment_numbers.append(int(e))
        except ValueError:
            pass

    # Returns a combination of numbers, if the guess is for example '18.500 st', otherwise just returns the number
    if len(comment_numbers) > 1:
        return int(str(comment_numbers[0]) + str(comment_numbers[1]))
    elif len(comment_numbers) == 1:
        return comment_numbers[0]


def main():
    # Inputs to the program
    url_ending = input('The name of the file (include .html, should be in the \"/examples\" folder): ')
    min_value = input('The lowest allowed guess: ')
    max_value = input('The highest allowed guess: ')

    # Try parsing the inputs
    try:
        min_value = int(min_value)
        max_value = int(max_value)
    except ValueError:
        print('All the value inputs are not integers!')
        return

    # Makes soup of the html page
    url = 'C:/Program Files/GitHub/Wisdom-of-the-Crowd/examples/' + url_ending
    try:
        page = open(url, encoding='utf8')
    except FileNotFoundError:
        print('The file could not be found!')
        return
    soup = BeautifulSoup(page.read(), 'html.parser')

    # Find all the comments (either facebook or instagram, or none of them)
    if 'facebook' in url_ending:
        comments = soup.find_all('div', {'dir': 'auto'})
    elif 'instagram' in url_ending:
        comments = soup.find_all('span', {'class': '_7UhW9 xLCgt MMzan KV-D4 se6yk T0kll'})
    else:
        print('Can\'t find either facebook or instagram content in the file!')
        return

    # Get the numbers from every comment
    lines = []
    for comment in comments:
        number = get_guess(comment)

        # Check so every number contains something and isn't too large or too small
        if number is not None and min_value < number < max_value:
            lines.append(number)

    # Makes a dataframe
    df = pd.DataFrame(lines, columns=['Comment'])
    print(df)

    # Finds the average guess
    average = 0
    for number in lines:
        average += number

    # No division by zero when finding the average
    if len(lines) > 0:
        average /= len(lines)
    else:
        print("Division by zero not allowed.")
        return

    # Printing the answer
    print('Average: ' + str(average))


if __name__ == '__main__':
    main()
