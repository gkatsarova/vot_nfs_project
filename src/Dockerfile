FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV JWT_SECRET_KEY=your_secret_key
ENV NFS_SHARE_PATH=/mnt/nfs_share

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
