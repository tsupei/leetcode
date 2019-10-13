class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        wl = len(words[0])
        wc = len(words)
        if wl > len(s):
            return []
        if wl == len(s) and len(words) == 1:
            if words[0] == s:
                return [0]
        idx_arr = []
        for idx in range(len(s)-wl*wc+1):
            target = s[idx:idx+wl*wc]
            target_list = [target[i:i+wl] for i in range(0,wl*wc,wl)]
            if set(target_list) != set(words):
                continue
            else:
                dic = {}
                for w in target_list:
                    dic.setdefault(w, 0)
                    dic[w] += 1
                for w in words:
                    dic[w] -= 1
                for k, v in dic.items():
                    if v != 0:
                        break
                else:
                    idx_arr.append(idx)
        return idx_arr

                    
                    