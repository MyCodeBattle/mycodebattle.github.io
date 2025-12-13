---
categories: Posts
date: 2014-07-01 00:00:00
title: 数论部分备忘
tags: []
layout: post
---

## 其他

### 积性函数

φ(n) －欧拉函数，  
μ(n) －莫比乌斯函数，关于非平方数的质因子数目  
gcd(n,k) －最大公因子，当k固定的情况  
d(n) －n的正因子数目  
σ(n) －n的所有正因子之和  
σk(n) － 因子函数，n的所有正因子的k次幂之和，当中k可为任何复数。  
1(n) －不变的函数，定义为 1(n) = 1 （完全积性）  
Id(n) －单位函数，定义为 Id(n) = n（完全积性）  
Idk(n) －幂函数，对于任何复数、实数k，定义为Idk(n) = n^k （完全积性）  
ε(n) －定义为：若n = 1，ε(n)=1；若 n > 1，ε(n)=0。别称为“对于狄利克雷卷积的乘法单位”（完全积性）  
λ(n) －刘维尔函数，关于能整除n的质因子的数目  
γ(n)，定义为γ(n)=(-1)^ω(n)，在此加性函数ω(n)是不同能整除n的质数的数目

### 佩尔方程

形式：$x^2-ny^2=1$，若$n$为正整数。

解法：先找出最小解，然后代入方程

$$x_{i+1} = x_1x_i + ny_1y_i$$

$$y_{i+1} = x_1y_i + y_1x_i$$

### 勾股数公式

#### 证明

先假定x, y, z两两互质，由于x, y互质，故x, y中至少有1个是奇数。下面用反证法证明x和y中有且只有1个奇数。假定x, y都为奇数，设：

$$x = 2a + 1$$  
$$y = 2b + 1$$  
$$x^2 + y^2 = (2a + 1)^2 + (2b + 1)^2 = 4(a^2 + b^2 + a + b) + 2$$

又因为$x^2$和$y^2$是奇数，则$z^2$是偶数，且必能被$4$整除，与上式矛盾，因此$x, y$中只有一个奇数。

假设$x$为奇数，$y$为偶数，则$z$为奇数，$2z$与$2x$的最大公因数为$2$，$2z$和$2x$可分别写作

  * $$2z = (z + x) + (z - x)$$
  * $$2x = (z + x) - (z - x)$$


那么跟据最大公因数性质，$z + x$和$z - x$的最大公因数也为$2$，又因为：

$$(z + x)(z - x) = y^2$$  
两边同除以$4$得：  
$$((z + x) / 2)((z - x) / 2) = (y / 2)^2$$

故可令：

  * $$z + x = 2m^2, z - x = 2n^2$$  
其中$z = m + n$, $x = m - n$（$m$与$n$互质）


则有：$y^2 = z^2 - x^2 = 2m^22n^2 = 4m^2n^2$  
即$y = 2mn$

综上所述，可得到下式：  
$$x = m^2 - n^2, y = 2mn, z = m^2 + n^2$$. (m, n为任意自然数)

#### 公式

$$x = m^2 - n^2, y = 2mn, z = m^2 + n^2. (m, n为任意自然数), x、y互质。$$

### Farey数列

数学上，n阶的法里数列是0和1之间最简分数的数列，由小至大排列，每个分数的分母不大于n。每个法里数列从0开始，至1结束，写作$\dfrac {0} {1}$和$\dfrac {1} {1}$.

$$ \left| F_{n}\right| =\left| F_{n-1}\right| +\varphi \left( n\right) $$

$$ \left| F_{n}\right| =1+\sum _{m=1}^{n}\varphi \left( m\right) $$

### Catalan数另类递推式

$$ f\left( n\right) =\dfrac {f\left( n-1\right) \cdot \left( 4n-2\right) } {n+1} $$

### 最小交换次数

求最少交换次数，使得1~n排列有序。找出环的数目，答案就是n-环数。eg （13254）可分为（1）、（23）、（54）三个环。

