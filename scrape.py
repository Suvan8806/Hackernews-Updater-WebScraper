import requests
from bs4 import BeautifulSoup
import pprint

#use .titleline instead of .storylink
#href is the link

def get_page_data(page):
    url = f'https://news.ycombinator.com/news?p={page}'
    res = requests.get(url) #gives you the document itself
    soup = BeautifulSoup(res.text, 'html.parser')# soup object!, now tis just html 
    links = soup.select('.titleline > a')# got .titleline by going to webiste, using inspect
    subtext = soup.select('.subtext') # got .score by going to the website. using inspect
    return links, subtext

def time_since_posted(subtext_item):
    time_text = subtext_item.select('.age > a')[0].getText()
    if 'hour' in time_text or 'hours' in time_text:
        return int(time_text.split()[0]) < 24  # Check if less than 24 hours
    elif 'minute' in time_text or 'minutes' in time_text:
        return True  # All minutes are within 24 hours
    elif 'day' in time_text or 'days' in time_text:
        return int(time_text.split()[0]) < 1  # Check if less than 1 day
    return False

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['Comments + Votes'], reverse=True)

def create_custom_hn():
    pages = 10
    hn = []
    for page in range(1, pages + 1):
        links, subtext = get_page_data(page)
        for idx, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None) #href is the link you get from the html code
            vote = subtext[idx].select('.score')
            comments = subtext[idx].select('a')[-1].getText()  # Get the last link in subtext for comments
            
            # Handle comment count extraction
            if 'comment' in comments:
                comment_count = int(comments.split()[0])  # Extract number of comments
            else:
                comment_count = 0  # No comments

            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                aggregate = points + int(comment_count)

                if points > 99 and time_since_posted(subtext[idx]): # Checks if over 99 votes and within 24 hours
                    hn.append({'title': title, 'link': href, 'votes': points, 'comments': comment_count, 'Comments + Votes': aggregate})
    return sort_stories_by_votes(hn)[:10]

# Specify the number of pages to scrape
#pprint.pprint(create_custom_hn())