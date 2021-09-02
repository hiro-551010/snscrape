import pandas as pd
import snscrape.modules.twitter as sntwitter
import os
import asyncio

tweets_list1 = []
tweets_list = []
count = 1000

def keywords(keyword, since, until):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} since:{since} until:{until}').get_items()):
        if i>count:
            break
        tweets_list.append({
            "date": tweet.date, "content": tweet.content, "url": tweet.url, "username": tweet.user.username,
            "reply_count": tweet.replyCount, "like_count": tweet.likeCount, "retweet_count": tweet.retweetCount
        })

    df = pd.DataFrame(tweets_list)
    
    pwd = os.path.join(os.path.dirname(__file__))
    csv_path = f"{pwd}/tweets.csv"
    df["content"] = df["content"].replace('\n', '', regex=True)
    df.to_csv(csv_path)

def main(keyword, since, until):
    keywords(keyword, since, until)
    

