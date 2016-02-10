from GitterClasses import *


class Git(object):

    remoteUrl = ''

    def __init__(self, username, password, repo):
        self.username = username
        self.password = password
        self.repo = repo
        self.remoteUrl = 'https://www.github.com/' + username + '/' + repo

    def clone(self):
        if os.path.exists(self.repo):
            sys.exit(
                'fatal: destination path \'' +
                self.repo +
                '\' already exists and is not an empty directory.')
        os.system('git clone ' + self.remoteUrl)

    def add(self):
        os.chdir(self.repo)
        os.system('git add .')

    def commit(self, msg):
        os.system('git commit -m \'' + msg + '\'')

    def push(self):
        pass
        os.system(
            'git push https://' +
            self.username +
            ':' +
            self.password +
            '@github.com/' +
            self.username +
            '/' +
            self.repo)


# REPO_NAME = 'test'
# REMOTE_URL = 'https://github.com/aedorado/' + REPO_NAME + '.git'
# FILE_NAME = 'new_file.txt'
# MSG = 'A new commit'

# if os.path.exists(REPO_NAME):
#     shutil.rmtree(REPO_NAME)

# os.system('git clone ' + REMOTE_URL)
# os.chdir(REPO_NAME)
# os.system('pwd')

# open(FILE_NAME, 'wb').close()

# os.system('git add .')
# os.system('git commit -m \'' + MSG + '\'')
# os.system('git push https://aedorado:****@github.com/aedorado/test.git')
# git push
# https://<username>:<password>@github.com/<username>/<repository-name>

# print "---- DONE ----"
