
Complete definitions for key Git & GitHub terminology

GIT WORKFLOW FUNDAMENTALS

Working Directory - This is the project folder/workspace.    

Staging Area - The staging area can also be referred to as “untracked files”. This is usually where files that have not been committed yet go to.

Local Repo (head) - The local repository refers to a Git repository that is kept locally on your computer. A head is a pointer to a commit object.  Any number of heads can be found in a repository. One head is chosen to be the "current head" at any given time; this head is aliased to HEAD.

Remote repo (master) - Versions of your project that are hosted on a network or the Internet are known as remote repositories. Each of them typically has either read-only or read/write access for you, and you can have a number of them.

WORKING DIRECTORY STATES  

Staged -  There are three main states that your file can reside in within Git. 

These three states combine to form a system based on promotion where each file may reside in one of these three states and switch between them based on operations performed on it. When a file enters the staged state, we are done making all the modifications. You have marked the file to go into the next commit snapshot, which means it is now prepared to be uploaded to the local git database.
Modified - The state of the file changes from committed to modified whenever any modification is made. This is because the document has changed since its last committed version was saved to our local database. 

Committed - The file is now safely stored in your local database. 

GIT COMMANDS:

Git add - A change in the working directory is added to the staging area via the git add command.

Git commit - One of the fundamental and essential features of Git is the git commit command. The add command is important as it selects the changes that will be staged for the next commit.. Git commit is then used to create a snapshot of the staged changes.

Git push - To upload content from a local repository to a remote repository, you will need to use the git push command. Commits are sent from your local repository to a remote repository through pushing.

Git fetch - The git fetch command allows you to download commits, refs and  files from a remote repository into your local repo.

Git merge - With the help of this command, you can take the independent lines of development created by a git branch and have them integrated into a single branch.

