from GitterClasses import *

if len(sys.argv) == 5 and sys.argv[1] == 'fetch' and sys.argv[3] == 'git-push':
	print 'Fetch from Codechef and push to github.'
	Config.githubUser = sys.argv[4]
	Config.gitpasswd = getpass.getpass('Git Password : ')
	confirm = getpass.getpass('Retype Password : ')
	if (Config.gitpasswd != confirm):
		sys.exit('Passwords dont match!')
elif len(sys.argv) == 3 and sys.argv[1] == 'fetch':
	print 'Fetch and save from Codechef'
else:
	sys.exit('Kindly follow correct format for input.\n\tpython teststrt.py fetch <codechef-username>\nOR\n\tpython strt.py fetch <codechef-username> git-push <github-username>/<github-repo>')


Config.codechefUser = sys.argv[2]

Chef.buildProblemListAndFileStructure(Config.codechefUser)
Chef.updateSubmissionList()
Chef.fetchSubmissions()

if len(sys.argv) == 3:
	sys.exit('Done.')
