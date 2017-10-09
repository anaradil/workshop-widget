from __future__ import unicode_literals, absolute_import, print_function


from bugzilla import RHBugzilla3 as Bugzilla


BZ_URL = "https://bugzilla.redhat.com/xmlrpc.cgi"
OPEN_BUG_STATUS = [
    'ASSIGNED', 'NEW', 'MODIFIED', 'ON_DEV', 'ON_QA', 'VERIFIED',
    'FAILS_QA', 'RELEASE_PENDING', 'POST', 'REOPENED',
    ]
# Since we don't log into Bugzilla, we don't get email addresses.
UNASSIGNED = "Nobody's working on this, feel free to take it"


def get_package_reviews(email):
    """
    Get the current package review requests in Fedora's Bugzilla for the
    specified email address.
    """
    bzapi = Bugzilla(BZ_URL)
    query = bzapi.build_query(
        product="Fedora",
        component="Package Review",
        reporter=email,
        status=OPEN_BUG_STATUS,
        include_fields=["id", "summary", "status", "assigned_to", "flags"],
        )
    bugs = bzapi.query(query)

    results = dict(
        no_reviewer=[],
        under_review=[],
        review_passed=[],
        )
    for bug in bugs:
        # You can inspect the bug by looking at bug.__dict__
        flags = dict([(f["name"], f["status"]) for f in bug.flags])
        if bug.assigned_to == UNASSIGNED:
            results["no_reviewer"].append(bug)
            continue
        elif flags.get("fedora-review") == "+":
            results["review_passed"].append(bug)
        else:
            results["under_review"].append(bug)

    return results
