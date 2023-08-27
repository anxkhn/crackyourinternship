class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = 0
        curr = capacity
        counter = 0
        while plants[-1] != 0:
            # print("i:",i,"counter:",counter,"curr:",curr,plants)
            if plants[i]<= curr:
                curr -= plants[i]
                plants[i] = 0
                counter+=1
                i+=1
            else:
                counter += 2*(i)
                curr = capacity
        return counter
