# Úkol 1: TWO SUM

function twoSum(nums, target) {
    const numIndicesMap = {};

    for(let i = 0;i<nums.length;i++) {
        const complement = target - nums[i];

        if(numIndicesMap.hasOwnProperty(complement)) {
            return
            [numIndicesMap[complement],i];
        }
        numIdicesMap[nums[i]] = i;
    }
    return[];
}

console.log(twoSum([2,7,11,15],9));
console.log(twoSum([3,2,4],6));
console.log(twoSum([3,3],6));

# Úkol 2: PALINDROME NUMBER

def isPalindrome(x)
if x < 0:
    return False

reversed_x = 0
original_x = x
while x !=0:
    digit = x % 10
    reversed_x = reversed_x * 10 + digit
    x//= 10

    return original_x == reversed_x

    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))

# Úkol 3: ROMAN TO INTEGER

def romanToInt(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

     for char in s[::-1]: 
        value = roman_values[char]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result


print(romanToInt("III"))     
print(romanToInt("LVIII"))   
print(romanToInt("MCMXCIV")) 

# Úkol 4: LONGEST COMMON PREFIX

def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()

    prefix = ""
    for char1, char2 in zip(strs[0], strs[-1]):
        if char1 == char2:
            prefix += char1
        else:
            break

    return prefix

    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))

# Úkol 5: VALID PARENTHESES

def isValid(s):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
        else:
            return False

    return not stack

print(isValid("()"))       
print(isValid("()[]{}")) 
print(isValid("(]"))        

# Úkol 6: MERGED TOW SORTED LISTS
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

result = mergeTwoLists(list1, list2)

while result:
    print(result.val, end=" ")
    result = result.next

# Úkol 7: REMOVE ELEMENT
def removeElement(nums, val):
    if not nums:
        return 0

    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1

    return left


nums1 = [3, 2, 2, 3]
val1 = 3
expectedNums1 = [2, 2]
k1 = removeElement(nums1, val1)
assert k1 == len(expectedNums1)
print(nums1[:k1])  

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
expectedNums2 = [0, 1, 4, 0, 3]
k2 = removeElement(nums2, val2)
assert k2 == len(expectedNums2)
print(nums2[:k2]) 