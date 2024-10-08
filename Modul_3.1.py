from operator import contains

calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [l.upper() for l in list_to_search]
print (string_info('BeZoBrAzIe'))
print (string_info('KinG_Down'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print (is_contains('BaNanA',['LinKin_PArk','HolLa']))
print (is_contains('Coffee', ['cookies', 'cOFfeE', 'LonG']))
print (calls)