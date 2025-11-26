# your code goes here!

import re

class EmailAddressParser:
    # email pattern that does NOT include spaces
    email_regex = re.compile(
        r"[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # find emails one-by-one (no merging across spaces)
        found = self.email_regex.findall(self.emails)

        # unique + sorted
        unique_sorted = sorted(set(found))

        return unique_sorted
