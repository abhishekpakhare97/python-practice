message = input("Enter message : ")
words = message.split(" ")

emoji = {
    ":)" : "😊",
    ":(" :"😞",
    "<3" : "❤"
}
output = ""
for emoji_detect in words:
    output += emoji.get(emoji_detect,emoji_detect)+ " "
print(output)