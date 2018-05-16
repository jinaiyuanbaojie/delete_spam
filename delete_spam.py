#!/usr/bin/python
import os
import random
import shutil
from exchangelib import Credentials, Account

print('Connecting...')
credentials = Credentials('域\邮箱名','密码')
acount = Account('邮箱名@邮箱地址',credentials=credentials, autodiscover=True)
print('Login successfully.')

# 自定义黑名单，邮件主题包含下面的字符串
blackList = ['[JIRA]','[Service Desk Notification]']
for item in acount.inbox.all():
    subject = item.subject
    for blackName in blackList:
        if blackName in subject:
            print(subject)
            item.soft_delete()

print('Jobs done.')
