def to_lowercase(word):
  return word.lower()
def to_uppercase(word):
  return word.upper()
def solve(word):
  uppercase_count = 0
  lowercase_count = 0
  for letter in word:
    if letter.isupper():
      uppercase_count += 1
    elif letter.islower():
      lowercase_count += 1
  if uppercase_count > lowercase_count:
    return to_uppercase(word)
  else:
    return to_lowercase(word)
if __name__ == "__main__":
  word = input()
  print(solve(word))