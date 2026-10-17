class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mymap = {}

        for i in range(len(nums2)):
            mymap[nums2[i]] = i

        sol = []

        for i in range(len(nums1)):
            ind = mymap[nums1[i]]
            found = False

            for j in range(ind + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    sol.append(nums2[j])
                    found = True
                    break

            if not found:
                sol.append(-1)

        return sol
