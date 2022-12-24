class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}
        
        for i in range(len(s)):
            if s[i] in mapS:
                mapS[s[i]] = mapS.get(s[i]) + 1
            else:
                mapS[s[i]] = 1
            if t[i] in mapT:
                mapT[t[i]] = mapT.get(t[i]) + 1
            else:
                mapT[t[i]] = 1
        
        for i in mapS:
            if mapS.get(i) != mapT.get(i):
                return False
        return True
    