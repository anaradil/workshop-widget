Get more interesting data
=========================

Having a configurable static HTML output may be useful in some cases, but
that's not where Hubs really shines. In this section, you will modify the
widget to output the status of a user's package reviews in Fedora's Bugzilla.

You will be using a simple function calling Bugzilla's XMLRPC interface via the
`python-bugzilla <https://github.com/python-bugzilla/python-bugzilla>`_
library. This function is in the ``workshop_widget/bzlib.py`` module, go ahead
and have a look. It takes the Bugzilla user's email address as an input, and
outputs a dictionary containing the bug objects sorted by review status in the
following lists::

    {
        no_reviewer: [],
        under_review: [],
        review_passed: [],
    }


Updating the widget class
-------------------------

To make use of this function, add the following line to the imports section in
``workshop_widgtet/__init__.py``::

    from .bzlib import get_package_reviews

The function takes the Bugzilla email address as an input, you are thus going
to need it as a widget parameter. Edit the ``WorkshopWidget.parameters`` list
to look like this::

    parameters = [
        dict(
            name="email",
            label="Email address",
            help="The Bugzilla email address.",
        ),
    ]

You could have kept the ``text`` parameter and added ``email``, but since it's
not going to be used anymore, just remove it.


Updating the view
-----------------

Now modify the ``get_context()`` method in your widget's root view to look like
this::

    def get_context(self, instance, *args, **kwargs):
        email = instance.config["email"]
        if not email:
            return {"reviews": {}}
        return {"reviews": get_package_reviews(email)}

It's now using the ``email`` parameter, and outputs the result of
``get_package_reviews()`` in a dictionary which will be available in the Jinja2
template.


Updating the template
---------------------

Modify the template to look like this:

.. code-block:: jinja

    {% extends "panel.html" %}

    {% block content %}

    {% if reviews.no_reviewer %}
        <strong>No reviewer:</strong>
        <ul>
        {% for bug in reviews.no_reviewer %}
            <li>
                <a href="{{ bug.weburl }}">#{{ bug.id }}</a>
                {{ bug.summary }}
            </li>
        {% endfor %}
        </ul>
    {% endif %}

    {% endblock %}

This only generates the contents of the ``no_reviewer`` list. Add sections for
the ``under_review`` and ``review_passed`` lists too (this is left as an
exercice). If you're a Jinja2 expert, you may choose to `use a macro
<http://jinja.pocoo.org/docs/2.9/templates/#macros>`_ here.


Updating and restarting the server
----------------------------------

The widget code is now ready, but it has a new dependency: the
``python-bugzilla`` library. You will have to edit your widget's ``setup.py``
file and add it in the ``install_requires`` list. Once this is done, go back to
the VM and update the virtualenv by running:

.. code-block:: shell

    source /srv/hubs/venv/bin/activate
    cd /srv/hubs/widget-workshop/widget/
    python setup.py develop

Then go back to the home directory and run ``honcho start`` again.


Trying it out
-------------

Refresh the webrowser's page. You should now see an empty widget where the text
used to be. This is normal, since the email address hasn't been configured yet.
There is a way to avoid displaying the widget entirely if there is no data, or
if it is not configured, but we won't go into that in this workshop.

Click on the widget's edit icon (top-right corner). Fill in your Bugzilla email
address and click "Save". The page should refresh and show your review
requests. If the page is still empty, it means you currently have no active
review requests. You can modify the Jinja2 template to show a friendly message
in that situation. This is also left as an exercise for you.

You can also use somebody else's Bugzilla email address. You can use
`this Bugzilla query`_ to choose a reporter that currently has an interesting
variety of requests.

.. _this Bugzilla query: https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&bug_status=POST&bug_status=MODIFIED&bug_status=ON_DEV&bug_status=ON_QA&bug_status=VERIFIED&bug_status=RELEASE_PENDING&classification=Fedora&columnlist=reporter%2Cshort_desc%2Cassigned_to%2Cchangeddate%2Cflagtypes.name&component=Package%20Review&email1=aurelien%40bompard.org&emailtype1=exact&list_id=7652963&product=Fedora&query_based_on=&query_format=advanced


If you have an error
--------------------

If you have an error in the UI (message ``got an error trying to display this
widget``) or in the console (a *Traceback*), look at the console where you ran
the ``honcho start`` command. If there's a *Traceback* there, read the lines
and look where there's one that points to a file in your code directory. If the
line in the file and the message don't help, feel free to `reach out to me
<mailto:abompard@fedoraproject.org>`_.
