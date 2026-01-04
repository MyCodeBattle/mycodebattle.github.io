---
categories: Posts
date: 2014-09-20 00:00:00
title: LeetCode - Surrounded Regions
tags: []
layout: post
---

## 题意

把被包围的O全部变为X

## 思路

这题做得真是纠结啊。。一开始用DFS，一直RERERERERERERE，看了很久代码没问题。后来问了一下hcbbt巨巨，他说可能爆栈了，后来换了BFS才过。

思路就是从边界是O的开始找，能找到的O全部变为T，最后扫描一遍，把T变为O，把O变为X。

PS:看多了ACM里各位巨巨的代码之后再看网上的一些代码，真是。。。太不优雅了。

## 代码


```c++
#define MP(a, b) make_pair(a, b)
typedef pair<int, int> pii;
 
int dir[][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
class Solution {
public:
    void BFS(vector<vector<char> > ∓, int x, int y)
    {
        mp[x][y] = 'T';
        queue<pii> qu;
        qu.push(MP(x, y));
        while (!qu.empty())
        {
            pii cur = qu.front(); qu.pop();
            x = cur.first, y = cur.second;
            for (int i = 0; i < 4; i++)
            {
                int xx = x + dir[i][0], yy = y + dir[i][1];
                if (xx < 0 || xx >= row || yy < 0 || yy >= col || mp[xx][yy] != 'O') continue;
                mp[xx][yy] = 'T';
                qu.push(MP(xx, yy));
            }
        }
    }
    void solve(vector<vector<char> > ∓)
    {
        if (mp.empty() || mp[0].empty()) return;
        row = (int)mp.size(), col = (int)mp[0].size();
        for (int i = 0; i < col; i++)
        {
            if (mp[0][i] == 'O') BFS(mp, 0, i);
            if (mp[row - 1][i] == 'O') BFS(mp, row - 1, i);
        }
        for (int i = 1; i < row - 1; i++)
        {
            if (mp[i][0] == 'O') BFS(mp, i, 0);
            if (mp[i][col - 1] == 'O') BFS(mp, i, col - 1);
        }
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
            {
                if (mp[i][j] == 'T') mp[i][j] = 'O';
                else if (mp[i][j] == 'O') mp[i][j] = 'X';
            }
    }
private:
    int row, col;
};
```