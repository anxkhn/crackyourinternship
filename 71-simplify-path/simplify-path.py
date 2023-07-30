class Solution:
    def simplifyPath(self, path: str) -> str:
        d_f_list = []
        path = path.split("/")
        for elem in path:
            if d_f_list and elem == "..":
                d_f_list.pop()
            elif elem not in [".", "", ".."]:
                d_f_list.append(elem)
                
        return "/" + "/".join(d_f_list)
