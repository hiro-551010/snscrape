from json import encoder
from gspread_dataframe import set_with_dataframe
import pandas as pd
import snscrape.modules.twitter as sntwitter
from .to_sh import Auth

tweets_list = []
count = 1000

def person(username):
    for i,tweet in enumerate(sntwitter.TwitterUserScraper(username, False).get_items()):
        if i>count:
            break
        tweets_list.append([
            tweet.date, tweet.content, tweet.url, tweet.user.displayname, tweet.replyCount,
            tweet.likeCount, tweet.retweetCount,
        ])

    df = pd.DataFrame(tweets_list, columns=["日付", "内容", "url", "ユーザー名", "リプライ数", "いいね数", "リツイート数"])
    df["内容"] = df["内容"].replace('\n', '', regex=True)

    auth = Auth()
    wb = auth.gc.open_by_key(auth.SP_SHEET_KEY)
    sheet_name = df["ユーザー名"][0]
    sheet_list = [ws.title for ws in wb.worksheets()]
    if sheet_name in sheet_list:
        wks = wb.worksheet(title=sheet_name)
        set_with_dataframe(wks, df)   
    else:
        wks = wb.add_worksheet(title=sheet_name, rows=30, cols=100)
        set_with_dataframe(wks, df)

def main(username):
    person(username)

