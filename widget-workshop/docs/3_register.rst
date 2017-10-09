Register it and add it to your hub
==================================

.. highlight:: shell


Register the widget
-------------------

To register your newly created widget, you will first have to declare the
package on your Vagrant VM's virtualenv. Connect to your VM using Vagrant's SSH
command::

    cd ../fedora-hubs
    vagrant ssh

Then inform the Python virtualenv that your new widget package is available::

    source /srv/hubs/venv/bin/activate
    cd /srv/hubs/widget-workshop/widget/
    python setup.py develop

Don't forget the first command or you will not be using the virtualenv's
Python. Now that Hubs' virtualenv knows about your new widget package, it is
time to declare it in Hubs' configuration file. This is how Hubs knows which
widgets are available.

Edit the ``/srv/hubs/config/hubs_config.py`` file.  Also edit the
``/srv/hubs/fedora-hubs/hubs/default_config.py`` file and copy the contents of
the ``WIDGETS`` list over to the first configuration file. Now add
``workshop_widget:WorkshopWidget`` to this list.

Start Hubs by running the ``honcho start`` command from the user's home
directory. Now you will add this new widget to your own hub.


Add the widget to your hub
--------------------------

1. Go back to your browser on http://localhost:5000/
2. If you are not logged-in, use the login link on the top-right of the page
   and login with your Fedora credentials
3. Click on "My Hub" in the left menu. You are now viewing your personal hub.
4. Click on the "edit page layout" button on the right
5. Click on one of the "+ Add a widget" links
6. In the dropdown, select "Workshop-Widget", and click "Add"

The widget is now added to your hub. If you have added the widget to the right
column, it may appear further down the page. You can click on the "Save
changes" button on the right to leave the edit mode.
