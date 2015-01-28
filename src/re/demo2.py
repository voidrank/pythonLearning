import re

# (?:...)
# A non-apturing version of regular parentheses. Matches
# whatever regular expression is inside the parentheses,
# but the substring matched by the group cannot be retieved
# after performing a match or referenced later in the pattern.
m = re.search(r"(?:1(2)3)(123)", "123123")
print(m.group(0, 1, 2))

# (?#...)
# A comment; the contents of the parentheses are simply
# ignored
print(re.match(r"(?#comment)comment", "commentcomment"))
print("")

# (?=...)
# Matches if .. matches net, but doesn't consume any of
# the string. This is called a lookahead assertion
print(re.match(r"Issac (?=Asimov)", "Issac Asimov"))
print(re.match(r"Issac (?=Asimov)", "Issac Asi"))
print("")


# (?!...)
# Matches if ... doesn't matches next, but doesn't
# comsume any of the string. This is called a
# lookahead assertion. For example, Isaac (?=Asimov)
# will match 'Isaac ' only if it's followed by
# 'Asimov'
print(re.match(r"Issac (?!Asimov)", "Issac Asimov"))
print(re.match(r"Issac (?!Asimov)", "Issac Asi"))
print("")

# (?<=...)
# Natches if the current position int the string
# is preceded by a match for ... that ends at the
# current position. This is called a positive
# lookbehind assertion. (?<=abc)def will find a
# match in abcdef, since the lookbehind will back
# up 3 characters and check if the contained patterns
# which start with positive lookbehind assertions will
# not match at the beginning of the string being
# searched; you will most likely want to use search()
# function rather than match() function:
m = re.search(r'(?<=abc)def', 'abcdef')
print(m.group(0))

# (?<!...)
# Matches if the current position in the string
# is not preceded by a match for .... This is called
# a negative lookbehing assertion. Similat to
# positive lookbehind
m = re.search(r'(?<!abc)def', 'abcdef')
m = re.search(r'(?<!abc)def', 'abadef')
print(m.group(0))
print("")

# (?(id/name)yes-pattern|no-pattern)
# Will try to match with yes-pattern if the group
# with given id or name existrs, and with no-pattern
# if it doesn't. no-pattern is optional and can be
# omitted. For examples:
m = re.search(r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', "hahah@fudan.edu.cn")
print(m.group(0, 1, 2))
print("")
# is a poor email matching pattern, which will match
# with '<user@host.com>' as well as 'user@host.com',
# but not with '<user@host.com' nor 'user@host.com>'

# The special sequences consist of '\' and a character
# from the list below. If the ordinary character is
# not on the list, then the resulting RE will match
# second character. For example, \$ matches the
# character '$'

# \number
# Matches the contents of the group of the same number.
# Groups are numbered starting from 1. For example:
m = re.compile(r'(.+) \1')
print(m.match('the the'))
print(m.match('55 55'))
print(m.match('55 55 55'))
print("")

# \A
# Matches only at the start of the string
print(re.search(r"\Abcd", "abcd"))
print("")

# \b
# boundary string
# a sequence of Unicode alohanumeric or
# underscore characters
m = re.compile(r'\bfoo\b')
print(m.search('foobar'))
print(m.search(' foo '))
print(m.search('sdh foo ss'))
print("")

# \B
# Matches the empty string, but only when
# it is not at the beginning or end of a
# word. This means that:
m = re.compile(r'py\B')
print(m.match('python'))
print(m.match('py3'))
print(m.match('py2'))
print(m.match('py'))
print("")
# the opposite of \b

# \d
# Matches any Unicode decimal digit.
m = re.compile(r'\d')
print(m.match("1"))
print("")

# \D
# Matches any character which is not a Unicode
# decimal digit. This is the opposite of \d
m = re.compile(r'\D')
print(m.match("1"))

# \S [^ \t\n\r\f\v]

# \w [a-zA-Z0-9_]

# \W the opposite of \w

# \Z Matches only at the end of the string

# Other escapes supported by Python string literals
# \a \b \f \n \r \t \u \U \v \x \\
# \a \b \f \n \r \t \u \U \v \x \\
