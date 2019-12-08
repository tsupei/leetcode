class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        line = [words[0]]
        cur = len(words[0])
        for word in words[1:]:
            if cur + len(word) + 1 <= maxWidth:
                cur += len(word) + 1
                line.append(word)
            else:
                lines.append(line[:])
                line = [word]
                cur = len(word)
        lines.append(line)

        output = []
        print(lines)
        for line in lines[:-1]:
            if len(line) == 1:
                str_arr = line + [" "] * (maxWidth - len(line[0]))
                output.append("".join(str_arr))
                continue
            total = 0
            for word in line:
                total += len(word)
            spaces = maxWidth - total
            if spaces % (len(line)-1) == 0:
                num_each_space = spaces // (len(line)-1)
                space = [" "] * num_each_space
                space = "".join(space)
                output.append(space.join(line))
            else:
                num_each_space = spaces // (len(line)-1)
                space = [" "] * num_each_space
                space = "".join(space)
                num_each_space = spaces % (len(line)-1)
                output_str = ""
                for idx, word in enumerate(line):
                    if idx != len(line)-1:
                        output_str = output_str + word + space 
                        if num_each_space != 0:
                            output_str += " "
                            num_each_space -= 1
                    else:
                        output_str = output_str + word
                output.append(output_str)
        total = 0
        for word in lines[-1]:
            total += len(word)
        total += len(lines[-1]) - 1
        print(total)
        str_arr = lines[-1]
        spaces =  [" "] * (maxWidth - total)
        output.append(" ".join(str_arr) + "".join(spaces))
        return output

if __name__ == "__main__":
    sol = Solution()
    words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    output = sol.fullJustify(words, maxWidth)
    print(output)







