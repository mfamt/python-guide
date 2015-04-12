from dateutil.rrule import rrule, DAILY
from dateutil.parser import parse as date_parse

def day_sequencer(d1, d2):
    """
    `d1` and `d2` are two date strings, preferably formatted as YYYYMMDD

    returns: a list of YYYMMDD-formatted dates between `d1`
       and `d2`, inclusive

    example:
      day_sequencer(20080227, 20080301)
      # => ['20080227', '20080228', '20080229', '20080301']
    """
    day1 = date_parse(str(d1))
    day2 = date_parse(str(d2))
    days = rrule(DAILY, dtstart = day1, until = day2)
    return [d.strftime("%Y%m%d") for d in days]
