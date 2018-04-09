# HutchIOPythonNextSteps
a git repo to keep track of code samples for fredhutch.io Next Steps in Python course

## Useful Links
### Class Outline
https://docs.google.com/document/d/163mlqhwYd5zUMZufD_2qAknvcjE0F-c-QNDr2gVfhwo/edit?usp=sharing

### Getting Started with Git
If you are primarily using Windows, GitHub has a Git GUI that can be used to interact with course repositories
Available here:
https://desktop.github.com/

Otherwise, if you are primarily using a *nix platform, you will need to be familiar with the Git Command Line Interface
A cheat sheet can be found here:
https://services.github.com/on-demand/downloads/github-git-cheat-sheet/

Some additional insights for setting up Git can be found here:
https://teams.fhcrc.org/sites/HDC/HDC%20Wiki/Data%20Science/Setting%20Up%20Git.aspx

Generally, regardless of whether you primarily interact with GitHub via a GUI, 
*it is a good idea to learn at least your basic workflow in terms of the command line interface*

The steps to pull this branch (Hello-World) down to your work environment of choice will look like the following:
1) make a fork of HutchIOPythonNextSteps to your personal GitHub Account
2) make a local clone of your forked repository from step 1
3) perform a *git fetch* operation to pull down the latest changes from your forked repository (normally referred to as origin)
4) Create a new local branch for Hello-World: git checkout -b <name of your local branch> origin/Hello-World

## Connecting to Hutch Resources
If you prefer, Hutch SciComp hosts a robust scientific computing cluster that can be accessed from within the Fred Hutch network
Computing Resources at the Hutch:
https://teams.fhcrc.org/sites/citwiki/SciComp/Pages/How%20can%20I%20access%20compute%20resources%20from%20remote.aspx 

Basic steps for connection
Join Fred Hutch Network via VPN if off campus, or via secure WiFi if on Campus
VPN software for the Hutch can be found here: https://centernet.fredhutch.org/cn/u/center-it/vpn.html

Use NoMachine or similar to connect to one of the *Linux Desktop Environments* like Sphinx, Minx, or Lynx


from a command line terminal within the NoMachine session, connect to the *SciComp rhino cluster*

a brief overview of this process can be found here:
https://teams.fhcrc.org/sites/HDC/HDC%20Wiki/Data%20Science/Project%20Setup.aspx

## Setting up your Python Environment
### Windows
A UI based installation route: Anaconda
https://www.anaconda.com/download/

Alternately, a handy set of instructions from Google:
https://cloud.google.com/python/setup#windows


### Linux
*Note: While you can install and maintain your own distribution of linux as part of your own work environment, 
I highly recommend you become comfortable using the SciComp provided resources for ease-of-use*

####Modules
https://teams.fhcrc.org/sites/citwiki/SciComp/Pages/How%20to%20use%20environment%20Modules.aspx

essentially, running a custom python environment  on the rhino cluster is done in two steps:
set up a baseline environment using a module load command like:
> module load Python/3.6.2-foss-2016b-fh2

followed by setting up a Python Virtual Environment on top like:
> virtualenv mypythonenv --system-site-packages

which will make a new folder called mypythonenv in the current directory
 
A summary of virtualenvs can be found here: http://docs.python-guide.org/en/latest/dev/virtualenvs/
but for our purposes, it is enough to know the following

an inactive virtualenv can be started like
> source mypythonenv/bin/activate

an active virtualenv can be shut off with
> deactivate

and while a virtualenv is active, you can run python installations to install to that environment, 
circumventing the need to have admin priviledges to install python libraries
> pip install numpy



