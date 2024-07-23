# Introduction to Version Control and Git

In this module, we will introduce the basics of Git, emphasizing its functionality in version control. We will cover topics such as cloning repositories, forking, making pull requests, and merging repositories using Git on the command line.

# Version Control using Git and the Command Line

I will replicate what has been done step by step:

1. In this session, we opened Terminal and navigated to the desktop.
2. The Story directory was created, and text files were generated.
3. The Git repository was initialized with " **git init** ," establishing version control.
4. The working directory, staging area, and local repository were explained.
  1. **Working Directory** : The working directory is the current directory or folder where we are actively working on our project. It's where we create, modify, and delete files as part of our project. On this case, the Story directory is the working directory.
  2. **Staging Area** : The staging area is an intermediate step between the working directory and the local repository. It allows us to selectively choose which changes (files) we want to commit to the version control System.
    1. The presenter uses the git add command to add the file "chapter1.txt" to the staging area. This means that the changes made to this file are now ready to be committed.
  3. **Local Repository** : The local repository is where Git permanently stores the committed changes. It maintains a record of all the changes made to files over time, creating a history of the Project. In this case, the .git directory is created, representing the local repository
5. Commands:
    - " **git add**": changes to files were tracked by adding them to the staging area with it.
    - " **git commit -m**": changes were committed with it and a descriptive message. It is very important to establish a clear commit description or message.
    - " **git status**" is used to check the status of the working directory, staging area, and local repository in a Git project. It provides information about the changes made to files and their current state in relation to version control.
    - " **git diff**" to view differences.
    - " **git checkout**" to revert changes.
    - " **git log**": is used to display a log of commits in a Git repository. It provides a chronological history of commits, showing details such as the commit hash, author, date, and commit message.
    - " **git rm --cached -r .**": remove everything from the Git staging area.

The instructor created and modified text files, showcasing the commit process for each change. All the commands demonstrate how version control helps manage file versions.

# Github and Remote Repositories

In this lesson, the presenter discusses the process of creating a remote repository using GitHub. The steps involved are:

1. **GitHub Account Setup** : The process involves visiting GitHub.com, filling out a quick form, and confirming the email.
2. **Creating a Repository on GitHub** : by clicking on the "+" in the top right corner, selecting "New Repository," and providing a name and description. Public repositories are the default, but the option to make it private is available.
3. **Using Command Line Instructions** : we will use command line instructions to set up the repository (push it) in our laptop. The process involves copying the repository's URL from GitHub and executing commands in the terminal:
    - git remote add origin https://github.com/Angelas-Test-Account/Story.git
    - git branch -M main
    - git push -u origin main
4. **Creating a Remote** : refers to informing the local Git repository about the existence of a remote repository, particularly on a platform like GitHub. This involves using the command **git remote add origin** to establish a connection between the local repository and the remote repository. The remote is conventionally named " **origin**" for ease of understanding.
5. **Pushing to the Remote Repository** : The command **git push -u origin**** main **is executed to push the local repository to the remote repository. The "** main **" branch is specified, and the "** -u**" flag links up the local and remote repositories.

# Gitignore

The **.gitignore** file in Git allows users to specify rules for preventing certain files from being committed to both local and remote repositories. It is very important to exclude sensitive information like passwords and API keys from being hosted on platforms like GitHub. Examples of those files are **.DS\_Store** and **secrets.txt**.

The **.gitignore** file can be created by simply creating a file named like this. It is very important to keep the precise naming and case sensitivity. Inside this file, we can:

- List the folders and files we want to ignore.
- Use the pound sign ( **#** ) to add comments.
- Use wildcards for file types that will be ignored. E.g. \*.txt

GitHub repository **github/gitignore (**[https://github.com/github/gitignore](https://github.com/github/gitignore)) provides templates for different project types, including Python projects ([https://github.com/github/gitignore/blob/main/Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)). We can simply copy and paste from here.

# Cloning

The **git clone** command clones a remote repository on GitHub to the local machine. Cloning allows users to obtain a copy of a remote repository, including all versions and commits, and work on it in their own local environment. Cloning is a way to leverage someone else's open-source code, enabling users to customize, extend, or fix issues with the code. Studying and modifying open-source provides a huge educational value of code as a means to improve programming skills.

Interesting projects to clone and learn: [https://github.com/MunGell/awesome-for-beginners#python](https://github.com/MunGell/awesome-for-beginners#python)

# Branching and Merging

**Branching** ( **git branch**** name-of-branch**) allows developers to work on different features or experiments without affecting the main branch of a project. The main benefits of branching include the ability to develop features concurrently, experiment with new ideas, and isolate changes for testing.

How to **switch between branches** :

- **git branch** : lists the branches and marks with a \* the one you are currently on.
- **git checkout branch-name** : switches the branch to the specified branch name.

**Merging** ( **git merge**** name-of-branch**) is merging the changes made in a branch back into the main branch. To merge a branch with the main, we have to go to the main branch first, and then use the merge command. Merging implies resolving potential conflicts.

A graphical representation of the branching and merging process is presented using the GitHub network graph.

# Forking and Pull Requests

For working in a team of programmers and contributing to open-source projects, collaboration using remote repositories and GitHub is necessary.

**Forking** a repository on GitHub allows contributors to make changes to their own copy of the project without affecting the original. Forking is a crucial step in open-source collaboration, giving contributors full permissions over their duplicate repository. Giving write access to everyone could lead to issues, and forking allows contributors to suggest changes via **pull requests**. A pull request is like making a suggestion on a change to the original creators of the code, so that they can review and pull the changes.

# Additional Git Challenges

Complete the challenges here: [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
