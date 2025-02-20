# Have the function most_free_time(strArr) read the strArr parameter being passed which will represent a full day and
# will be filled with events that span from time X to time Y in the day. The format of each event will be
# hh:mmAM/PM-hh:mmAM/PM. For example, strArr may be ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"].
# Your program will have to output the longest amount of free time available between the start of your first event
# and the end of your last event in the format: hh:mm. The start event should be the earliest event in the day and
# the latest event should be the latest event in the day. The output for the previous input would therefore be 01:30
# (with the earliest event in the day starting at 09:10AM and the latest event ending at 02:45PM).
# The input will contain at least 3 events and the events may be out of order.
import datetime


def most_free_time(strArr):
    times = [
        (
            datetime.datetime.strptime(event.split("-")[0], "%I:%M%p"),
            datetime.datetime.strptime(event.split("-")[1], "%I:%M%p"),
        )
        for event in strArr
    ]
    sorted_times = sorted(times, key=lambda x: x[0])
    max_diff = 0
    for i in range(len(sorted_times) - 1):
        diff = (sorted_times[i + 1][0] - sorted_times[i][1]).seconds
        max_diff = max(max_diff, diff)
    hours = int(max_diff / 3600)
    hours = "{:02}".format(hours)
    minutes = int((max_diff % 3600) / 60)
    return f"{hours}:{minutes}"


if __name__ == "__main__":
    print(most_free_time(["10:00AM-12:30PM", "02:00PM-02:45PM", "09:10AM-09:50AM"]))
