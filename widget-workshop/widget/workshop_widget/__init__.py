from __future__ import unicode_literals, absolute_import, print_function
from hubs.widgets.base import Widget
from hubs.widgets.view import RootWidgetView
from .bzlib import get_package_reviews

class WorkshopWidget(Widget):

    name = "workshop-widget"
    position = "both"
    parameters = [
        dict(
            name="email",
            label="Email address",
            help="The Bugzilla email address.",
        ),
    ]


class BaseView(RootWidgetView):

    def get_context(self, instance, *args, **kwargs):
        email = instance.config["email"]
        if not email:
            return {"reviews":{}}
	total=0
	for val in get_package_reviews(email).values():
		total+=len(val)
	if total == 0:
		return {"reviews":{"no_bugs":True}}
	return {"reviews": get_package_reviews(email)}
