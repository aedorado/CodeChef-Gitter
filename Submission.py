from GitterClasses import *

def getExtension(lang):
	return '.cpp'

# submission class
class Submission:
	def __init__(self, sid, verdict, link, lang, contestcode, pcode):
		self.sid = sid
		self.verdict = verdict
		self.link = link
		self.lang = lang
		self.contestcode = contestcode
		self.pcode = pcode

	def fetchCode(self, i):
		print 'Fetching '+ self.contestcode + '/' + self.pcode + '_' + str(i) + ' in ' + self.lang
		response = urllib2.urlopen(self.link)		#open webpage
		html = response.read()
		if i != 0:
			opfile = open('CodechefGitterSolutions\\' + self.contestcode + '\\' + self.pcode  + '_' + str(i) + getExtension(self.lang), 'w')
		else:
			opfile = open('CodechefGitterSolutions\\' + self.contestcode + '\\' + self.pcode  + '_' + str(i) + getExtension(self.lang), 'w')
		opfile.write(HTMLParser.HTMLParser().unescape(html)[5:-6])
		pass