例题：UVa 10570

## 模板

### 高斯消元解异或方程组


```c++
//n个灯，m个开关。一个开关控制多个灯，最后输出自由变量的个数。
int A[MAXN][MAXN], M[MAXN][MAXN], n, m;     
LL Gauss()
{
    //row是第几个灯, col是对应的开关. M[row][col] = 1, 说明row这个灯被col这个开关控制
    int row = 0, col = 0, i, j;
    for (; col < m; col++)  //row, col为正在检查的行列
    {
        for (i = row; i < n; i++)   //如果当前这个变量存在，跳出循环
            if (M[i][col]) break;
        if (i == n) continue;   //如果变量为0，继续下一个
        if (i != row)   //如果这个方程不在上一个有序的行下一行，交换这两行
            for (j = col; j <= m; j++) swap(M[i][j], M[row][j]);    
        for (i = row+1; i < n; i++)     //对之后的方程消元
            if (M[i][col])  //如果之后的一条方程里有这个变量，两条方程异或
                for (j = col; j <= m; j++) M[i][j] ^= M[row][j];
        row++;
    }
    for (i = row; i < n; i++)
        if (M[i][m]) return 0;  //如果出现矛盾方程，即|0 0 0 0|1|出现，返回0
    return 1ll << (m-row);      //不然就返回2^自由变量.因为每个自由变量都可以有两种选择
}
```
 

### 求逆元


```c++
LL inv(LL a, LL b)      //计算模n下a的逆。如果不存在逆返回-1
{
    LL d, x, y;
    Extend_Gcd(a, n, d, x, y);
    return d == 1 ? (x+n)%n : -1;
}
```
 

### 中国剩余定理


```c++
void Extend_GCD(LL a, LL b, LL &d, LL &x, LL &y)
{
    if (!b) d = a, x = 1, y = 0;
    else { Extend_GCD(b, a%b, d, y, x); y -= x * (a/b); }
}
 
LL China(int n, int *a, int *m) //n个方程：x≡a[i](mod m[i])
{
    LL M = 1, d, y, x = 0;
    for (int i = 0; i < n; i++) M *= m[i];
    for (int i = 0; i < n; i++)
    {
        LL w = M / m[i];
        Extend_GCD((LL)m[i], w, d, d, y);
        x = (x + y*w*a[i]) % M;
    }
    return (x+M) % M;
    
}
```
 

### 一般的中国剩余定理


```c++
void Extend_Chinese_Remainder(LL &a1, LL &r1)   //计算K mod ai = ri, ri不互素情况
{
    LL a2, r2, x, y, g;
    for (int i = 1; i < 4; i++)
    {
        a2 = a[i]; r2 = r[i];
        Extend_Gcd(a1, a2, g, x, y);
        LL C = r2 - r1, tmp = a2 / g;
        x = C / g * x;
        x = (x%tmp + tmp) % tmp;
        r1 = a1*x + r1;
        a1 = a1 / g * a2;
        r1 = (r1%a1 + a1) % a1;
    }
}
```
 

### Miller Rabin大素数测试和pollard_rho分解因数


