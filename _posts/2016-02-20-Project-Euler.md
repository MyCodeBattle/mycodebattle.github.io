---
categories: Solvint-Reports
date: 2015-09-20 20:00:00
title: Project Euler
tags:
layout: post
---

 ## 30. Digit fifth powers ## 

我们可以计算出枚举的上限。6位数的时候，$6\*9^5 = 354294 \leq 999999$，那么极限就是354294。

```python
ans = 0
for i in range(2, 400000):
    s = str(i)
    add = 0
    for j in s:
        add += (ord(j)-ord('0'))**5
    if add == i:
        ans += add
print ans
```

 ## 29. Distinct powers ## 

枚举。

```python
vis = set()
for i in range(2, 101):
    for j in range(2, 101):
        vis.add(i**j)
print len(vis)
```

 ## 27. Number spiral diagonals ## 

枚举。

```python
import math
 
def cal(n, a, b):
    return n*n + a*n + b
 
def is_prime(n):
    if n <= 1:
        return False
    m = int(math.sqrt(n+0.5))
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True
 
prime = set()
max_cnt = 0
 
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        n = 0
        while True:
            if cal(n, a, b) in prime:
                n += 1
            elif is_prime(cal(n, a, b)):
                prime.add(cal(n, a, b))
                n += 1
            else:
                if n > max_cnt:
                    max_cnt = n
                    ans = a*b
                break
print ans
```


 ## 26. Reciprocal cycles ## 

我们知道，x可以被9、99、999等的第一个数整除，1/x的循环节的位数就是9的个数。
那么我们枚举一下即可。

```python
ans = 0
cur_ans = 0
for i in range(1, 1000):
    num = 9
    while i % 2 == 0:
        i /= 2
    while i % 5 == 0:
        i /= 5
    if i == 1:
        continue
    while True:
        if num % i == 0:
            break;
        num = num * 10 + 9
    if len(str(num)) > cur_ans:
        cur_ans = len(str(num))
        ans = i
print ans
```

 ## 25. Reciprocal cycles ## 

暴力。
```python
f = [1, 1]
while True:
    f.append(f[-1]+f[len(f)-2])
    if len(str(f[-1])) == 1000:
        print len(f)
        break
```

 ## 24. Lexicographic permutations ## 

偷懒。如果要更快的话可以用数学规律算出来。

```python
import itertools
 
li = '0123456789'
it = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
mp = list(it)
print mp[1000000-1]
```

 ## 23. Non-abundant sums ## 

暴力枚举。

```python
import math
nums = []
 
def get_abundant_numbers():
    for i in range(2, 28124):
        m = int(math.sqrt(i))
        cur = 0
        for j in range(2, m+1):
            if i % j == 0:
                cur += j
                if j*j != i:
                    cur += i/j
        if cur > i:
            nums.append(i)
 
def solve():
    vis = set()
    ans = 0
    for i in nums:
        for j in nums:
            vis.add(i+j)
    for i in range(1, 28124):
        if i not in vis:
            ans += i
    print ans
 
get_abundant_numbers()
solve()
```

 ## 21. Amicable numbers ## 

暴力枚举约数。

```pytnon
import math
 
mp = {}
aans = 0
def handle(n):
    if mp.has_key(n):
        return mp[n]
    m = int(math.sqrt(n))
    global aans
    ans = 0
    for i in range(2, m+1):
        if n % i == 0:
            ans += i
            if i*i != n:
                ans += n / i
    ans += 1
    mp[n] = ans
for i in range(2, 10000):
    handle(i)
for i in range(2, 10000):
    if mp[i] != i and mp[i] < 10000 and mp[i] != 1 and mp[mp[i]] == i:
        aans += i
print aans
```


 ## 20. Factorial digit sum ## 

暴力。

```python
import math
 
ans = 0
for i in str(math.factorial(100)):
    ans += int(i)
print ans
```
 ## 19. Counting Sundays ## 

