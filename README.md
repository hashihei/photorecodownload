# photorecodownload
## Name
photorecodownload
* フォトレコから画像を一括ダウンロードするスクリプト

## Requirement
* python python3.8.x
    * 動作確認バージョンWindows(python 3.8.1)

* chrome
    * 動作確認バージョン 83.0.4103.116

* chromedriver
    * 動作確認バージョン　84.0.4147.30
    * https://chromedriver.chromium.org/downloads

* selenium

## Usage
* Windows Install (Use PowerShell)
```
git clone xxx
```

* Configure
    1. etc/login.conf
        * [MUST]
            * ダウンロード画像枚数
                NOS = 100
            * ログインユーザID
                USER = 152*****
            * ログインパスワード
                PASS = sample@gmail.com
            * photoreco ログインURL
                LOGIN_URL = https://www.photoreco.com/login/
                

* Execution
```
cd .\photorecodownload\
python main.py
```

## Author
hashihei

## Note
None.
