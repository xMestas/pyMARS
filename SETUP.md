## Setup

#### Miniconda Package Manager
[Cantera Install Link](https://cantera.org/install/index.html) - we recommend using the Miniconda package manager which is linked below, specifically Miniconda3 for your respective operating system. Note that it requires 400MB disk space. Entire installation is very large (~3.5Gb), though subject to change as software is updated.

[Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) 

Ensure Conda is in Your .bashrc -- it should already be there.

`vim .bashrc in home folder`, include `export PATH=”/nfs/stak/users/{ONID}/miniconda3/bin:$PATH”` (or something similar) if necessary

#### Script
**[1]** - **Moving Script to Appropriate Location**

PC :: Simply drag script into mobaXterm/other GUI.

Mac users :: `sftp your@server.address`, `put <filename>`, `bye`

**[2]** - **Running Script**

`bash <filename>.sh`

This will install python 3.7.1 and roughly 40 other things (takes a minute or so)

**[3]** - **Post-Script Restart of Session**

exit and re-ssh to server to apply .bashrc changes

#### Cantera
`conda create --name spam --channel cantera cantera ipython matplotlib`

#### Environment
`source activate spam`

_any time you want to run pymars, you must run this command_

when you are in this mode, prompt will include `(spam)`

then deactivate active environment at end with `source deactivate`

#### Library Installs w/ Conda

`conda install networkx`

`conda install h5py`

`conda install pytables`

`conda install pytest`

#### Clone and Install

clone GitHub repo to your preferred location (note the 3.5Gb size)

Install with `python setup.py install`

potentially `python3 setup.py install` instead, from our experience.

`pyMARS` is called from terminal via pyMARS.py which can be found in the pyMARS directory. (a double `cd`)

-------

**Oregon State University Specifics**

- likely using flip server
- Miniconda3 will likely be installed into location: `/nfs/stak/users/<ONID>/miniconda3`

