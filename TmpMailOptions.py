'''
Created on 16.10.2014

@author: jakob
'''

from zope.interface import implements
from IMailOption import IMailOption

class TmpMailOptions(object):
    implements(IMailOption)

    __subject = ""
    __receiver = ""
    __transmitter = ""
    __message = ""
    __loginname = ""
    __password = ""
    __attachments = ""
    __SMTP_Server_URL = ""
    __SMTP_Server_Prot = ""

    def get_subject(self):
        return self.__subject

    def get_receiver(self):
        return self.__receiver

    def get_transmitter(self):
        return self.__transmitter

    def get_message(self):
        return self.__message

    def get_loginname(self):
        return self.__loginname

    def get_password(self):
        return self.__password

    def get_attachments(self):
        return self.__attachments

    def set_subject(self, value):
        self.__subject = value

    def set_receiver(self, value):
        self.__receiver = value

    def set_transmitter(self, value):
        self.__transmitter = value

    def set_message(self, value):
        self.__message = value

    def set_loginname(self, value):
        self.__loginname = value

    def set_password(self, value):
        self.__password = value

    def set_attachments(self, value):
        self.__attachments = value
        
    def get_SMTP_Server_URL(self):
        return self.__SMTP_Server_URL

    def get_SMTP_Server_Prot(self):
        return self.__SMTP_Server_Prot

    def set_SMTP_Server_URL(self, value):
        self.__SMTP_Server_URL = value

    def set_SMTP_Server_Prot(self, value):
        self.__SMTP_Server_Prot = value

    subject = property(get_subject, set_subject, None, None)
    receiver = property(get_receiver, set_receiver, None, None)
    transmitter = property(get_transmitter, set_transmitter, None, None)
    message = property(get_message, set_message, None, None)
    loginname = property(get_loginname, set_loginname, None, None)
    password = property(get_password, set_password, None, None)
    attachments = property(get_attachments, set_attachments, None, None)
    smtpserver = property(get_SMTP_Server_URL, set_SMTP_Server_URL, None, None)
    smtpport = property(get_SMTP_Server_Prot, set_SMTP_Server_Prot, None, None)
    
 
    

        