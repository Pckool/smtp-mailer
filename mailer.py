#! /usr/local/bin/python
import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
from email.mime.text import MIMEText

SMTPserver = 'prismium.us'
sender =     'info@prismium.us'
destination = ['phillclesco@yahoo.com']

USERNAME = "info@prismium.us"
PASSWORD = "%z+#-DPB=#mR"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


content="""\
Test message
"""

subject="Meooowws"

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except Exception as exc:
    sys.exit( "mail failed; %s" % str(exc) ) # give a error message


    import poplib
from email import parser

pop_conn = poplib.POP3_SSL('prismium.us')
pop_conn.user('info@prismium.us')
pop_conn.pass_('%z+#-DPB=#mR')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    print (message['subject'])
pop_conn.quit()