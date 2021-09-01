from json import encoder
import pandas as pd
import snscrape.modules.twitter as sntwitter
import os 

tweets_list = []

def person(username):
    for i,tweet in enumerate(sntwitter.TwitterUserScraper(username, False).get_items()):
        if i>100:
            break
        tweets_list.append({
            "date": tweet.date, "content": tweet.content, "url": tweet.url, "username": tweet.user.username,
            "reply_count": tweet.replyCount, "like_count": tweet.likeCount, "retweet_count": tweet.retweetCount
        })

    df = pd.DataFrame(tweets_list)
    df["date"] = df["date"].replace('')
    df["content"] = df["content"].replace('\n', '', regex=True)

    pwd = os.path.join(os.path.dirname(__file__))
    csv_path = f'{pwd}/tweets.csv'
    df.to_csv(csv_path)


def main(username):
    person(username)