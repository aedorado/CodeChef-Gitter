from GitterClasses import *

problemlist = []


def buildProblemListAndFileStructure(user):
    url = 'https://www.codechef.com/users/' + user
    print '\nAttempting First Fetch'

    OK = False
    while OK is False:
        try:
            response = urllib2.urlopen(url)  # open webpage
            print 'Success'
            OK = True
        except urllib2.HTTPError as e:
            print 'Failure.\nAn HTTP error occured : ' + str(e.code)
            print 'Refetching..'

    html = response.read()  # read the response
    soup = BeautifulSoup(html, "html.parser")
    tdps = soup.findAll('p')

    finaltdp = []
    for tdp in tdps:
        if len(tdp.findAll('b')) != 0 and len(tdp.findAll('span')) != 0:
            finaltdp.append(tdp)

    if not os.path.exists(Config.githubRepo):		# if directory doesn't exist
        print 'Creating Directory: ' + Config.githubRepo
        os.makedirs(Config.githubRepo)

    for tdp in finaltdp:
        contestcode = tdp.find('b')
        contestcode = contestcode.get_text()
        print contestcode

        if not os.path.exists(Config.githubRepo + '/' + contestcode + '/'):		# if directory doesn't exist
            # print 'Creating Directory: CodechefGitterSolutions/' +
            # contestcode + '/'
            os.makedirs(
                Config.githubRepo +
                '/' +
                contestcode +
                '/')				# create directory

        problems = tdp.findAll('a')

        for problem in problems:
            print '--> ' + problem['href']
            problemlist.append(
                Problem(contestcode,
                        problem['href'],
                        []))  # instantiate object and add to list

    print str(len(problemlist)) + ' problems found.\n'

totalFetchCount = 0


def updateSubmissionList():		# fill submission details in submissionlist of each problem
    global totalFetchCount
    print 'Updating submission details.'
    i = 0
    total = len(problemlist)
    for problem in problemlist:
        problem.updateSubmissionList()
        i = i + 1
        print str(float(i * 100) / total)[0:5] + '% done.\n'
        totalFetchCount = totalFetchCount + len(problem.submissionList)


def fetchSubmissions():
    print 'Fetching all required solutions (' + str(totalFetchCount) + ' total)'
    fetchedCount = 0
    for problem in problemlist:
        problem.fetchAllSubmissions()
        fetchedCount = fetchedCount + len(problem.submissionList)
        print str(float(fetchedCount * 100) / totalFetchCount)[0:5] + '% done.\n'
