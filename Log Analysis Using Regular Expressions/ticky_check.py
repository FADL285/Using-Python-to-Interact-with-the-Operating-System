#!/usr/bin/env python3

import re
import operator

per_user = {}
errors = {}

logfile = 'syslog.log'

with open(logfile, 'r') as f:

    for line in f.readlines():
        result = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", line)

        if result.group(1) == "ERROR":
            if result.group(2) not in errors.keys():
                errors[result.group(2)] = 0

            errors[result.group(2)] += 1

        if result.group(3) not in per_user.keys():
            per_user[result.group(3)] = {}
            per_user[result.group(3)]["INFO"] = 0
            per_user[result.group(3)]["ERROR"] = 0

        if result.group(1) == "INFO":
            per_user[result.group(3)]["INFO"] += 1
        elif result.group(1) == "ERROR":
            per_user[result.group(3)]["ERROR"] += 1

    errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

    per_user = sorted(per_user.items())

errors.insert(0, ('Error', 'Count'))

with open('error_message.csv', 'w') as f:
    for error in errors:
        a, b = error
        f.write(str(a) + ', '+str(b) + '\n')

with open('users_statistics.csv', 'w') as f:
    f.write("Username, INFO, ERROR\n")
    for stats in per_user:
        a, b = stats
        f.write(str(a)+', '+str(b["INFO"])+', '+str(b["ERROR"])+"\n")
