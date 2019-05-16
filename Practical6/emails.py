# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:08:43 2019

@author: cici\
Practical 6: Working with strings
"""
#import necessary libraries
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#open csv file
address=open('C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical6/address_information.csv','r')
r=[]
#get information from csv file
for line in address:
    fields=line.split(r',')
    if (len(fields)>1):
        if re.match(r'(\S+)@(\S+)',fields[1]):
            #check the email address
            if not '.com' in fields[1]:
                print(fields[1],": Wrong Address!")
                continue
            #print the results of address validation
            print(fields[1],": Correct Address!")
            r.append(fields[1])
#send emails
mail_host="smtp.zju.edu.cn"  
mail_user=input('Please input user name:')   
mail_pass=input('Please input password:')   
Users=['Anna','Mary','Emma']
n=0
sender = '3180111441@zju.edu.cn'
print("From:",sender)
body=open('C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical6/body.txt','r')
d=body.read()
body.close()
while n<len(Users):
    receivers = r[n]
    m=d.replace('User',Users[n])#Modify the text
    message = MIMEText(m, 'plain', 'utf-8')
    message['From'] = Header("Cici", 'utf-8')
    message['To'] =  Header(Users[n], 'utf-8')
    subject = 'To '+Users[n]+':Your analysis job has been finished!'
    message['Subject'] = Header(subject, 'utf-8')    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect('smtp.zju.edu.cn', 25)
        smtpObj.login(mail_user,mail_pass) 
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Error! Can not send the email.")
    n=n+1
    if n>=len(Users):
        break