```c++
set<LL> fac;
 
LL multi(LL a, LL b, LL m)
{
    LL ans = 0;
    a %= m;
    while(b)
    {
        if(b & 1)
        {
            ans = (ans + a) % m;
            b--;
        }
        b >>= 1;
        a = (a + a) % m;
    }
    return ans;
}
 
LL quick_mod(LL a, LL b, LL m)
{
    LL ans = 1;
    a %= m;
    while(b)
    {
        if(b & 1)
        {
            ans = multi(ans, a, m);
            b--;
        }
        b >>= 1;
        a = multi(a, a, m);
    }
    return ans;
}
 
bool Miller_Rabin(LL n)
{
    if(n == 2) return true;
    if(n < 2 || !(n & 1)) return false;
    LL m = n - 1;
    int k = 0;
    while((m & 1) == 0)
    {
        k++;
        m >>= 1;
    }
    for(int i=0; i<10; i++)
    {
        LL a = rand() % (n - 1) + 1;
        LL x = quick_mod(a, m, n);
        LL y = 0;
        for(int j=0; j<k; j++)
        {
            y = multi(x, x, n);
            if(y == 1 && x != 1 && x != n - 1) return false;
            x = y;
        }
        if(y != 1) return false;
    }
    return true;
}
 
LL pollard_rho(LL n, LL c)
{
    LL i = 1, k = 2;
    LL x = rand() % (n - 1) + 1;
    LL y = x;
    while(true)
    {
        i++;
        x = (multi(x, x, n) + c) % n;
        LL d = __gcd((y - x + n) % n, n);
        if(1 < d && d < n) return d;
        if(y == x) return n;
        if(i == k)
        {
            y = x;
            k <<= 1;
        }
    }
}
 
bool Find(LL n, int c)          //如果是素数返回false
{
    if(n == 1) return false;
    if(Miller_Rabin(n))
    {
        fac.insert(n);
        return false;
    }
    LL p = n;
    LL k = c;
    while(p >= n) p = pollard_rho(p, c--);
    Find(p, k);
    Find(n / p, k);
    return true;
}
```
 

### 快速幂取模


```c++
LL PowMod(LL a, LL m, LL n)
{
    if (m == 1)
        return a % n;
    LL x = PowMod(a, m >> 1, n);
    LL ans = x * x % n;
    if (m & 1)
        ans = ans * a % n;
    return ans;
}
 
LL PowMod(LL a, LL m, LL n)
{
    LL ans = 1;
    while (m > 0)
    {
        if (m & 1)
            ans = ans * a % n;
        a = a * a % n;
        m >>= 1;
    }
    return ans;
}
```
 

### 欧几里得扩展


```c++
void GCDExt(LL a, LL b, LL &d, LL &x, LL &y)
{
    if (!b)
        d = a, x = 1, y = 0;
    else
    {
        GCDExt(b, a % b, d, y, x);
        y -= x * (a / b);
    }
}
```
 

### 欧拉函数


```c++
void PHI_Table()
{
    for (int i = 2; i < MAXN; ++i)
        if (!phi[i])
            for (int j = i; j < MAXN; j += i)
            {
                if (!phi[j]) phi[j] = j;
                phi[j] = phi[j] / i * (i - 1);
            }
}
```
 
```c++
int euler_phi(int n)
{
    int m = (int)sqrt(n + 0.5);
    int ans = n;
    for (int i = 2; i <= m; i++) if (n % i == 0)
    {
        ans = ans / i * (i-1);
        while (n % i == 0) n /= i;
    }
    if (n > 1) ans = ans / n * (n-1);
    return ans;
}
```
 

### 矩阵快速幂计算Fibonacci数列


```c++
#include <bits/stdc++.h>
#define LL long long
using namespace std;
  
struct MATRIX
{
    LL mat[2][2];
};
  
MATRIX ans, temp;
LL mod;
  
MATRIX Calc(MATRIX a, MATRIX b)
{
    MATRIX t;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            t.mat[i][j] = (a.mat[i][0] * b.mat[0][j] + a.mat[i][1] * b.mat[1][j]) % mod;
    return t;
}
  
void Init()
{
    temp.mat[0][0] = 1, temp.mat[0][1] = 1;
    temp.mat[1][0] = 1, temp.mat[1][1] = 0;
    ans.mat[0][0] = 1, ans.mat[1][1] = 1;
    ans.mat[0][1] = ans.mat[1][0] = 0;
}
  
int main()
{
    //freopen("input.txt", "r", stdin);
    int i, j;
    LL n;
    while (~scanf("%lld%lld", &n, &mod))
    {
        Init();
        while (n)
        {
            if (n & 1)
                ans = Calc(temp, ans);
            temp = Calc(temp, temp);
            n >>= 1;
        }
        printf("%lld\n", (ans.mat[1][0]) % mod);
    }
    return 0;
}
```