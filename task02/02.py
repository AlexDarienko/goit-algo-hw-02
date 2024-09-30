from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо в нижній регістр
    s = ''.join(s.split()).lower()
    char_deque = deque(s)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    test_strings = [
        "А роза упала на лапу Азора",
        "Доход",
        "Паліндром",
        "Я несу гусеня",
        "Де помити мопед"
    ]
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}': {'паліндром' if result else 'не паліндром'}")

if __name__ == "__main__":
    main()
