import requests
from bs4 import BeautifulSoup
import praw
import config
import time
import os

def bot_login():
    print("Signing in...")
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Urban Bot")

    print("Sign in complete.")

    return r

def run_bot(r, comments_replied_to):
    print("Searching through the last 1000 comments...")
    for comment in r.subreddit('test').comments(limit=1000):
        if "!urban" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("Comment found containing \"!urban\" with id: " + comment.id)
            keyword = comment.body[7:]
            target_url = "https://www.urbandictionary.com/define.php?term=" + keyword
            response = run_scraper(target_url)
            comment.reply("**" + keyword + ":** " + response + "\n\n###### Definition provided by [urbandictionary.com](https://www.urbandictionary.com/).")
            print("Replied to comment with id: " + comment.id)
            comments_replied_to.append(comment.id)
            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Search completed.")
    print(comments_replied_to)
    print("Sleeping for 10 seconds...")
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
    
    return comments_replied_to

def run_scraper(target_url):
    r = requests.get(target_url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"})
    if r.status_code == 200:
        print("Running web scraper...")
    else:
        r.raise_for_status()
    
    soup = BeautifulSoup(r.text, "html.parser")
    summary = soup.find(class_="meaning").get_text()
    
    return summary

#initialize the bot
r = bot_login()
comments_replied_to = get_saved_comments()

print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)
