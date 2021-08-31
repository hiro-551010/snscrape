from json import encoder
import pandas as pd
import snscrape.modules.twitter as sntwitter
import json

tweets_list = []

for i,tweet in enumerate(sntwitter.TwitterUserScraper("matsu_bouzu", False).get_items()):
    if i>100:
        break
    # tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.url,\
    #                     tweet.user.username, tweet.user.followersCount,tweet.replyCount,\
    #                     tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.lang,\
    #                     tweet.outlinks, tweet.media, tweet.retweetedTweet, tweet.quotedTweet,\
    #                     tweet.inReplyToTweetId, tweet.inReplyToUser, tweet.mentionedUsers,\
    #                     tweet.coordinates, tweet.place, tweet.hashtags, tweet.cashtags])
    tweets_list.append({
        "content": tweet.content, "url": tweet.url, "username": tweet.user.username,
        "reply_count": tweet.replyCount, "like_count": tweet.likeCount, "retweet_count": tweet.retweetCount})


df = pd.DataFrame(tweets_list)
df["content"] = df["content"].replace('\n', '', regex=True)
df.to_csv("tweets2.csv")
