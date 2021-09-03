import pandas as pd
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gspread_dataframe import set_with_dataframe
import os

class Auth():
    # ワークブックまで開く処理
    SP_CREDENTIAL_FILE = "./attendance-1.json"
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    SP_SHEET_KEY = '1lFird1_ulK9IJgkAuNql-TaMRG3RE1ByjOrzBPEix4s'
    
    # herokuから環境変数として取得
    CREDENTIAL = {
        "type": "service_account",
        "project_id": os.environ['PROJECT_ID'],
        "private_key_id": os.environ['PRIVATE_KEY_ID'],
        "private_key": os.environ['PRIVATE_KEY'].replace('\\n', '\n'),
        "client_email": os.environ['CLIENT_EMAIL'],
        "client_id": os.environ['CLIENT_ID'],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ['CLIENT_X509_CERT_URL']
    }

    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(self.CREDENTIAL, self.SP_SCOPE)
        self.gc = gspread.authorize(credentials)

