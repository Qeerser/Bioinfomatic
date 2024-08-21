input_string = ""
with open('input.txt', 'r') as files:
    # Read the entire file
    input_string = files.read()

mapping = {}

with open('text.txt', 'r') as file:
    for line in file:
        words = line.split()
        mapping.update({words[i]: words[i + 1] for i in range(0, len(words), 2)})

result, index = "", 0
while index < len(input_string):
    key = input_string[index:index + 3]
    word = mapping.get(key, "Stop")
    if word == "Stop":
        break
    result += word
    index += 3

with open("output.txt", 'w') as file:
    file.write(result)