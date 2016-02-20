---
categories: Article
date: 2016-02-05 23:40:21
title: Java中Comparable接口和Comparator接口的区别
tags: [Java]
layout: post
---

这两个接口都能用来排序。
不过如果一个类实现了`Comparable`接口，可以看做这个类支持排序，那么在使用的时候就可以不用比较器。
当类没实现`Comparable`接口的时候，就要用比较器进行比较，也就是`Comparator`。

在重写接口的时候，程序通过返回值判断两个元素的大小。

- 返回值 -1, 说明ele1 < ele2。
- 返回值 1，ele1 > ele2。
- 返回值 = 0，ele1 = ele2。

写到这里本来要写段int降序排序的，然后我才发现Java不提供对基本类型的定义排序（ ＴДＴ）
在我理解中如果返回1就说明这两个元素要换位置。

```java
public class Solution {

    public static void main(String[] args) {
        Integer[] arr = new Integer[20];
        for (int i = 0; i < arr.length; ++i)
            arr[i] = i;
        Arrays.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (o1.compareTo(o2) < 0)
                    return 1;
                else
                    if (o1.equals(o2))
                        return 0;
                return -1;
            }
        });
        for (int u : arr)
            System.out.println(u);
    }
}
```
