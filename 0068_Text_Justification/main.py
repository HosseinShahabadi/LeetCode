class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        def generateJustifiedLine(inline_words, no_chars) -> str:
            no_spaces = len(inline_words) - 1
            inline_spaces = maxWidth - no_chars
            if no_spaces == 0:
                return inline_words[0] + (' ' * (maxWidth - len(inline_words[0])))
            elif no_spaces == 1:
                return inline_words[0] + (' '*inline_spaces) + inline_words[1]
            
            string = ''
            if inline_spaces % no_spaces == 0:
                space = (' ' * (int(inline_spaces / no_spaces)))
                for word in inline_words[:-1]:
                    string += (word + space)
                string += inline_words[-1]
            else:
                space = (' ' * (int(inline_spaces / no_spaces) + 1))
                for word in inline_words[:(inline_spaces % no_spaces)]:
                    string += (word + space)

                space = (' ' * (int(inline_spaces / no_spaces)))
                for word in inline_words[(inline_spaces % no_spaces):-1]:
                    string += (word + space)
                
                string += inline_words[-1]
            
            return string

        n = len(words)
        ans = []
        pointer = 0
        last_line = False

        while pointer < n:
            inline_words = []
            no_chars = 0
            while no_chars + (len(inline_words) - 1) <= maxWidth:
                if no_chars + len(inline_words) + len(words[pointer]) <= maxWidth:
                    no_chars += len(words[pointer])
                    inline_words.append(words[pointer])
                    pointer += 1
                else:
                    break
                if pointer == n:
                    last_line = True
                    break
            
            if not last_line:
                ans.append(generateJustifiedLine(inline_words, no_chars))
            else:
                string = ''
                for word in inline_words[:-1]:
                    string += (word + ' ')
                string += inline_words[-1]
                string = string + (' ' * (maxWidth - len(string)))
                ans.append(string)
        return ans
