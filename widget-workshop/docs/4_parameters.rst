Add parameters
==============

Click on "edit page layout" again to go back to the edit mode. By clicking on
the top-right cog-like icon in your widget, you bring up the widget's
configuration panel. It currently reads "Nothing to configure".

Widgets on a hub (called widget "instances") can have parameters, and multiple
widget instances on the same hub can have different values for those
parameters. It is up to the widget class to declare what parameters it accepts.


Add the parameter
-----------------

Add the following attribute to ``WorkshopWidget`` in
``workshop_widget/__init__.py`` to make it look like::

    class WorkshopWidget(Widget):

        name = "workshop-widget"
        position = "both"
        parameters = [
            dict(
                name="text",
                label="Text",
                default="The workshop widget",
                help="The text to display.",
            ),
        ]


Update the view
---------------

Now that the parameter is declared, modify the root view to take it into
account. It should look like::

    class BaseView(RootWidgetView):

        def get_context(self, instance, *args, **kwargs):
            return dict(text=instance.config["text"])

You have overridden the ``get_context()`` method. It takes the widget instance
as first argument. This ``instance`` argument is a database record, an instance
of the ``hubs.models.Widget`` class. The values of the widget parameters are
available in the ``instance.config`` dictionary.

The return value of the ``get_context()`` method will be used as context to
render the view template.


Update the template
-------------------

Modify the ``workshop_widget/templates/root.html`` template to use the new
variable, like this:

.. code-block:: jinja

    {% extends "panel.html" %}

    {% block content %}
    {{ text }}
    {% endblock %}


Restart the server
------------------

From now on, it will be easier to have one terminal tab logged in the VM with
``vagrant ssh``, and one terminal tab opened in the code directory
(``widget-workshop/widget/workshop_widget``). The contents of the code
directory will be automatically synced to the VM in the
``/srv/hubs/widget-workshop/widget/workshop_widget`` directory, so you don't
need to edit the files inside the VM.

Start the server again with ``honcho start`` on the VM, go back to your hub in
your web browser and reload the page. Clicking on the cog icon now brings up a
dialog with a text field. Change the text and click on "Save". The widget's
text has now been updated.
