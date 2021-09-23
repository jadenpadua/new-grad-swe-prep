"""
Write a function to crush candy in one dimensional board. In candy crushing games,
groups of like items are removed from the board. In this problem, any sequence of 3
or more like items should be removed and any items adjacent to that sequence should 
now be considered adjacent to each other. This process should be repeated as many time as possible. 
You should greedily remove characters from left to right.

Example 1:

Input: "aaabbbc"
Output: "c"
Explanation:
1. Remove 3 'a': "aaabbbbc" => "bbbbc"
2. Remove 4 'b': "bbbbc" => "c"
Example 2:

Input: "aabbbacd"
Output: "cd"
Explanation:
1. Remove 3 'b': "aabbbacd" => "aaacd"
2. Remove 3 'a': "aaacd" => "cd"
Example 3:

Input: "aabbccddeeedcba"
Output: ""
Explanation:
1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
3. Remove 3 'c': "aabbcccba" => "aabbba"
4. Remove 3 'b': "aabbba" => "aaa"
5. Remove 3 'a': "aaa" => ""
Example 4:

Input: "aaabbbacd"
Output: "acd"
Explanation:
1. Remove 3 'a': "aaabbbacd" => "bbbacd"
2. Remove 3 'b': "bbbacd" => "acd"
"""
def crush(s):
    if not s: return s

    stack = []
    # Store char and count of each char in stack
    stack.append([s[0], 1])
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            # pop entry from stack if greater than three
            if stack[-1][1] >= 3:
                stack.pop()
            # case where we popped an item from stack and the curr char is same as new top of stack
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
        else:
            stack[-1][1] += 1
    # if there are three or more chars still in the stack that havent been removed by next char pointer
    if stack[-1][1] >= 3:
        stack.pop()

    res = []
    for entry in stack:
        entry_string = entry[0] * entry[1]
        res.append(entry_string)
    return ''.join(res)

print(crush("aaabbbc"))
print(crush("aaabbbacd"))
print(crush("aabbccddeeedcba"))
