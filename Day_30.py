def abbreviate_word(word):
  """Replaces a long word with an abbreviation.

  Args:
    word: The word to abbreviate.

  Returns:
    The abbreviation of the word, or the word itself if it is not too long.
  """
  if len(word) > 10:
    return word[0] + str(len(word) - 2) + word[-1]
  else:
    return word

def main():
  """Reads words from the input and prints their abbreviations."""
  n = int(input())
  for _ in range(n):
    word = input()
    print(abbreviate_word(word))

if __name__ == "__main__":
  main()