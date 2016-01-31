import urllib2	#to interact with urls
import os		#to interact with os
import re 		#to use regular expressions
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

#problem class
class Problem:

	def __init__(self, contestcode, statuslink, submission_list):
		self.contestcode = contestcode
		self.statuslink = statuslink
		self.submission_list = []
		self.pcode = self.getPcodeFromStatusLink(statuslink)

	def getPcodeFromStatusLink(self, statuslink):
		pattern = '[A-Z0-9]*,'
		pcode = re.search(pattern, statuslink)
		pcode = pcode.group(0)
		pcode = pcode[:-1]						# remove , form 'KSPHERES,'
		return pcode

	def updateSubmittionList(self):
		print 'Updating submittion list for ' + self.pcode
		url = 'https://www.codechef.com' + self.statuslink
		print url
		response = urllib2.urlopen(url)		#open webpage
		soup = BeautifulSoup(html, 'html.parser')
		rows = soup.findAll('tr')#, { 'class' : 'kol' })
		print str(len(rows)) + ' submittions found.'
		pass


user = 'divyanshumehta'
url = 'https://www.codechef.com/users/' + user

response = urllib2.urlopen(url)		#open webpage
html = response.read()

print 'Response 1 Recieved'

soup = BeautifulSoup(html, "html.parser")
tds = soup.findAll('td')
tdps = soup.findAll('p')

finaltdp = []
for tdp in tdps:
	if len(tdp.findAll('b')) != 0 and len(tdp.findAll('span')) != 0:
		finaltdp.append(tdp)

problemlist = []

for tdp in finaltdp:
	contestcode = tdp.find('b')
	print contestcode.get_text()
	problems = tdp.findAll('a');

	for problem in problems:
		print '--> ' + problem['href']
		# pcode = re.search(pattern, problem['href'])
		# pcode = pcode.group(0)
		# pcode = pcode[:-1]							# remove , form 'KSPHERES,'
		problemlist.append(Problem(contestcode.get_text(), problem['href'], []))	# instantiate object and add to list


print str(len(problemlist)) + ' problems found..'

#append submission details to submissionlist of each problem
for problem in problemlist:
	problem.updateSubmittionList()