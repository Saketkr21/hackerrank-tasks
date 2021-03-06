import sys, traceback

def lumberjack():
    bright_side_of_death()

def bright_side_of_death():
    return tuple()[0]

# lumberjack()
# exit()
#
# Traceback (most recent call last):
#   File "/Users/dminaev/projects/python/hackerrank-tasks/error_logging.py", line 9, in <module>
#     lumberjack()
#   File "/Users/dminaev/projects/python/hackerrank-tasks/error_logging.py", line 4, in lumberjack
#     bright_side_of_death()
#   File "/Users/dminaev/projects/python/hackerrank-tasks/error_logging.py", line 7, in bright_side_of_death
#     return tuple()[0]
# IndexError: tuple index out of range

try:
    lumberjack()
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print "*** print_tb:"
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    print "*** print_exception:"
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    print "*** print_exc:"
    traceback.print_exc()
    print "*** format_exc, first and last line:"
    formatted_lines = traceback.format_exc().splitlines()
    print formatted_lines[0]
    print formatted_lines[-1]
    print "*** format_exception:"
    print repr(traceback.format_exception(exc_type, exc_value,
                                          exc_traceback))
    print "*** extract_tb:"
    print repr(traceback.extract_tb(exc_traceback))
    print "*** format_tb:"
    print repr(traceback.format_tb(exc_traceback))
    print "*** tb_lineno:", exc_traceback.tb_lineno