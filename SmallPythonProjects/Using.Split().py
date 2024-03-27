message = input('> ')
words = message.split() #splits string into separate words, with or without a separator
emojis = {
    ":)": " 😊",
    ":(": " ☹",
    ";)": " 😏"
}
output = ' '
for word in words:
    output += emojis.get(word, word)
print(output)
