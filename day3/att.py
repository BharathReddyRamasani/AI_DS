# A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:
# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.
l1=[i for i in input()]
l2=[i for i in input()]
l3=[i for i in input()];s1=set();s2=set();s3=set()
for i in l1:
    s1.add(i.lower())
for i in l2:
    s2.add(i.lower())
for i in l3:
    s3.add(i.lower())
s=s1|s2|s3
all=s1 & s2 & s3
oneday=(s1^s2)^s3
pair1=s1&s2;pair2=s2&s3;pair3=s1&s3
print(f'exactly one day{oneday}')
print(f'every day{all}')
print(f'day1 and day2{pair1}')
print(f'day2 and day3{pair2}')
print(f'day1 and day3{pair3}')
print(f'total attendees{len(s)}')



