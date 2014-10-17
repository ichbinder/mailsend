#!/usr/bin/env python
# encoding: utf-8
'''
Created on 10.10.2014

@author: jakob
'''

import sys
import os
from optparse import OptionParser 
from zope.interface import implements
from IMailOption import IMailOption

class Cli(object):
    implements(IMailOption)
    
    __version__ = 0.1
    __updated__ = '2014-10-10'
    
    __parser = None
    __opts = None

    def __init__(self):
        program_name = os.path.basename(sys.argv[0])
        program_version = "v%s" % (self.__version__)
        program_build_date = "%s" % (self.__updated__)

        program_version_string = '%s %s (%s)' % (program_name, program_version, program_build_date)
        program_longdesc = "Send Emails" 
        program_license = "Copyright 2014 Jakob Warnow Licensed under the GPL2"
        
        self.__parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
        
        self.__parser.add_option("-s", "--subject", dest="subject", help="The subject of Mail", action='store')
        self.__parser.add_option("-r", "--receiver", dest="receiver", help="Set the receiver", action='store')
        self.__parser.add_option("-t", "--transmitter", dest="transmitter", action="store", help="Set the transmitter")
        self.__parser.add_option("-m", "--message", dest="message", action="store", help="Message to send", default="default Mail")
        self.__parser.add_option("-l", "--login_name", dest="loginname", action="store", help="Set the login name for SMTP Server")
        self.__parser.add_option("-p", "--password", dest="password", action="store", help="Set the password for SMTP Server")
        self.__parser.add_option("-u", "--smtp_server", dest="smtpserver", action="store", help="Set the URL for SMTP Server")
        self.__parser.add_option("-o", "--smtp_port", dest="smtpport", action="store", help="Set the port for SMTP Server")
        self.__parser.add_option("-f", "--file", dest="file", help="Set the attachments for Mail", metavar="FILE")

    def paser(self):
        (opts, args) = self.__parser.parse_args()
        self.__opts = opts
        
        if not ((opts.loginname is None) and (opts.password is None)):
            # Making sure all mandatory options appeared.
            google_mandatories = ['loginname', 'password']
            
            for gm in google_mandatories:
                if not opts.__dict__[gm]:
                    print "google mandatory option is missing\n"
                    self.__parser.print_help()
                    exit(-1)

    def get_subject(self):
        return self.__opts.subject

    def get_receiver(self):
        if self.__opts.receiver == None:
            return None
        else:
            return self.__opts.receiver.replace(' ', '').split(",")

    def get_transmitter(self):
        return self.__opts.transmitter

    def get_message(self):
        return self.__opts.message

    def get_loginname(self):
        return self.__opts.loginname

    def get_password(self):
        return self.__opts.password
    
    def get_SMTP_Server_URL(self):
        return self.__opts.smtpserver
        
    def get_SMTP_Server_Prot(self):
        return self.__opts.smtpport
    
    def get_attachments(self):
        if self.__opts.file == None:
            return None
        else:
            return self.__opts.file.replace(' ', '').split(",")
