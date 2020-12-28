class BoyerMoore:

    def __init__(self, input_string):
        self.input_string = input_string
        self.characters = 256

    def build_shift_dictionary(self, string, size):
        shift_dictionary = [-1]*self.characters
        for symbol_shift in range(size):
            shift_dictionary[ord(string[symbol_shift])] = symbol_shift
        return shift_dictionary

    def boyer_moore_search(self, pattern_string):
        result = []

        pattern_string_length = len(pattern_string)
        input_string_length = len(self.input_string)

        shift_dictionary = self.build_shift_dictionary(pattern_string, pattern_string_length)

        i = 0
        while i <= (input_string_length - pattern_string_length):
            j = pattern_string_length - 1

            while j >= 0 and pattern_string[j] == self.input_string[i + j]:
                j -= 1

            if j < 0:
                result.append(i)
                if i + pattern_string_length >= input_string_length:
                    break
                next_letter = self.input_string[i + pattern_string_length]
                next_shift = shift_dictionary[ord(next_letter)]
                i += pattern_string_length - next_shift

            else:
                if i + j >= input_string_length:
                    break
                align_letter = self.input_string[i + j]
                next_shift = shift_dictionary[ord(align_letter)]
                i += max(1, j - next_shift)

        return result