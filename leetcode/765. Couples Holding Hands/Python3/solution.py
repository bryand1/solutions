class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        row = [x // 2 for x in row]
        count = 0
        for i in range(0, len(row), 2):
            if row[i] != row[i + 1]:
                j = row.index(row[i], i + 1)
                row[i + 1], row[j] = row[j], row[i + 1]
                count += 1
        return count
