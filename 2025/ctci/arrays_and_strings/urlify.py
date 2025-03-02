def urlify(string, true_length):
    string = list(string)
    index = len(string)

    for i in range(true_length - 1, -1, -1):
        if string[i] == " ":
            string[index - 3: index] = "%20"
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1

    return "".join(string[index:])
