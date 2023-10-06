#!usr/bin/env python3
from lib.blockvotes import *

latest_height = 71988893;
period_in_blocks = 8640;
max_loops = 100;
count = 0;
voted_parsed = {}
while count < max_loops:
    print("\n> Checking block: " + str(latest_height));
    print("> loop: " + str(count));
    voted_result = check_votes(latest_height, True);

    for vote in voted_result:
        if vote[0] not in voted_parsed:
            voted_parsed[vote[0]] = vote[1]
    count += 1;
    latest_height -= period_in_blocks;


# voted_result = check_votes(latest_height, True);
print(voted_parsed);
print("size of voted_parsed: ");
print(len(voted_parsed));
# show_validators();

