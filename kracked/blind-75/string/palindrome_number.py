def isPalindrome(x):
    if x < 1:
        return False

    div = 1
    while x >= div * 10:
        div *= 10

    while x:
        right = x % 10
        left = x // div

        if left != right: return False

        x = (x % div) // 10
        div = div / 100
    return True
