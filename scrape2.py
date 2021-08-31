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

f = open("tweets.csv", "w")
j = json.dumps(tweets_list, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
f.write(j)
f.close()
# df = pd.DataFrame(tweets_list)
# df.to_csv("tweets.csv")
