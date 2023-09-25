from deque import Deque


def is_palindrome(string):
    if string == '' or string is None:
        return False

    deque = Deque()
    for letter in string:
        if letter.isalnum():
            deque.addTail(letter.lower())

    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True
