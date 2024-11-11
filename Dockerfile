# 使用するPythonのバージョン
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
COPY . .

# プロトコルファイルからPythonクラスを生成
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto

# サーバーを起動するコマンド
CMD ["python", "server.py"]