枚举。

```python
num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
cur = 5
ans = 0
 
def check(n):
    if n % 100 == 0:
        if n % 400 == 0:
            return True
        else:
            return False
    else:
        return n % 4 == 0
 
for i in range(1901, 2001):
    for j in range(12):
        for k in range(num[j]):
            cur = (cur+1) % 7
            if k == 0 and cur == 6:
                ans += 1
        if check(i) and j == 1:
            cur = (cur+1) % 7
print ans
```


 ## 18. Maximum path sum I ## 

简单dp。

```python
dp = {}
 
def dfs(x, y):
    if (x >= len(mp) or y >= len(mp[x])):
        return 0
    if dp.has_key((x, y)):
        return dp[(x, y)]
    dp[(x, y)] = max(dfs(x+1, y), dfs(x+1, y+1)) + mp[x][y]
    return dp[(x, y)]
 
f = file('Y:\input.txt', 'r')
 
mp = []
for i in f.readlines():
    mp.append([])
    for j in i.split():
        mp[len(mp)-1].append(int(j))
print dfs(0, 0)
```

 ## 17. Number letter counts ## 

先写出全部的单词。统计一下前100的，然后100以上的直接x100 + 前100字母数。
统计前100的时候先统计出前10的，后面直接x10 + 前10.

```python
word = [['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'], ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']]
 
nine_words = 0
for i in word[0]:
    nine_words += len(i)
ans = 0
for i in word[1]:
    ans += len(i)
ans += nine_words
for i in word[2]:
    ans += len(i)*10 + nine_words
ninety_nine = ans
for i in word[0]:
    ans += 100*(len(i)+10) + ninety_nine
    ans -= 3
ans += 11
print ans
```

 ## 16. Power digit sum ## 

暴力。
```python
ans = 0
for i in str(2**1000):
    ans += int(i)
print ans
```

 ## 15. Lattice paths ## 

基础dp。

```python
dp = [[]]
for i in range(30):
    dp.append([])
    for j in range(30):
        dp[i].append(0)
dp[1][1] = 1
for i in range(1, 22):
    for j in range(1, 22):
        dp[i][j] += dp[i][j-1] + dp[i-1][j]
        #print dp[i][j]
print dp[21][21]
```

 ## 14. Longest Collatz sequence ## 

要记忆化搜索。

```python
mp = {}
mp[1] = 0
 
def Solve(n):
    tmp = n
    cnt = 0
    while True:
        if mp.has_key(n):
            mp[tmp] = cnt + mp[n]
            return mp[tmp]
        if n & 1:
            n = 3*n+1
        else:
            n = n / 2
        cnt += 1
 
ans = 0
pos = 0
for i in range(1000001, 0, -1):
    tmp = Solve(i)
    if tmp > ans:
        ans = tmp
        pos = i
print pos
```

 ## 13.Large sum ## 

直接搞。

```python
f = file('Y:\input.txt', 'r')
mp = []
for i in f.readlines():
    mp.append(int(i.strip()))
print str(sum(mp))[:10]
```

 ## 12. Highly divisible triangular number ## 

根据唯一分解定理，约数是（各个质因数数目+1）相乘。

```python
import math
 
def Calc(n):
    ret = 1
    m = int(math.sqrt(n))
    for i in range(2, m+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
        ret *= (cnt+1)
    if (n != 1):
        ret *= 2
    return ret

 
cur = 0
cnt = 1
 
while True:
    cur += cnt
    cnt += 1
    ans = Calc(cur)
    if (ans >= 500):
        print cur
        break
```
 ## 11. Largest product in a grid ## 

枚举。

