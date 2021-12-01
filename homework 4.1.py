word = input("Введите слово: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")
