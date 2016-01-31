from GitterClasses import *

# problemlist = [ Problem('LTIME32', '/LTIME32/status/TRIANGCL,anurageldorado', []),
				# Problem('JAN15', '/JAN15/status/ONEKING,anurageldorado', []),
				# Problem('JAN16', '/JAN16/status/DEVPERF,anurageldorado', []),
				# Problem('Practice Problems', '/status/CHRECT,anurageldorado', [])]

problemlist = []

def buildProblemListAndFileStructure():
	user = 'gr8raghav'
	url = 'https://www.codechef.com/users/' + user

	response = urllib2.urlopen(url)		#open webpage
	html = response.read()

	soup = BeautifulSoup(html, "html.parser")
	tds = soup.findAll('td')
	tdps = soup.findAll('p')

	finaltdp = []
	for tdp in tdps:
		if len(tdp.findAll('b')) != 0 and len(tdp.findAll('span')) != 0:
			finaltdp.append(tdp)

	if not os.path.exists('CodechefGitterSolutions/'):		# if directory doesn't exist
		print 'Creating Directory: CodechefGitterSolutions/'
		os.makedirs('CodechefGitterSolutions/')

	for tdp in finaltdp:
		contestcode = tdp.find('b')
		contestcode = contestcode.get_text()
		print contestcode

		if not os.path.exists('CodechefGitterSolutions/' + contestcode + '/'):		# if directory doesn't exist
			# print 'Creating Directory: CodechefGitterSolutions/' + contestcode + '/'
			os.makedirs('CodechefGitterSolutions/' + contestcode + '/')				# create directory 

		problems = tdp.findAll('a');

		for problem in problems:
			print '--> ' + problem['href']
			problemlist.append(Problem(contestcode, problem['href'], []))	# instantiate object and add to list

	print str(len(problemlist)) + ' problems found.\n'

def updateSubmissionList():
	# fill submission details in submissionlist of each problem
	print 'Updating submission details.'
	for problem in problemlist:
		problem.updateSubmissionList()


def fetchSubmissions():
	print 'Fetching all accepted solutions.'
	for problem in problemlist:
		problem.fetchAllSubmissions()
		pass

buildProblemListAndFileStructure()
updateSubmissionList()
fetchSubmissions()