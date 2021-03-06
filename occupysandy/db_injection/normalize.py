# normalize.py
'''
Contains functions for normalizing data in specific ways
These functions are called when importing raw data
and when querying data
'''

'''
parseDefault()
string: value to be converted into a string
return: string
If no normalize function is specified the default will be run
Takes one argument and outputs a string
'''
def parseDefault(string):
	return str(string)


'''
parseBool()
string: value to be parsed, normally a string
return: bool
Takes one argument which it evaluates to true or false
should test against common vernacular: yes, no, nope, yeah ...
as well as: true, false, "0", "1" ...
'''
def parseBool(string):
	return parseDefault(string)

'''
parseInt()
string: possible integer value trapped in a string (or worse!)
return: int OR string
Takes one argument and attempts to convert it to an into
an integer. If input can't be converted into an int return string.
'''
def parseInt(string):
	return parseDefault(string)

'''
parseEmail()
string: possible email value
return: string (email address)
'''
def parseEmail(string):
	return parseDefault(string)

'''
parseMultiChoice()
string: string that is part of a set
limit: list of choices to match against
return: unchanged string OR -1 OR null on blank 
Takes two arguments, a normal string that may or may not be part of a set
if limit is true it is expected to be a list of possible answers to limit
the string to. If string is not in limit, return -1
'''
def parseMultiChoice(string, limit = False):
	if string == '' : return parseDefault(string)


'''
parseDate()
date: string, possibly with some kind of date
return: formatted date OR original string
Takes one that could be a well formatted date, or a sloppy
mess with some semblance of a date structure... find the date or
give up and return the original string
'''
def parseDate(date):
	return parseDefault(string)


'''
parseLocation()
string: string, possibly with some kind of geographic information
anon: bool, should the output be precise or anonymous (default True)
return: lat/long or some kind of standard geo data
Takes two arguments, the string is an address, city, state, region, or country
let's go ahead and assume it's in a horrible format
this string gets turned into geo data
if anon is True then returned geo data should be obfuscated (generalized to neighborhood level)
'''
def parseLocation(string, anon = True):
	return parseDefault(string)

'''
parseNotApplicable()
string: value to be parsed
allowed: bool default: True
return: 'n/a' OR null OR string
Takes two arguments, the string to be parsed and a bool.
string is tested against common vernacular responses of n/a
if we can safely say a string is n/a then normalize it
if allowed is False and answer is n/a return null
if string is not marked n/a return unaltered
'''
def parseNotApplicable(string, allowed = True):
	#I'm giving this one a try for fun
	synonym = { 'nan', 'na' , 'n-a' , 'n/a' , 'notapplicable' , 'not applicable' , 'not available', 'no answer' }
	
	if str(string).lower().strip() in synonym and str(string).strip() != '':
		if allowed:
			return 'NaN'
		else:
			return None
	else:
		return string

'''
Can you think of any other parse functions?
Add them and be automatically registered to win a high five
'''


'''
because the config file will pass in the function names as strings we need
to create this dict to assist when calling our functions
'''
funcdict = {
  'parseDefault': parseDefault,
  'parseBool': parseBool,
  'parseInt': parseInt,
  'parseEmail': parseEmail,
  'parseMultiChoice': parseMultiChoice,
  'parseDate': parseDate,
  'parseLocation': parseLocation,
  'parseNotApplicable': parseNotApplicable
}