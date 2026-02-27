#Question 1

#A mutable object is one you can change in place after it’s created. In Python, a list is mutable, so you can edit its contents (replace items, add, remove) without making a brand-new list.
#An immutable object can’t be changed in place.
# A string is immutable, so you can’t change individual characters inside it—any “change” creates a new string instead.Handball analogy
# A list is like your team’s lineup/strategy board during a handball match. The coach can swap players, change positions, or add a new play on the same board.
# That’s mutability: you’re modifying the same thing. A string is like the name printed on the back of a jersey. You can’t change “ALEX” to “MAX” by editing just one letter on that same jersey.
# If you want a different name, you need a new jersey (a new string). That’s immutability.

# LISTS ARE MUTABLE
lineup = ["Left Wing", "Center", "Right Back"]
print("Original lineup:", lineup)

lineup[1] = "Pivot"          # change an element in place
lineup.append("Goalkeeper")  # add an element in place
print("Updated lineup: ", lineup)

# STRINGS ARE IMMUTABLE
jersey_name = "ALEX"
print("\nOriginal jersey name:", jersey_name)

# jersey_name[0] = "M"  # This would cause an error: strings can't be changed in place

new_name = "M" + jersey_name[1:]  # make a NEW string instead
print("New name:           ", new_name)
print("Still original:     ", jersey_name)

#Question 2

def palindrome(word: str) -> bool:
    return word == word[::-1]

nums = [
    "6593036601359343374664733439531066303956",
    "5485839837501070045005400701057389385845",
    "7489617719749244646336564429479177169847",
    "8025833559061079503003059701609553385208",
]

not_pal = [s for s in nums if not palindrome(s)]
print(not_pal)  # strings that are NOT palindromes

#QUESTION 3
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

#Question 4
def is_valid_url(url):
    if type(url) != str:
        return False

    s = url.strip()

    if s == "":
        return False
    if " " in s:
        return False

    pos = s.find("://")
    if pos == -1:
        return False

    scheme = s[:pos]
    rest = s[pos + 3:]

    if scheme != "http" and scheme != "https":
        return False

    slash_pos = rest.find("/")
    if slash_pos == -1:
        host = rest
    else:
        host = rest[:slash_pos]

    if host == "":
        return False

    if "." not in host:
        return False

    parts = host.split(".")
    for part in parts:
        if part == "":
            return False
        if part[0] == "-" or part[-1] == "-":
            return False
        for ch in part:
            if not (("a" <= ch.lower() <= "z") or ("0" <= ch <= "9") or ch == "-"):
                return False

    tld = parts[-1]
    if len(tld) < 2:
        return False
    for ch in tld:
        if not ("a" <= ch.lower() <= "z"):
            return False

    return True
#A URL is basically an address for a website. The main parts we usually see are:
#scheme: tells the type, like http or https
#:// : the separator
#host/domain: like google.com
#optional path: like /about/page
#A valid URL should look like:
#http://something.com or https://something.com (and it can have /path after)

#I just used:

#find() to locate :// and /
#slicing to separate scheme/host/path
#plit(".") to break up the domain
#loops to check every character is allowed
#This way I can catch obvious invalid URLs like:

#issing scheme: google.com
#spaces: https://go ogle.com
#weird domains: https://-abc.com or https://abc..com
#That’s basically how my function decides if it’s valid or not.

def is_valid_url(url):
    # must be a string
    if type(url) != str:
        return False

    s = url.strip()

    # basic invalid cases
    if s == "" or " " in s:
        return False

    # must contain scheme separator
    pos = s.find("://")
    if pos == -1:
        return False

    scheme = s[:pos]
    rest = s[pos + 3:]

    # allow only http/https
    if scheme != "http" and scheme != "https":
        return False

    # rest must start with host (stop at / ? # if present)
    end = len(rest)
    for sep in ["/", "?", "#"]:
        p = rest.find(sep)
        if p != -1 and p < end:
            end = p
    host = rest[:end]

    if host == "":
        return False
    if "." not in host:
        return False

    parts = host.split(".")
    for part in parts:
        if part == "":
            return False
        if part[0] == "-" or part[-1] == "-":
            return False
        for ch in part:
            if not (("a" <= ch.lower() <= "z") or ("0" <= ch <= "9") or ch == "-"):
                return False

    tld = parts[-1]
    if len(tld) < 2:
        return False
    for ch in tld:
        if not ("a" <= ch.lower() <= "z"):
            return False

    return True


# tests (so you SEE it returns)
tests = [
    "https://example.com",
    "http://sub.domain.co.uk/path?x=1",
    "ftp://example.com",
    "https://example",
    "https://exa_mple.com",
    "  https://google.com  ",
    123,
    "https://-bad.com",
    "https://bad-.com",
]
for t in tests:
    print(t, "->", is_valid_url(t))

#Question 5
def longest_word_ending_in_al(filename):
    longest = ""

    try:
        f = open(filename, "r")
    except:
        return ""

    for line in f:
        for w in line.split():
            w = w.strip('.,!?:"\'();[]{}')
            wl = w.lower()
            if len(wl) >= 2 and wl[-2:] == "al":
                if len(w) > len(longest):
                    longest = w

    f.close()
    return longest


# DEMO (this makes a file, then runs the function)
sample_text = (
    "This is a local, global trial.\n"
    "The principal goal is practical; the final signal is not real.\n"
    "animal? several.\n"
)
with open("sample.txt", "w") as f:
    f.write(sample_text)

print(longest_word_ending_in_al("sample.txt"))  # principal

#QUESTION 5
def longest_word_ending_in_al(filename):
    longest = ""

    try:
        f = open(filename, "r")
    except:
        return ""

    for line in f:
        for w in line.split():
            w = w.strip('.,!?:"\'();[]{}').lower()
            if w.endswith("al") and len(w) > len(longest):
                longest = w

    f.close()
    return longest


with open("sample.txt", "w") as f:
    f.write("local global principal practical final real\n")

result = longest_word_ending_in_al("sample.txt")
print("RESULT:", result)  # RESULT: principal

# Explanation:
# - We open the file in read mode.
# - We read it line by line, and for each line we split it into words using split().
# - Each word may have punctuation (like "global,"), so we remove punctuation from the ends using strip(...).
# - We check if the cleaned word ends with "al" using endswith("al").
# - We keep a variable `longest` that stores the longest matching word found so far.
# - At the end we close the file and return `longest`.
# - If the file cannot be opened, we return "".

#QUESTION 7
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# go through the list by index so we can replace values inside the list
for i in range(len(random_numbers)):
    n = random_numbers[i]  # current number

    # if number > 80, replace it by its negative value
    if n > 80:
        random_numbers[i] = -n

    # if number < 40, replace it by sum of its digits (works for 1..39)
    elif n < 40:
        tens = n // 10      # gets the tens digit
        ones = n % 10       # gets the ones digit
        random_numbers[i] = tens + ones

# print the final modified list
print(random_numbers)
#QUESTION8
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#QUESTION 9
print(2+3*6/2)


#Question 10
def days_since_birthday_whole_years(bday, current_year):
    birth_year = int(bday.split("-")[2])

    def is_leap(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

    days = 0
    for year in range(birth_year + 1, current_year):
        days += 366 if is_leap(year) else 365

    return days

print(days_since_birthday_whole_years("10-04-2005", 2026))  # 7305