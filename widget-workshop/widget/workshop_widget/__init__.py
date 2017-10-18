from __future__ import unicode_literals, absolute_import, print_function
from hubs.widgets.base import Widget
from hubs.widgets.view import RootWidgetView
from .bzlib import get_package_reviews
from hubs.widgets.caching import CachedFunction

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

class GetReviews(CachedFunction):

    def execute(self):
        email = self.instance.config["email"]
        if not email:
            return {"reviews":{}}
	total=0
	for val in get_package_reviews(email).values():
	    total+=len(val)
	if total == 0:
	    return {"reviews":{"no_bugs":True}}
	return {"reviews": get_package_reviews(email)}

    def should_invalidate(self, message):
	if ".bugzilla.bug." not in message["topic"]:
            return False
	try:
            product = message['msg']['bug']['product']
	    component = message['msg']['bug']['component']
	    reporter = message['msg']['bug']['creator']
	except KeyError:
	    return False
	return (
	    product == "Fedora" and
	    component == "Package Review" and
	    reporter == self.instance.config["email"]
		)


class BaseView(RootWidgetView):

    def get_context(self, instance, *args, **kwargs):
	get_reviews = GetReviews(instance)
    	return {"reviews": get_reviews()}
       
