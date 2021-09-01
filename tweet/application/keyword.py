import pandas as pd
import snscrape.modules.twitter as sntwitter
import os

#ツイート検索するキーワード
# search = "松本人志"

# #Twitterでスクレイピングを行い特定キーワードの情報を取得
# scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# #最初の10ツイートだけを取得し格納
# sliced_scraped_tweets = itertools.islice(scraped_tweets, 10)

# #データフレームに変換する
# df = pd.DataFrame(sliced_scraped_tweets)

# df.to_csv("tweet.csv")

tweets_list1 = []
tweets_list = []


def keywords(keyword):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()):
        if i>100:
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
    df.to_csv(csv_path)

def main(keyword):
    keywords(keyword)