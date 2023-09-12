class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        em_set = set()
        for i in emails:
            x = i.split("@")
            x[0] = x[0].replace(".","")
            x[0] = x[0].split("+")[0]
            em_set.add(x[0]+"@"+x[1])
        return len(em_set)
        