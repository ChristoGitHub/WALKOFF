|Build Status| |Build status| |Maintainability|\ |GitHub (pre-)release|

Description
===========

-  Are repetitive, tedious processes taking up too much of your time?
-  Is more time spent focusing on managing your data than acting on the
   data itself?

WALKOFF is an automation framework that allows you to easily automate
these 80% of tedious tasks so you can get the job done faster, easier,
and cheaper.

WALKOFF is built upon an app based architecture which enables the plug
and play integration of devices and capabilities. These capabilities can
then be tied together to form Workflows. Workflows are defined in a JSON
format making them easily sharable across environments and organizations
and easily created/customizable through our drag and drop workflow
editor.

.. raw:: html

   <center>

.. raw:: html

   </center>

WALKOFF also makes it easier to manage your newly automated processes
with real-time visual updates and feeds based on your workflows
progress.

Apps can also have custom interfaces enabling app developers to uniquely
display information. WALKOFF not only makes it easier for users to
automate their processes but allows users to act on their processes
faster as well.

Walkoff apps can be found at: https://github.com/iadgov/WALKOFF-Apps

Installation Instructions
-------------------------

To install, you can run (possibly with administrator privileges)
``python setup_walkoff.py``

Alternatively, you can manually install WALKOFF

First, install the dependencies with the following command:

``pip install -r requirements.txt``

To install the dependencies for each individual app, run:

``python scripts/install_dependencies.py``

Or to just install the dependencies for specific apps:

``python scripts/install_dependencies -a AppOne,AppTwo,AppThree``

Next, navigate to /walkoff/client and install the client dependencies
with the following commands:

``npm install``

Next, use gulp to build the client:

``npm run build``

That's it! To start up the server, just navigate back to the walkoff
root and run:

``python walkoff.py``

Then, navigate to the specified IP and port to start using WALKOFF. The
default is ``http://127.0.0.1:5000``.

Through this script, you can also specify port and host, for example

::

    `python walkoff.py --port 3333 --host 0.0.0.0`

For more options, run

::

    `python walkoff.py --help`

Features
--------

1. Custom app interfaces

-  Interfaces are built using HTML/CSS/Javascript with back-end
   functionality using Python.

-  Capability to stream data to interfaces.

2. User and Role based authentication

3. Case based logging

-  Can granularly configure which events to log on a per-case basis

4. Drag and Drop Workflow Editor

-  Makes creation and editing of workflows as easy as dragging and
   dropping capabilities.

5. Flexible Workflow Execution

-  Manual Execution - Execute a workflow by pressing a button
-  Active Execution - Cron style workflow execution *Run workflow every
   8 hours for the next 3 months*
-  Passive Execution - Trigger a workflow based upon data sent to
   Walkoff
-  Ability to pause and resume workflows enabling *human in the loop*
   execution

6. Metrics

-  How often are certain apps run?

-  How often workflows are run?

Base Requirements
-----------------

-  Python 2.7+ or Python 3.4+
-  NodeJS and Node Package Manager (npm)
-  Tested on Windows and Linux

*Requirements for apps may differ*

Apps
----

WALKOFF-enabled apps can be found at www.github.com/iadgov/walkoff-apps

Branches
--------

1. master - Main branch for WALKOFF version 2 will be updated from
   development periodically
2. development - Development branch for WALKOFF version 2. Updated
   frequently
3. gh-pages - Pages used to generate documentation at our
   `github.io <https://iadgov.github.io/WALKOFF>`__ site
4. gh-pages-development - Branch used to document new features in
   development.
5. walkoff-experimental - WALKOFF version 1 *No longer under
   development*

*Other development-centric branches may be created but should not be
considered permanent*

Updating Walkoff
----------------

An update script, ``update.py``, is provided to update the repo to the
most recent release. This script uses SqlAlchemy-Alembic to update
database schemas and custom upgrade scripts to update the workflow JSON
files. To run this script in interactive mode run
``python update.py -i``. Other options can be viewed using
``python update.py --help``. The most common usage is
``python update.py -pcs`` for pull, clean, and setup.

Stability and Versioning
------------------------

WALKOFF uses Semantic Versioning. Until the full feature set is
developed, the versions will begin with ``0.x.y``. The ``x`` version
will be updated when a breaking change is made, a breaking change being
defined as one which modifies either the REST API or the API used to
develop and specify the apps is modified in a way which breaks backward
compatibility. No guarantees are yet made for the stability of the
backend Python modules. The ``y`` version will be updated for patches,
and bug fixes. The REST API will have an independent versioning system
which may not follow Walkoff's version number.

Contributions
-------------

WALKOFF is a community focused effort and contributions are welcome.
Please submit pull requests to the ``development`` branch. Issues marked
``help wanted`` and ``good first issue`` are great places to start
contributing. Additionally, you can always look at our `CodeClimate
Issues page <https://codeclimate.com/github/iadgov/WALKOFF/issues>`__
and help us improve our code quality.

Comments or questions? walkoff@nsa.gov

.. |Build Status| image:: https://img.shields.io/travis/iadgov/WALKOFF/master.svg?maxAge=3600&label=Linux
   :target: https://travis-ci.org/iadgov/WALKOFF
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/hs6ujwd1f87n39ut/branch/master?svg=true
   :target: https://ci.appveyor.com/project/iadgovuser11/walkoff/branch/master
.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/330249e13845a07a69a2/maintainability
   :target: https://codeclimate.com/github/iadgov/WALKOFF/maintainability
.. |GitHub (pre-)release| image:: https://img.shields.io/github/release/iadgov/WALKOFF/all.svg?style=flat
   :target: release
