# Have the function counting_minutes(str) take the str parameter being passed which will be two times (each properly
# formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two
# times. The time will be in a 12 hour clock format.
# For example: if str is 9:00am-10:00am then the output should be 60.
# If str is 1:00pm-11:00am the output should be 1320.


import datetime


def get_minutes(time_str):
    t = datetime.datetime.strptime(time_str, "%I:%M%p")
    minutes = t.hour * 60 + t.minute
    return minutes


def counting_minutes(time_str):
    time_1 = time_str.split("-")[0]
    time_2 = time_str.split("-")[1]
    time_1 = get_minutes(time_1)
    time_2 = get_minutes(time_2)
    diff = time_2 - time_1
    diff = diff + 24 * 60 if diff < 0 else diff
    return diff


if __name__ == "__main__":
    print(counting_minutes("9:00am-10:00am"))
    print(counting_minutes("1:00pm-11:00am"))
