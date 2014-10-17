#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'jakob'


import ConfigParser
from StringIO import StringIO
import os
from zope.interface import implements
from IMailOption import IMailOption


class ConfPaser(object):
    implements(IMailOption)

    __pathToConfig = None
    __config = None
    
    __subject = ""
    __receiver = ""
    __transmitter = ""
    __message = ""
    __loginname = ""
    __password = ""
    __smtpserver = ""
    __smtpport = ""
    __attachments = ""

    def __init__(self, pathToConfig):
        try:
            if os.path.exists(pathToConfig):
                self.__pathToConfig = pathToConfig
            else:
                raise
        except:
            print "Config file not found.", pathToConfig
            exit(-1)
            #raise

        self.__config = ConfigParser.SafeConfigParser()

    def __ConfigSectionMap(self, section):
        dictOptions = {}
        options = self.__config.options(section)
        for option in options:
            try:
                dictOptions[option] = self.__config.get(section, option).strip('"').strip("'")
                if dictOptions[option] == "":
                    exit(-1)
                    #raise
            except:
                print("exception on %s ! maybe no value?" % option)
                exit(-1)
                #raise

        return dictOptions

    def paser(self):
        try:
            data = StringIO('\n'.join(line.strip() for line in open(self.__pathToConfig)))
            self.__config.readfp(data)
        except Exception as e:
            print "Configuration file could not be loaded ", e

        sections = self.__config.sections()
                
        try:
            sections = [x.lower() for x in sections]
            if ("global" not in sections):
                raise ImportError("global section error!")
        except ImportError as e:
            print e, " Maybe no global section in Configuration file?"
            exit(-1)
            #raise

        for section in self.__config.sections():
            try:
                dictOptions = self.__ConfigSectionMap(section)
                if section.lower() in "global":
                    self.__subject = dictOptions["subject"] if "subject" in dictOptions else None
                    self.__receiver = dictOptions["receiver"] if "receiver" in dictOptions else None
                    self.__transmitter = dictOptions["transmitter"] if "transmitter" in dictOptions else None
                    self.__message = dictOptions["message"] if "message" in dictOptions else None
                    self.__loginname = dictOptions["loginname"] if "loginname" in dictOptions else None
                    self.__password = dictOptions["password"] if "password" in dictOptions else None
                    self.__smtpserver = dictOptions["smtpserver"] if "smtpserver" in dictOptions else None
                    self.__smtpport = dictOptions["smtpport"] if "smtpport" in dictOptions else None
                    self.__attachments = dictOptions["attachments"] if "attachments" in dictOptions else None
            except:
                print "Error Configuration file please take a look."
                exit(-1)
                #raise
                
    def get_subject(self):
        return self.__subject

    def get_receiver(self):
        if self.__receiver == None:
            return None
        else:
            return self.__receiver.replace(' ', '').split(",")

    def get_transmitter(self):
        return self.__transmitter

    def get_message(self):
        return self.__message

    def get_loginname(self):
        return self.__loginname

    def get_password(self):
        return self.__password
    
    def get_SMTP_Server_URL(self):
        #print self.__smtpserver
        return self.__smtpserver
        
    def get_SMTP_Server_Prot(self):
        return self.__smtpport
    
    def get_attachments(self):
        if self.__attachments == None:
            return None
        else:
            return self.__attachments.replace(' ', '').split(",")


