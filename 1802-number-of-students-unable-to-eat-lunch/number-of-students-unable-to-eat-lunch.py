class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while sandwiches:
            student = students[0]
            
            if student == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                if sandwiches[0] not in students:
                    break

                students.popleft()
                students.append(student)

        return len(students)
    
    