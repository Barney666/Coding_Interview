'''
题目描述

柏林州立大学正在举办一场舞会，庆祝它的第 100500 次周年纪念！n 个男孩和 m 个女孩已经在忙于排练华尔兹、小步舞、波罗乃兹舞、四对方舞。

我们知道，很多男孩和女孩的组队 (一个男孩和一个女孩组成一对舞伴)，将被邀请到舞会上。然而，每一组中的两位舞伴技巧的值，至多相差 1 。对于每个男孩，我们知道他的跳舞技巧。类似地，对于每个女孩，我们也知道她的跳舞技巧。

编写代码，判断最大可能的二人组队数目。

输入描述

第一行包含一个整数 n (1 ≤ n ≤ 100) — 男孩的数目
第二行包含一个序列 a1, a2, ..., an (1 ≤ ai ≤ 100)，其中 ai 是第 i 个男孩的跳舞技巧。
第三行包含一个整数 m (1 ≤ m ≤ 100) — 女孩的数目
第四行包含一个序列 b1, b2, ..., bm (1 ≤ bj ≤ 100)，其中 bj 是第 j 个女孩的跳舞技巧。
输出描述

输出一个整数表示跳舞组对的最大可能数目
'''
n=int(input())
ai=list(map(int,input().split()))
m=int(input())
bi=list(map(int, input().split()))
result=0

if n<=m:
    less=ai
    more=bi
else:
    less=bi
    more=ai

record=0
strength=len(less)-1
for skill in less:
    equal=more.count(skill)
    add=more.count(skill + 1)
    sub=more.count(skill - 1)
    if equal!=0:
        more.remove(skill)
        result+=1
    else:
        if add!=0 and sub!=0 and record<=strength:
            less.append(skill)     # 如果+1和-1都可 就让他去后面再排着一会再看 因为可能涉及到分配的问题 让只有一个可以的先来
        else:
            if add==0:
                if sub==0:
                    continue
                else:
                    more.remove(skill - 1)
                    result+=1
            else:
                more.remove(skill+1)
                result+=1
    record+=1

print(result)