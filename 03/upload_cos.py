# -*- coding: utf-8 -*-
# auther: Joe wen

import os, sys, time, re, json, urllib
from datetime import datetime, timedelta
from qcloud_cos import CosClient, UploadFileRequest, StatFileRequest, ListFolderRequest, DelFileRequest,DelFolderRequest, CreateFolderRequest

appid = "1251180962"
secret_id = u'AKID9Bg4HI4kBSXQ7ev85vZ0JTSFrHVXq1Sm'
secret_key = u'HOJ2ZuujLlySnw8PbdT9duyqY9YmoeIw'
region_info = 'gz'
bucket = u'backup'
# remotepath = u'/user.txt'
# localpath = u'/user.txt'
# remotefolder = '/abab/'
#localpath = u'/Users/joe/Documents/tutory_python/03/'

allfolder_name = []
allfile_name = []


def screendir(filepath):
    for alldir in os.listdir(filepath):
        child = os.path.join(filepath, alldir)
        if os.path.isdir(child):
            allfolder_name.append(child)
            screendir(child)
        else:
            allfile_name.append(child)
    return allfolder_name, allfile_name
    # print(child.decode('utf8'))

def Uploadfile(cos_client,bucket,remotepath,localpath):
    request = UploadFileRequest(bucket, remotepath, localpath)
    request.set_insert_only(0)  #0是允许覆盖 1是不允许
    upload_file_ret = cos_client.upload_file(request)
    #print(upload_file_ret['message'])
    if upload_file_ret['message'] == u'SUCCESS':
        print(localpath.encode('utf8') + '上传成功')
    elif upload_file_ret['message'] == u'ERROR_CMD_BUCKET_NOTEXIST':
        print('bucket错误，请重新检查bucker名称')
    elif upload_file_ret['message'] == u'ERROR_PROXY_AUTH_APPID':
        print('APPID错误')
    elif upload_file_ret['message'] == u'PROXY_AUTH_SECRETID_NOEXIST':
        print('secret_id错误')
    elif upload_file_ret['message'] == u'ERROR_PROXY_AUTH_FAILED':
        print('secret_key错误')
    else:
        print('other error')

def Createfolder(cos_client,bucket,remotefolder):
    request = CreateFolderRequest(bucket,remotefolder)
    create_folder_ret = cos_client.create_folder(request)
    #print(repr(create_folder_ret['message']))
    if create_folder_ret['message'] == u'SUCCESS':
        print('创建目录成功')
    elif create_folder_ret['message'] == u'ERROR_CMD_COS_PATH_CONFLICT':
        print('目录已存在')
    else:
        print('创建失败')


filepath = "/Users/joe/Downloads/test"
filepath_len = len(filepath)

screendir(filepath)

#print(allfolder_name, allfile_name)
#folder_len = len(allfolder_name) -1


cos_client = CosClient(int(appid), secret_id, secret_key, region=region_info)

for remotefolder in allfolder_name:
    folder_abs = os.path.join(filepath,remotefolder)
    remotefolder = remotefolder[filepath_len:] + '/'
    if folder_abs in allfolder_name:
        Createfolder(cos_client, bucket, unicode(remotefolder))

for remotepath in allfile_name:
    localpath = remotepath
    file_abs = os.path.join(filepath,remotepath)
    remotepath = remotepath[filepath_len:]

    if file_abs in allfile_name:
        Uploadfile(cos_client,bucket,unicode(remotepath),unicode(localpath))

