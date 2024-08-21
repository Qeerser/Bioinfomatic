all_list = []

with open("input.txt", 'r') as file:
    for line in file:
        all_list.append(line.strip())

all_list.sort()

prefix = str(all_list[0][:-1])
answer = ""

with open("output.txt", 'w') as output_file:
    for word in all_list:
        if prefix == word[:-1]:
            answer += word[1:] + ","
        else:
            output_file.write(f"{prefix} -> {answer.rstrip(',')}\n")
            prefix = word[:-1]
            answer = word[1:] + ","

    if answer:
        output_file.write(f"{prefix} -> {answer.rstrip(',')}\n")