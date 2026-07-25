class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # resList = []
        # innerList = []
        # addedList = []
        # i = 0
        # for i in range(len(strs)):
        #     innerList = [strs[i]]
        #     for j in range(i+1, len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             innerList.append(strs[j])
        #     if not any(item in sublist for sublist in resList for item in innerList):
        #         resList.append(innerList)
        # return sorted(resList)
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())

        