# -*- coding: utf-8 -*-
#auther: Joe wen

import os,sys,time,re,json,urllib
from datetime import datetime,timedelta
from qcloud_cos import CosClient,UploadFileRequest,StatFileRequest,ListFolderRequest,DelFileRequest,DelFolderRequest,CreateFolderRequest

# Draw title with Frame
def drawTitle(string):
	width = (len(string)+len(string.decode('utf-8')))/2
	hr = '─'*(width+10)
	print '\n┌%s┐\n│ >>> %s <<< │\n└%s┘'%(hr,string,hr)
# Print format JSON
def formatJSON(obj,indent=4):
	return json.dumps(obj,encoding="UTF-8", ensure_ascii=False,indent=indent)

def readLocalFiles(root,subFolder=u''):
    start = datetime.now()
    drawTitle('Reading local file')