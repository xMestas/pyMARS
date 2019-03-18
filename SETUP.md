## Setup

**[1]** - **Miniconda**

[Cantera Install Link](https://cantera.org/install/index.html) - we recommend using Miniconda which is linked below, specifically Miniconda3 for your respective operating system. Note that it requires 400MB disk space. Entire installation is very large (~3.5Gb), though subject to change as software is updated.

[Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) is our package install manager of choice. 

**[2]** - **Move Script to Appropriate Location**

PC :: Simply drag script into mobaXterm/other GUI.

Mac users :: `sftp <ONID>@flip.engr.oregonstate.edu`, `put <filename>`, `bye`

**[3]** - **Run .sh File**

`bash <filename>.sh` - Miniconda3 will be installed into location: `/nfs/stak/users/<ONID>/miniconda3`

This will install python 3.7.1 and roughly 40 other things (takes a minute or so)

**[4]** - **Ensure Conda is in Your .bashrc**

It should already be there.

`vim .bashrc in home folder`, then `export PATH=”/nfs/stak/users/{ONID}/miniconda3/bin:$PATH”`

**[5]** - **Restart Session**

exit and re-ssh to server to apply .bashrc changes

**[6]** - **Install Cantera**
`conda create --name spam --channel cantera cantera ipython matplotlib`
Installs a lot of stuff...drink a covfefe ☕️

Take great satisfaction in the spinning ascii loading disc. :: `y` to proceed, then take great satisfaction in ascii hashtag loading bars.

**[8]** - **Spam Environment**

_any time you want to run pymars, you must run this command_

when you are in this mode, prompt will include `(spam)`

then deactivate active environment at end with `source deactivate`

**[9]** - **Quick, Easy Installs**

`conda install networkx`

`conda install h5py`

`conda install pytables`

`conda install pytest`

maybe another real quick covfefe break ☕️

**[10]** - **Clone and Install**

clone GitHub repo to any location, but `<youonid>.flip.engr.oregonstate.edu` is preferred. 

Install with `python setup.py install`

potentially `python3 setup.py install` instead, from our experience.

pyMARS is called from terminal via pyMARS.py which can be found in the pyMARS directory.
