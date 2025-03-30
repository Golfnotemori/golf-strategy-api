【Renderでのアップロード手順】

1. https://render.com にアクセスしてアカウント作成
2. New + → Web Service → Deploy from a ZIP file を選択
3. このZIPをアップロード
4. 設定は以下：
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
5. 公開されたURLをコピーして、Bubble.ioのAPI Connectorに登録！
