# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:08:43 2019

@author: sissy
"""
import re
address=open(r'C:\Users\sissy\Desktop\test Git\IBI1_2018-19\Practical6\address_information.csv','r')
r=[]
for line in address:
    fields=line.split(r',')
    if (len(fields)>1):
        if re.match(r'(\S+)@(\S+)',fields[1]):
            if not '.com' in fields[1]:
                print(fields[1],": Wrong Address!")
                continue
            print(fields[1],": Correct Address!")
            r.append(fields[1])

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
mail_host="smtp.zju.edu.cn"  
mail_user="3180111441"    
mail_pass="sjy20090218"   
Users=['Anna','Mary','Emma']

n=0
sender = '3180111441@zju.edu.cn'
print("From:",sender)

while n<len(Users):
    receivers = r[n]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    m='Dear '+ Users[n]+ ",\nPlease find the results of your gene set linkage analysis result in attached file.\nThis is an email sent by the server, please don't reply.\nThank you for using GSLA."
    message = MIMEText(m, 'plain', 'utf-8')
    message['From'] = Header("Cici", 'utf-8')
    message['To'] =  Header("Anna", 'utf-8')
    subject = 'To '+Users[n]+':Your analysis job has been finished!'
    message['Subject'] = Header(subject, 'utf-8')    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect('smtp.zju.edu.cn', 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass) 
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error! Can not send the email.")
    n=n+1
    if n>=len(Users):
        break
    