class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            counter_s={}
            counter_t={}
            for i,x  in enumerate(s):
                if x in counter_s:
                    counter_s[x]+=1
                else:
                    counter_s[x]=1
                if t[i] in counter_t:
                    counter_t[t[i]]+=1
                else:
                    counter_t[t[i]]=1
            print(counter_s,counter_t)
            for key in counter_s:
                if key in counter_t:
                    if counter_t[key]==counter_s[key]:
                        continue
                    else:
                        return False
                else:
                    return False
            return True


        