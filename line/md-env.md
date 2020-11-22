line
- https://developers.line.biz/ja/docs/messaging-api/getting-started/#using-console


アカウントあれば通知できるサービス
- https://notify-bot.line.me/

結構重い。
ウェブフックURLは用意してあるとハンディだった。


開発者アカウント
Your name：aine
Your email：メールアドレス



プロバイダチャネルを作成

プロバイダ名：ainekurainenahatomujiku

ここに開発者アカウントが所属するような感じになる

メッセージングAPIでチャネルを作成

チャネル名：script-sketch-bot

チャネルアイコン

チャネル説明：スクリプトスケッチするボット

カテゴリ名：ウェブサービス

サブカテゴリ名：ウェブサービス（写真・動画）

作成後、チャネルID等が発行されていることが確認できればOK

ボットサーバはline sdkからこしらえる模様。

herokuにボットサーバおいてサーブするURLを用意。

このURLがウェブフックURL。


