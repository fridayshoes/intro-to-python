# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  words_without_hyphen = exclude_hyphen_words(words)
  words_ten_or_longer = exclude_short_words(words_without_hyphen)
  words_report = create_word_report(words_ten_or_longer)
  return (f'These words are quite long: {", ".join(words_report)}')

def exclude_hyphen_words(words):
  words_without_hyphen = []
  for word in words:
    if "-" not in word:
      words_without_hyphen.append(word)
  return words_without_hyphen
      
def exclude_short_words(words_without_hyphen):
  words_ten_or_longer = []
  for word in words_without_hyphen:
    if len(word) >= 10:
      words_ten_or_longer.append(word)
  return words_ten_or_longer
  

def create_word_report(words_ten_or_longer):
  words_report = []
  for word in words_ten_or_longer:
    if len(word) >= 15:
      words_report.append((word[:15]) + "...")
    else:
      words_report.append(word)
  return words_report
  

print("Function - exclude hyphen words:")
print(exclude_hyphen_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))

print("Function - exclude short words:")
print(exclude_short_words([
    'hello',
    'nonbiological',
    'Kay',
    'antidisestablishmentarianism'
  ]))

print("Function - create word report:")
print(create_word_report([
    'nonbiological',
    'antidisestablishmentarianism'
  ]))


print("Function - report_long_words:")
print(report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))
  

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
