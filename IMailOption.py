'''
Created on 14.10.2014

@author: jakob
'''

from zope.interface import Interface

class IMailOption(Interface):

    def get_subject(self):
        """subject"""

    def get_receiver(self):
        """receiver"""

    def get_transmitter(self):
        """transmitter"""

    def get_message(self):
        """message"""

    def get_loginname(self):
        """loginname"""

    def get_password(self):  
        """password"""  
    
    def get_SMTP_Server_URL(self):
        """SMTP Server URL"""
        
    def get_SMTP_Server_Prot(self):
        """SMTP Server Port"""
        
    def get_attachments(self):
        """attachments"""