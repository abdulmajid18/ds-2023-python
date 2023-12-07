# For example, given s = "the sky is blue", return "blue is sky the"


def reverse_words(s: str):
    list_str = s.split(' ')
    stack = []

    for i in list_str:
        if i != '':
            stack.append(i)

    new_str = ''
    for i in range(len(stack)):
        new_str += stack.pop()
        if i != len(stack):
            new_str += ' '

    return new_str


def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end -= 1


class Solution:
    def rev_sentence(sentence: str):
        # first split the string into words
        words = sentence.split(' ')

        # then reverse the split string list and join using space
        reverse_sentence = ' '.join(reversed(words))

        # finally return the joined string
        return reverse_sentence

    def rev_stack(self, sentence: str):
        # creating an empty stack
        stack = []

        # pushing words onto the stack
        for word in sentence.split():
            stack.append(word)

        # creating an empty list to store the reversed words
        reversed_words = []

        # popping words off the stack and appending them to the list
        while stack:
            reversed_words.append(stack.pop())

        # joining the reversed words with a space
        reversed_string = " ".join(reversed_words)

        # printing the reversed string
        print(reversed_string)
        return reversed_string

    def reverse(self, s, start, stop):
        while start < stop:
            s[start], s[stop] = s[stop], s[start]
            start += 1
            stop -= 1

    def rev_inplace(self, s: str):
        s = list(s)
        start, stop = 0, len(s) - 1
        self.reverse(s, start, stop)
        start = stop = 0
        while stop < len(s):
            if s[stop] == ' ':
                self.reverse(s, start, stop - 1)
                start = stop + 1
            stop += 1
        self.reverse(s, start, stop - 1)

def main():
    S = "geeks quiz practice code"
    solution = Solution()
    solution.rev_inplace(S)

if __name__ == '__main__':
    main()
    ans = reverse_words("the sky is blue")
    print(ans)
