class Strstr:
    def Sunday(self, s, t):
        """
        s: source
        t: target
        """
        pass

    def KMP(self, s, t):
        trans = [0] # next

        # preprocess
        max_subfix_len = 0
        for char in t[1:]:
            while char != t[max_subfix_len] and max_subfix_len > 0:
                max_subfix_len = trans[max_subfix_len]

            if char == t[max_subfix_len]:
                max_subfix_len += 1

            trans.append(max_subfix_len)
        print(trans)

        # search
        index_t = 0
        index_s = 0
        while index_s < len(s):
            # print(index_s, index_t)
            if s[index_s] == t[index_t]:
                if index_t == len(t)-1:
                    # print("pipei")
                    return index_s - index_t
                else:
                    index_s += 1
                    index_t += 1
            else:
                if index_t > 0:
                    index_t = trans[index_t-1]
                else:
                    index_s += 1
        return -1

    def Sunday(self, s, t):
        # preprocess
        jump = {}
        for i,c in enumerate(t):
            jump[c] = i
        print(jump)

        # search
        index_t = 0
        index_s = 0
        while index_s < len(s):
            ## forward search
            while s[index_s] == t[index_t]:
                if index_s < len(s):
                    index_s += 1
                    index_t += 1
                    if index_t == len(t) - 1:
                        return index_s - index_t
                else:
                    return -1

            # long jump
            last_index = index_s + len(t) - index_t
            if last_index >= len(s):
                return -1
            else:
                index_t = 0
                if s[last_index] in jump:
                    index_s = last_index - jump[s[last_index]]
                else:
                    index_s = last_index + 1

    def BM(self, s, t):
        # preprocess : bad char
        def PreBmBc(pattern : str, m : int, bmBc : list):
            for i in range(256):
                bmBc[i] = m
            for i in range(m-1):
                bmBc[ord(pattern[i])] = m - 1 - i

        def suffix(pattern, m, suff):
            suff[m - 1] = m
            for i in range(m-2,-1,-1):
                j = i
                while j >= 0 and pattern[j] == pattern[m - 1 - i + j]:
                    j -= 1
                suff[i] = i - j

        def PreBmGs(pattern, m, bmGs):
            # 计算后缀数组
            suffix(pattern, m, suff)
         
            # 先全部赋值为m，包含Case3
            for i in range(m):
                bmGs[i] = m
         
            # Case2
            j = 0
            for i in range(m-1, -1, -1):
                if suff[i] == i + 1:
                    while j < m - 1 - i:
                        if bmGs[j] == m :
                            bmGs[j] = m - 1 - i
                        j += 1

         
            # Case1
            for i in range(m-1):
                bmGs[m - 1 - suff[i]] = m - 1 - i
        def search(pattern, m, text, n):
            # Preprocessing
            PreBmBc(pattern, m, bmBc)
            PreBmGs(pattern, m, bmGs)
         
            # Searching
            j = 0
            while j <= n - m:
                for i in range(m-1,-1,-1):
                    if pattern[i] != text[i + j]:
                        break
                if i < 0 :
                    print("Find it, the position is {}".format(j))
                    j += bmGs[0]
                    return
                else:
                    j += max(bmBc[text[i + j]] - m + 1 + i, bmGs[i])
         
            print("No find.")

        return search(t, len(t), s, len(s))

s = Strstr()
s.BM("asdasd","asd")

# [从有限状态自动机的角度理解KMP算法](https://niuye.info/fms-kmp/)
# [字符串匹配算法总署](https://www.cnblogs.com/Franky-ln/p/5890201.html)
# [BM字符串匹配算法](http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
# [grep之字符串搜索算法Boyer-Moore由浅入深（比KMP快3-5倍）](http://blog.jobbole.com/52830/)
# [字符串匹配算法](https://wenku.baidu.com/view/cecd0b05b7360b4c2e3f6456.html?from=search)
# [最详细最容易理解的BM算法简介](https://wenku.baidu.com/view/dcb81e61647d27284b73517f.html?from=search)
