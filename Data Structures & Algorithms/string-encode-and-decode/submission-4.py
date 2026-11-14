class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:

        result, index = [], 0

        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            w_len = int(s[index:j])
            word = s[j + 1: j + 1 + w_len]
            result.append(word)
            index = j + 1 + w_len
        return result
