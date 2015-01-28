import re


print(".")
t = re.compile(r".")
print(t.match("1"))
print(t.split("1234"))
print("")


# start of a string
print("^")
t = re.compile(r"^.")
print(t.match("1234"[1:]))
print(t.match("1234"))
print("")


# end of a string
print("$")
t = re.compile(r".$")
print(t.match("1234"))
print(t.search("1234"))
print(t.split("1234"))
print("")


# ?
# match 0 or 1 repetitions
print("?")
t = re.compile(r"ab?")
print(t.match("a"))
print(t.match("ab"))
print(t.match("abb"))
print("")


# *
# match 0 or more repetitions
print("*")
t = re.compile(r".*")
print(t.match("1234"))
print(t.match(""))
print("")


# +
# match 1 or more repetitions
print("+")
t = re.compile(r".+")
print(t.match("123"))
print(t.match(""))
print("")


# *? +? ??
'''
    The '*', '+' and '?' qualifiers are all greedy,
    they match as much text as possible.
'''


# {m}
# Specifies that exactly m copies of the previous RE
# should be matched
print("{m}")
t = re.compile(r".{3}")
print(t.match("123"))
print(t.match("12"))


# {m,n}
# Causes the resulting RE to
# match from m to n repetitions
print("{m.n}")
t = re.compile(r".{3,5}")
print(t.match("alksdj"))
print(t.match("123"))
print("")


# {m,n}
# Casues the resulting RE to match from m to n
# repetitons of preceding RE, atempting to match as
# few as possible (non-greedy
print("{m,n}?")
t = re.compile(r".{3,5}?")
print(t.match("asjkdhf"))
print(t.match("123"))
print("")


# \ Either escapes special characters (permitting you
# to match characters like '*', '?', and so forth), or
# signals a special sequence
# you should use raw string, because Python's parser
# will pre-parse backslash. So if you don't use rawsting,
# you need to use "//" instead of "/"
print("\\")
t = re.compile(r"\*")
print(t.match("123"))
print(t.match(r"*"))
print("")


print("[] set")
# Used to indicate a set of characters. In a set:
#   Charaters can be listed individually, e.g.:
t = re.compile(r"[amk]")
print(t.search("123a123"))

#   Ranges of characters can be indicated two
#   characters and separating them by a "-",
#   for example:
t = re.compile(r"[a-z]*")
print(t.match("aaa"))

# Special characters lose their special meaning
# inside sets, for example:
t = re.compile(r"[[\](*?)]")
print(t.match("[]?"))
# but except "]"
t = re.compile(r"[a-z]{3,5}?")
print(t.match("asdf"))

#   Character classes such as \w or \S (defined
#   below) are also accepted inside a set, although
#   the characters they match depends on whether
#   ASCII or LOCALE

#   Character that not within a range can be matched
#   by complementing the set. if the first characters
#   of the set if '^', all the characters that are
#   not in the set will be matched. For example:
t = re.compile("[^5]")
print(t.match("5"))
print(t.match("123"))
print("")


# "|"
# A|B where A and B can be arbitrary REs, creates a
# regular expression that match either A or B. An
# arbitraty number of REs can be separared by the
# "|" in this way. This can be used inside groups
# (see below) as well. As the target string is
# scanned, REs separated by "|" are tried from left
# to right. When one pattern completely matches,
# that branch is accepted. This means that once A
# matches, B will not be tested further, even if it
# would produce a longer overall match. In other
# words, the '|' operator is never greedy. To match
# a literal '|', use '\|', or enclose it inside a
# character class, as in [|]
t = re.compile("ab|t")
print(t.match("t"))
print(t.match("abt"))
print("")


# (...)
# Matches whatever regular expression is inside the
# parenthess, and indicates the start and the end
# of a group; the contents of a group can be retrieved
# after a match has been performed, and can be matched
# later in the string with the \number
# To match the literal '(' or ')', use \( or \), or
# enclose them inside a character
print("(..)")
t = re.compile(r"(ab)+")
print(t.match("abb"))
t = re.compile(r"ab+")
print(t.match("abb"))
t = re.compile(r"\(")
print(t.match("(((("))
t = re.match(r"a(b)(c)d", "abcd")
print(t.group(0, 1, 2))
print("")

# (?..)
# This is an extension notation (a '?' following a
# '(' is not meaningful otherwise). The first
# character after the '?' determines what the meaning
# syntax of the construct is. Extensions usually do
# not create a new group; (?P<name>...) is the only
# exception to this rule. Following are the currently
# supported extensions

# (?aiLmsux)
# (one or more letters from the set 'a', 'i', 'L', 'm',
# 's', 'u', 'x'.) The group matches the empty string;
# the letters set the corresponding falsg: re.A
# ----------actually, i don't know what it means-------


# (?P<name>...)
# Similar to regular parentheses, but the substring
# matched by the group is accessible via the symboloc
# group name. Group names must be valid Python identifiers,
# and each group name must be defined only once within
# a regular expression. A symbolic group is also
# a numbered group, just as if the group were not
# named.
t = re.match(r"(?P<quote>(heheda)*?)", "hehedaheheda")
print(t.group(0, 1, "quote"))
t = re.match(r"(?P<quote>(heheda)*)", "hehedaheheda")
print(t.group(0, 1, "quote"))
t = re.match(r"(?P<quote>(heheda){1,1}?)", "hehedaheheda")
print(t.group(0, 1, "quote"))
