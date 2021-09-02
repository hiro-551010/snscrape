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
        tweets_list.append([
            tweet.date, tweet.content, tweet.url, tweet.user.username, tweet.replyCount,
            tweet.likeCount, tweet.retweetCount
            ])

    df = pd.DataFrame(tweets_list, columns=[
            "tweet_date", "tweet_content", "tweet_url", "tweet_user_name", "tweet_reply_count",
            "tweet_like_count", "tweet_retweet_count"
        ])

    pwd = os.path.join(os.path.dirname(__file__))
    csv_path = f"{pwd}/tweets.csv"
    df["tweet_content"] = df["tweet_content"].replace('\n', '', regex=True)
    df.to_csv(csv_path)

def main(keyword, since, until):
    keywords(keyword, since, until)
    

