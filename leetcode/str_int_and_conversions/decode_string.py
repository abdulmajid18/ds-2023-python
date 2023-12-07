def decode_strings(s):
    stack = []
    for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            sub_str = ''
            while stack[-1] != '[':
                sub_str = stack.pop() + sub_str
            #  remove the [ found
            stack.pop()
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * sub_str)
    return ''.join(stack)