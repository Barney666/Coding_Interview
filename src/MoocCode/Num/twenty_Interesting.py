'''
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。
注意:
输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
'''
'''
然后，观察英文字母结果可知，0，2，4，6，8，这五个英文字母zero,two,four,six,eight，分别对应一个独一无二的字母：z,w,u,x,g 
那我们可以根据这五个字符的数量，先判断出这五个数的数量，然后从原始数据中减去这五个数所带字符的数量。
再判断剩下的数的数量:
观察剩下的英文字母可知，1，3，5，7，9，这五个英文字母one,three,five,seven,nine，也分别对应一个独一无二的字母：o,r,f,s,e
（为什么说nine对应一个e呢，应为处理完前面所有的字符，剩下的e的数量也只能代表nine的数量了）。 
'''

string = input()
dict1 = {"zero": "z", "two": "w", "four": "u", "six": "x", "eight": "g"}
dict2 = {"one": "o", "three": "r", "five": "f", "seven": "s", "nine": "e"}
record = {}
for i in range(0, len(dict1.values())):
    key = list(dict1.keys())[i]
    value = list(dict1.values())[i]
    temp = string.count(value)
    if temp != 0:
        record[key] = temp
        for char in key:
            index = string.index(char)
            string = string[0:index] + string[index + 1:]

for i in range(0, len(dict2.values())):
    key = list(dict2.keys())[i]
    value = list(dict2.values())[i]
    temp = string.count(value)
    if temp != 0:
        record[key] = temp
        for char in key:
            index = string.index(char)
            string = string[0:index] + string[index + 1:]

num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
result = ""
for i in range(0, 10):
    word = num[i]
    time = record.get(word)
    if time != None:
        for j in range(0, time):
            result += str(i)

print(result)
