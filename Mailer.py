'''
Created on 15.10.2014

@author: jakob
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os.path

class Mailer(object):

    def __init__(self, imailoption):
        assert isinstance(imailoption.get_receiver(), list)#, "receiver parameter ist not a list"
        self.__imailoption = imailoption
        
    def sendmail(self):
        msg = MIMEMultipart()
        msg['From'] = self.__imailoption.get_transmitter()
        msg['To'] = COMMASPACE.join(self.__imailoption.get_receiver())
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.__imailoption.get_subject()
    
        msg.attach( MIMEText(self.__imailoption.get_message()) )
        
        if self.__imailoption.get_attachments() != None:
            for am in self.__imailoption.get_attachments():
                if os.path.isfile(am):
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload( open(am,"rb").read() )
                    Encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(am))
                    msg.attach(part)
                else:
                    print "File dont not exists: %s" % (am)
    
        smtp = smtplib.SMTP(self.__imailoption.get_SMTP_Server_URL(),
                            self.__imailoption.get_SMTP_Server_Prot())
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.__imailoption.get_loginname(), 
                   self.__imailoption.get_password())
        smtp.sendmail(self.__imailoption.get_transmitter(),
                      self.__imailoption.get_receiver(), 
                      msg.as_string())
        smtp.close()
        