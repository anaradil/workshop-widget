Install and run Hubs
====================

.. highlight:: shell


Repositories
------------

The Fedora Hubs project page is https://pagure.io/fedora-hubs/. Go there and
fork the project, you'll be working on your own fork. If you already have a
fork, make sure the code is up-to-date. If you're not sure, go to your local
clone and run::

    git checkout develop
    git pull --rebase upstream develop
    git push

The ``git cherry -v`` command should return nothing.

If you don't have an existing fork, clone your fork locally with a command
similar to::

    git clone ssh://git@pagure.io/forks/your-username/fedora-hubs.git

In this workshop, you will create a widget for Fedora Hubs. To avoid wasting
too much time, an initial directory structure is available by cloning this
repository::

    git clone https://pagure.io/fedora-hubs-widget-workshop.git widget-workshop

You don't need to fork that repository in Pagure. Make sure the local name of
the clone is ``widget-workshop`` or some examples won't automatically work
later in this tutorial.


Development VM
--------------

You will be using Vagrant to hack on Hubs, so make sure you have the necessary
dependencies installed::

    sudo dnf install ansible vagrant vagrant-libvirt vagrant-sshfs

Copy the workshop's Vagrant file to your fedora-hubs clone and go to the
``fedora-hubs`` directory::

    cp widget-workshop/Vagrantfile fedora-hubs/Vagrantfile
    cd fedora-hubs

You are now ready to create the virtual machine::

    vagrant up --provider=libvirt

This command will take some time to complete. The Vagrant VM that will be
downloaded and used is based on a Fedora 25 bare VM, that has been provisionned
using the Ansible playbook available in the ``ansible`` subdirectory. This
playbook will be run again to provision the VM (but will have almost nothing to
do). The result is identical to starting from the ``fedora/25-cloud-base``
Vagrant box, only faster.

.. note::

    Make sure you don't have another development server running on port 5000 on
    your machine (maybe another Flask-based project you're working on?). If so,
    just shut down the development web server for now.

When the previous command is done, reboot the VM to make sure it is running
with the latest updates with the following command::

    vagrant reload

You can now use ``vagrant ssh`` to connect to the machine. You'll be greeted
with a message containing instructions to start the development server.


Running Hubs
------------

First, make sure the unit tests are passing::

    cd /srv/hubs/fedora-hubs
    tox -e py27-flask011

If all the tests pass, you can start the development webserver and the backend
services with this simple command::

    cd ~
    honcho start

Once the development server is started in the VM, you should be able to access
Fedora Hubs by pointing your web browser to http://localhost:5000/.  If it is
correctly running, you can stop the ``honcho start`` command for now (with
``Ctrl-C``) and disconnect from the VM.