```python
def Solve():
    dirc = ((0, 1), (1, 0), (1, 1), (1, -1))
    ans = 1
    for i in range(len(mp)):
        for j in range(len(mp)):
            for k in range(len(dirc)):
                tmp = 1
                l = 0
                for l in range(4):
                    x = i + l*dirc[k][0]
                    y = j + l*dirc[k][1]
                    if (x >= len(mp) or y >= len(mp) or x < 0 or y < 0):
                        break;
                    tmp *= int(mp[x][y])
                #print 'row %d col %d ans = %d' % (i, j, tmp)
                ans = max(ans, tmp)
    return ans
 
mp = []
f = file('Y:\input.txt', 'r')
for i in f.readlines():
    mp.append(i.strip().split())
print Solve()
```

 ## 10. Summation of primes ## 

筛。

```python
import math
 
vis = set()
MAXN = int(2e6)
 
def get_prime():
    ans = 0
    m = int(math.sqrt(MAXN+0.5))
    for i in range(2, m+1):
        if i not in vis:
            for j in range(i*i, MAXN, i):
                vis.add(j)
    for i in range(2, MAXN):
        if i not in vis:
            ans += i
    return ans
```
print get_prime()
 
 ## 9. Special Pythagorean triplet ## 

枚举。

```python
for i in range(1001):
    for j in range(i+1, 1001):
        k = 1000 - i - j
        if (i**2 + j**2 == k**2):
            print i*j*k
```

 ## 8. Largest product in a series ## 

枚举。我一直一直以为这是一个矩阵！！！

```python
f = open('Y:\\input.txt', 'r')
string = ''
for line in f.readlines():
    line = line.strip()
    string += line
ans = 0
for i in range(len(string)-12):
    mul = 1
    for j in range(i, i+13):
        mul = mul * int(string[j])
    ans = max(ans, mul)
print ans
```

 ## 7. Sum square difference ## 

$$5050^{2} - \frac{100(100 + 1)(2*100 + 1)}{6}$$

 ## 6. 10001st prime ## 

素数筛。


 ## 5. Smallest multiple ## 
 
输出1~20的最小公倍数
 
```
int main()
{
    int res = 1;
    for (int i = 2; i <= 20; i++)
        res = res / __gcd(res, i) * i;
    cout << res << endl;
    return 0;
}
```

 ## 4. Largest palindrome product ## 
 
输出三位数相乘最大的回文数
 
```c
bool Check(int num)
{
    char str[10];
    MS(str, 0);
    sprintf(str, "%d", num);
    string s = str, comp = s;
    reverse(s.begin(), s.end());
    if (s == comp) return true;
    return false;
}
  
int main()
{
    int ans = 0;
    for (int i = 100; i < 1000; i++)
        for (int j = 100; j < 1000; j++)
            if (Check(i * j)) ans = max(ans, i * j);
    cout << ans << endl;
}
```

 ## 3. Largest prime factor ## 
 
输出给定的数的最大素数项
 
```c
int main()
{
    LL num = 600851475143ll;
    set<int> st;
    for (LL i = 2; i <= (LL)sqrt(600851475143ll); i++)
    {
        while (num % i == 0)
        {
            st.insert(i);
            num /= i;
        }
    }
    cout << *st.rbegin() << endl;
    return 0;
}
```

 ## 2. Even Fibonacci numbers ## 
 
输出400W以内的Fibonacci数列中的偶数项的和
 
```c
int main()
{
    const int MAX = 4e6;
    ULL ans = 0;
    int fir = 1, sec = 2, tmp = 3;
    while (1)
    {
        if (tmp > MAX) break;
        if (!(tmp&1)) ans += tmp;
        fir = sec + tmp;
        swap(fir, tmp);
        swap(fir, sec);
    }
    cout << ans + 2 << endl;
}
```
 
 ## 1. Multiples of 3 and 5 ## 
 
字面意思
 
```c
int main()
{
    int ans = 0;
    for (int i = 1; i < 1000; i++)
        if (i % 5 == 0 || i % 3 == 0) ans += i;
    printf("%d\n", ans);
}
```

