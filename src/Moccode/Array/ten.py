'''
众所周知，皇室家族的名字非常有讲究。而作为研究皇室的历史学家的你，最近接到了一个艰巨的任务——分析王国历史中所有皇室夫人的名字。
王国历史上有n位皇室夫人，方便起见，我们将其从1至n编号。除了1号夫人外，其余夫人的名字均为一个大写字母连接着她母亲的名字。
而1号夫人作为王国的首任王后，她的名字只有一个大写字母。
例如，由于 AENERYS 由 A 与 ENERYS 组成，因此 ENERYS 是 AENERYS 的母亲。相似地，AENERYS 是 DAENERYS 与 YAENERYS 的母亲。
你知道王国历史上所有皇室夫人的姓名与关系，而你需要完成的任务是，对于其他历史学家感兴趣的名字串s，总共有多少位夫人的名字是以s起始的。
例如在样例的皇室族谱中，S 至 AENERYS 的这一支（包含 YS、RYS、ERYS、NERYS 与 ENERYS 这几位夫人）均只有一位女儿。
接下来 AENERYS 有两位女儿，分别是 DAENERYS，以及女儿是 RYAENERYS 的 YAENERYS。
在这个皇室家族内，有两位夫人的名字以 RY 起始，她们是 RYS 与 RYAENERYS。而 ERYS 与 ENERYS 均以 E 起始。名字以 N 起始的仅有一位夫人 NERYS。
同样地，以 S 起始的仅有首位王后 S。而没有任何一位夫人的名字以 AY 起始。

输入描述:
第一行有两个整数n, k,分别代表国历史上皇室夫人总数，以及其他历史学家感兴趣的名字串的个数。
接下来n行描述所有皇室夫人的姓名与关系。第i + 1行描述第i位夫人的资料c_i(符号"_"表示下标)与p_i,其中字符C_i表示她名字的首位字母, p_i为她母亲的编号。对于编号为1的首位王后, P_1 = 0。所有夫人的名字均不重复。
接下来k行,每行为一个大写字母构成的非空串，代表一个其他历史学家感兴趣的名字串。
数据范围：对于1<i≤n,保证有1≤p_i<i。感兴趣的名字串总长不超过10^6。

输出描述:
输出k行，第i行为一个整数，代表总共有多少位夫人的名字是以第i个感兴趣的名字串起始的。
'''


line1=input()
strNum=int(line1.split(" ")[0])
interstNum=int(line1.split(" ")[1])

name=""
for i in range(0, strNum):
    temp=input()
    name+=(temp.split(" ")[0])
name=''.join(reversed(name))    # 字符串反转

interst=[]
for i in range(0,interstNum):
    interst.append(input())

result=[]
for string in interst:
    if len(string)==1 or string[0]!=string[-1]:  # 字符串头尾是否一样
        result.append(name.count(string))
        # 字符串的count有 连着的重复字符 的时候会出现问题【估计是判定完出现一次后会把这个字符删掉再往下找】
        # "1111".count("11")是2而不是3
    else:
        index=0
        time=0
        while True:
            if len(name)-index < len(string):
                break
            if name[index]==string[0]:
                if name[index:index+len(string)]==string:
                    time+=1
            index+=1
        result.append(time)

for item in result:
  print(item)











