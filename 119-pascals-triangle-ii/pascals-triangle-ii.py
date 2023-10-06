class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)

        def nCr(n, r):
            if r > n:
                return 0
            else:
                return factorial(n) // (factorial(r) * factorial(n - r))
        main_list = []
        for i in range(rowIndex+1):
            main_list.append(nCr(rowIndex,i))
        return(main_list)

        