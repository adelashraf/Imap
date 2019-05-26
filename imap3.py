#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import getpass, imaplib
import pprint

mail = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    mail.login(sys.argv[1], getpass.getpass())
except IndexError:
    print ('please write email')
mail.select('Inbox')
tmp, data = mail.search(None, 'ALL')
num =  data[0].split()
print ('you have ', str(num).replace('[', '').replace(']', '').replace(' ', ''), 'message')
num =input('Write the mail to see :')
try:
    tmp, data = mail.fetch(str(num), '(RFC822)')
except ValueError :
    print ('please write the true message from the list')
mes = str(pprint.pprint(data[0][1]))
print (mes)
