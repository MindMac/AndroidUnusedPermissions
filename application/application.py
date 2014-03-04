#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-2

@author: Wenjun Hu
'''

# Global imports
import re, logging

# PermissionScanner imports
from permissions_map.api import API_PERMISSION_MAP
from permissions_map.intent import INTENT_PERMISSION_MAP
from permissions_map.contentprovider import CONTENTPROVIDER_PERMISSION_MAP

# Certificate information
CERT_ISSUER = 'issuer'
CERT_SUBJECT = 'subject'
CERT_SERIALNUM = 'serial_num'
CERT_THUMBPRINT = 'thumbprint'

# Logguer
log = logging.getLogger('log')

def to_unicode(string):
    if string:
        return unicode(string, 'utf-8', 'ignore')
    else:
        return string

def get_certificate(apk, filename) :
    try :
        import chilkat
        cert = chilkat.CkCert()
        f = apk.get_file( filename )
        bytedata = chilkat.CkByteData()
        bytedata.append2(f, len(f))
        success = cert.LoadFromBinary(bytedata)
        return success, cert
    except ImportError :
        log.error("The Chilkat module is not installed, see http://www.chilkatsoft.com/python.asp")
        return False, []

def get_certificate_information(apk) :
    file_list = apk.get_files()
    cert_pattern = re.compile('^(META-INF\/(.*).RSA)$')
    cert_file = ''
    cert_info = {}
    
    for i in file_list :
        if cert_pattern.match(i):
            cert_file = cert_pattern.match(i).groups()[0]
            log.info("Certificate found : %s" % cert_file)
            break

    
    success, cert = get_certificate(apk, cert_file)
    
    
    if success != True :
        log.error("Can not read the certificate %s from the APK" % cert_file)
        return cert_info

    cert_info_issuer  = ["C=%s" % to_unicode(cert.issuerC()), "ST=%s" % to_unicode(cert.issuerS()), 
                         "L=%s" % to_unicode(cert.issuerL()), "O=%s" % to_unicode(cert.issuerO()) , 
                         "OU=%s" % to_unicode(cert.issuerOU()) , "CN=%s" % to_unicode(cert.issuerCN()) ]
    cert_info_subject = ["C=%s" % to_unicode(cert.subjectC()), "ST=%s" % to_unicode(cert.subjectS()), 
                         "L=%s" % to_unicode(cert.subjectL()), "O=%s" % to_unicode(cert.subjectO()) , 
                         "OU=%s" % to_unicode(cert.subjectOU()) , "CN=%s" % to_unicode(cert.subjectCN()) ]

    cert_info[CERT_ISSUER] = ':'.join(cert_info_issuer)
    cert_info[CERT_SUBJECT] = ':'.join(cert_info_subject)
    cert_info[CERT_SERIALNUM] = cert.serialNumber()
    cert_info[CERT_THUMBPRINT] = cert.sha1Thumbprint()
    
    return cert_info

# Get api etc. by permission
def get_api_list(permission):
    return API_PERMISSION_MAP.get(permission)

def get_intent_list(permission):
    return INTENT_PERMISSION_MAP.get(permission)

def get_contentprovider_list(permission):
    return CONTENTPROVIDER_PERMISSION_MAP.get(permission)

