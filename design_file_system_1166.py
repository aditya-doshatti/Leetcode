'''
1166. Design File System

Medium

You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1

https://leetcode.com/problems/design-file-system/description/
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = Node(None)
        self.allPaths = {}

    def createPath(self, path: str, value: int) -> bool:
        dirs = path.split("/")
        curr, i = self.root, 1
        while i < len(dirs) and dirs[i] in curr.children:
            curr = curr.children[dirs[i]]
            i += 1
        if i == len(dirs) - 1:
            curr.children[dirs[i]] = Node(value)
            self.allPaths[path] = value
            return True
        return False        

    def get(self, path: str) -> int:
        if path in self.allPaths:
            return self.allPaths[path]
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
