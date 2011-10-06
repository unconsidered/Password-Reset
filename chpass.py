#!/usr/bin/env python                                                                                                                                                              
# encoding: utf-8                                                                                                                                                                  
"""                                                                                                                                                                                
Created by Daniel Clendenning on 10-5-2011.                                                                                                                                      
"""
import pwd, os, sys
#import subprocess


def my_change_passwd(user, passwd):
        #uid = pwd.getpwnam('root')[2]
        #os.setuid(uid)
        exit_code = os.system('echo "%s:%s" | chpasswd' % (user,passwd))
        if exit_code == 0:
        	pass
        else:
                print 'error code is %s' % (exit_code)


if __name__ == '__main__':
	user = sys.argv[1]
	passwd = sys.argv[2]
	if '"' in user or '"' in passwd:
		print 'error, cowardly refusing to proceed'
	my_change_passwd(user,passwd)
