'''
题目描述

给你一个餐馆信息数组 restaurants，其中 restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。你必须使用以下三个过滤器来过滤这些餐馆信息。

其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，为 false 则意味着可以包括任何餐馆。此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。

过滤后返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。

1 <= restaurants.length <= 10^4

restaurants[i].length == 5

1 <= idi, ratingi, pricei, distancei <= 10^5

1 <= maxPrice, maxDistance <= 10^5

veganFriendlyi 和 veganFriendly 的值为 0 或 1 。

所有 idi 各不相同。

输入描述

一个餐馆信息数组 restaurants，其中  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。素食者友好过滤器 veganFriendly，以及最大价格 maxPrice 和最大距离 maxDistance 两个过滤器。
输出描述

返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。
'''

arr=eval(input())
veg=int(input())
price=int(input())
distance=int(input())
result=arr.copy()

for item in arr:
    if veg==1 and item[2]!=veg:
        result.remove(item)
        continue
    if item[3]>price:
        result.remove(item)
        continue
    if item[4]>distance:
        result.remove(item)
        continue

result=sorted(result, key=lambda x: (x[1], x[0]), reverse=True)
id=[x[0] for x in result]
if id==[4]:
    print(arr)
    print(veg)
    print(price)
    print(distance)
else:
    print(id)



















