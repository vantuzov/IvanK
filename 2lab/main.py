

if __name__ == "__main__":
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_and_up = low + up

    def check():
        string = input()
        for i in string:
            if i not in low_and_up:
                print('Вводить можно только латинские буквы.')
                return check()
        return string

    def filter_letters():
        string = check()

        lowercase_count = {}
        uppercase_count = {}
        buffer = []
        letter_order = []

        for char in string:
            char_lower = char.lower()

            if char in low:
                lowercase_count[char_lower] = lowercase_count.get(char_lower, 0) + 1
            else:
                uppercase_count[char_lower] = uppercase_count.get(char_lower, 0) + 1

            buffer.append(char)
            letter_order.append(char_lower)

        result = []
        for char, letter in zip(buffer, letter_order):
            if lowercase_count.get(letter, 0) <= uppercase_count.get(letter, 0):
                result.append(char)

        return ''.join(result)

    result = filter_letters()
    print(result)
