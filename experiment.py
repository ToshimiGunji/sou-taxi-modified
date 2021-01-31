import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# SCOPES = ['https://spreadsheets.google.com/feeds',
#           'https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = "sou-taxi-project-d2a843809101.json"
# credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
# gc = gspread.authorize(credentials)
# SPREADSHEET_KEY = "16OD2Rv51rAMy-UPChHTsuoQQADm-huMt-9QTSKaDHy0"
#
# workbook = gc.open_by_key(SPREADSHEET_KEY)
# worksheet = workbook.worksheet("シート1")
# # worksheet_list = workbook.worksheets()
# # worksheet = gs.open_by_key(SPREADSHEET_KEY).worksheet("シート1")
# worksheet.update_acell("A3", str(datetime.now()))
while True:
    # 乗車コマンド
    start = input("乗車")
    if start == "乗車":
        get_on_time = datetime.now()
        print(get_on_time)
        # 降車コマンド
        while True:
            finish = input("降車、またはキャンセル")
            if finish == "降車":
                get_off_time = datetime.now()
                print(get_off_time)
                # 利用時間の算出
                time_dif = get_off_time - get_on_time
                all_secs = time_dif.seconds
                m, n = divmod(all_secs, 60)
                print("\n利用時間は{0}分{1}秒でした".format(m, n))
                break
            elif finish == "キャンセル":
                direct_input = input("だいたいの乗車分数を入力してください")
                print("\n乗車時間は{0}分0秒でした".format(direct_input))
                break
            else:
                print("有効なコマンドではありません")
                continue
        break
    else:
        print("有効なコマンドではありません")
        continue
