from GitterClasses import *

# problem class


class Problem:

    def __init__(self, contestcode, statuslink, submissionList):
        self.contestcode = contestcode
        self.statuslink = statuslink
        self.submissionList = []
        self.pcode = self.getPcodeFromStatusLink(statuslink)

    def getPcodeFromStatusLink(self, statuslink):
        pattern = '[A-Z0-9]*,'
        pcode = re.search(pattern, statuslink)
        pcode = pcode.group(0)
        pcode = pcode[:-1]						# remove , form 'KSPHERES,'
        return pcode

    def updateSubmissionList(self):

        print 'Updating submittion list for ' + self.pcode
        url = 'https://www.codechef.com' + self.statuslink
        print url

        OK = False
        while OK is False:
            try:
                response = urllib2.urlopen(url)  # open webpage
                print 'Success'
                OK = True
            except urllib2.HTTPError as e:
                print 'Failure.\nAn HTTP error occured : ' + str(e.code)
                print 'Refetching..'

        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.findAll('tr', {'class': 'kol'})
        print str(len(rows)) + ' submittions found.'
        accepted_sols = 0

        for row in rows:
            tds = row.findAll('td')

            verdict = tds[3].find('span')['title']
            if verdict != 'accepted' and verdict != '':
                # print '\n~ Continued ~\n'
                continue
            elif verdict == '':
                points = tds[3].find('span').get_text()
                if points.find('100') == -1:
                    continue
                verdict = 'accepted'

            accepted_sols = accepted_sols + 1

            sid = tds[0].get_text()

            path_list = glob.glob(
                Config.githubRepo +
                '/' +
                self.contestcode +
                '/*' +
                self.pcode +
                '*')

            cont = False
            for path in path_list:
                if path.find(sid) != -1:
                    print str(sid) + ' already available.'
                    cont = True
                    break

            if cont:
                continue

            lang = tds[6].get_text()
            link = 'https://www.codechef.com' + \
                tds[7].find('a')['href'].replace(
                    'viewsolution', 'viewplaintext')

            self.submissionList.append(
                Submission(sid,
                           verdict,
                           link,
                           lang,
                           self.contestcode,
                           self.pcode))

        print str(accepted_sols) + ' accepted submissions.'
        print str(len(self.submissionList)) + ' need to be updated.'

    def fetchAllSubmissions(self):				# fetch all submissions of a given problem
        i = 0
        for submission in self.submissionList:
            submission.fetchAndSave(
                i)			# fetch each submissions of a given problem
            i = i + 1
        pass
