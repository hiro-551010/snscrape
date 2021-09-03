from json import encoder
from gspread_dataframe import set_with_dataframe
import pandas as pd
import snscrape.modules.twitter as sntwitter
import os 
from .to_sh import Auth

tweets_list = []
count = 1000

def person(username):
    for i,tweet in enumerate(sntwitter.TwitterUserScraper(username, False).get_items()):
        if i>count:
            break
        tweets_list.append({
            "date": tweet.date, "content": tweet.content, "url": tweet.url, "username": tweet.user.username,
            "reply_count": tweet.replyCount, "like_count": tweet.likeCount, "retweet_count": tweet.retweetCount
        })

    df = pd.DataFrame(tweets_list)
    df["date"] = df["date"].replace('')
    df["content"] = df["content"].replace('\n', '', regex=True)

    auth = Auth()
    wb = auth.gc.open_by_key(auth.SP_SHEET_KEY)
    sheet_name = username
    sheet_list = [ws.title for ws in wb.worksheets()]
    if sheet_name in sheet_list:
        wks = wb.worksheet(title=sheet_name)
        set_with_dataframe(wks, df)
        
    else:
        wks = wb.add_worksheet(title=sheet_name, rows=30, cols=100)
        set_with_dataframe(wks, df)

    pwd = os.path.join(os.path.dirname(__file__))
    csv_path = f'{pwd}/tweets.csv'
    df.to_csv(csv_path)


def main(username):
    person(username)

