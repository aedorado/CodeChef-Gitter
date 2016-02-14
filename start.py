from GitterClasses import *

if len(sys.argv) == 5 and sys.argv[1] == 'fetch' and sys.argv[3] == 'git-push':
    print 'Fetch from Codechef and push to github.'
    Config.githubUser = (sys.argv[4])[:(sys.argv[4]).find('/')]
    Config.githubRepo = (sys.argv[4])[(sys.argv[4]).find('/') + 1:]
    pass1 = getpass.getpass('Github Password : ')
    pass2 = getpass.getpass('Retype Password : ')
    if (pass1 != pass2):
        sys.exit('Passwords dont match!')
    else:
        Config.githubPasswd = pass1
        git = Git(Config.githubUser, Config.githubPasswd, Config.githubRepo)
        git.clone()
elif len(sys.argv) == 3 and sys.argv[1] == 'fetch':
    print 'Fetch and save from Codechef'
else:
    sys.exit(
        'Kindly follow correct format for input.\n\tpython start.py fetch <codechef-username>\nOR\n\tpython start.py fetch <codechef-username> git-push <github-username>/<github-repo>')

Config.codechefUser = sys.argv[2]

Chef.buildProblemListAndFileStructure(Config.codechefUser)
Chef.updateSubmissionList()
Chef.fetchSubmissions()

if len(sys.argv) == 3:
    sys.exit('Done.')

git.add()
git.commit('Another Auto Commit!')
git.push()

sys.exit(
    '\nTask Completed\n\nFORK from : https://github.com/aedorado/CodeChef-Gitter\n')
