import os

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret')  
    NFS_SHARE_PATH = '/mnt/nfs_share'
    NFS_CLIENT_SHARE_PATH = '/mnt/nfs_clientshare'

