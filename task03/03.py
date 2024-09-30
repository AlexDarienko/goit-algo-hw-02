def is_symmetric(s):
    stack = []
    opening = '({['
    closing = ')}]'
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

def main():
    test_strings = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]
    for s in test_strings:
        result = is_symmetric(s)
        print(f"{s}: {'Симетрично' if result else 'Несиметрично'}")

if __name__ == "__main__":
    main()
