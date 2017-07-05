# What should I know before I get started?
Refer to the [Readme.md](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/blob/master/README.md) and the [Software Version Requirement](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/wiki/II.-Software-Version-Requirement)

# How Can I Contribute?
Firstly you need a local fork of the the project, so go ahead and press the "fork" button in GitHub. This will create a copy of the repository in your own GitHub account and you'll see a note that it's been forked underneath the project name:
***
yourname/3D-SCANNER-IITB
Now you need a copy locally, so find the "SSH clone URL" in the right hand column and use that to clone locally using a terminal:
***
$ git clone git@github.com:yourname/3D-SCANNER-IITB.git
***
Change into the new project's directory:

$ cd 3D-SCANNER

Finally, in this stage, you need to set up a new remote that points to the original project so that you can grab any changes and bring them into your local copy. Firstly clock on the link to the original repository – it's labeled "Forked from" at the top of the GitHub page. This takes you back to the projects main GitHub page, so you can find the "SSH clone URL" and use it to create the new remote, which we'll call upstream.

$ git remote add upstream git@github.com:.../3D-SCANNER-IITB.git
You now have two remotes for this project on disk:

    origin which points to your GitHub fork of the project. You can read and write to this remote.
    upstream which points to the main project's GitHub repository. You can only read from this remote.
### Branch!

The number one rule is to put each piece of work on its own branch. If the project is using git-flow, then it will have both a master and a develop branch.
For more details follow this link: [beginner'sGuide](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)

### Reporting Bugs
Issues can be used to keep track of bugs, enhancements, or other requests.Any GitHub user can create an issue in a public repository where issues have not been disabled.
     On GitHub, navigate to the main page of the repository.
     Issues tab Under your repository name, click Issues.
     New Issues buttonClick New issue.
     A Sample issue Type a title and description for your issue.
If you're a project maintainer, you can assign the issue to someone, add it to a project board, associate it with a milestone, or apply a label.
When you're finished, click Submit new issue.

### Suggesting Enhancements
### Your First Code Contribution
### Pull Requests
***
On GitHub, navigate to the main page of the repository.

Branch dropdown menuIn the "Branch" menu, choose the branch that contains your commits.

Pull Request buttonTo the right of the Branch menu, click New pull request.

Drop-down menus for choosing the base and compare branchesUse the base branch dropdown menu to select the branch you'd like to merge your changes into, then use the compare branch drop-down menu to choose the topic branch you made your changes in.

Pull request title and description fields Type a title and description for your pull request.
Create pull request button Click Create pull request
***
For more help follow this link: [PullRequest](https://help.github.com/articles/creating-a-pull-request/)
# Styleguides

    Git Commit Messages
    Documentation Styleguide

# Additional Notes

    Issue and Pull Request Labels
