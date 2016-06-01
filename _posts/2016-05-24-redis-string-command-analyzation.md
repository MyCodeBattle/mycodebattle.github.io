---
title: Redis 中 String 中各个命令的执行过程
layout: post
date: 2016-05-24
categories: Redis
---

#set key value [NX] [XX]#

先调用`setKey`。<br>

```
void setKey(redisDb *db, robj *key, robj *val) {
    if (lookupKeyWrite(db,key) == NULL) {
        dbAdd(db,key,val);
    } else {
        dbOverwrite(db,key,val);
    }
    incrRefCount(val);
    removeExpire(db,key);
    signalModifiedKey(db,key);
}
```

然后这时候要判断是覆盖还是新增加的，所以调用了`lookupKeyWrite`，接着调用了`lookupKey`，这里调用了`dictFind`获得了`dictEntry`。

如果`dictEntry`是 NULL，就调用 `dbAdd`，否则调用`dbOverWrite`。

然而写到这里我已经忘了 dictFind 的过程了，顺路写下。
Hash 一发 key，然后与一下容量，拿到桶，然后就是遍历比较了。

来看看`dbAdd`的过程。<br>

```
void dbAdd(redisDb *db, robj *key, robj *val) {
    sds copy = sdsdup(key->ptr);
    int retval = dictAdd(db->dict, copy, val);

    redisAssertWithInfo(NULL,key,retval == REDIS_OK);
    if (val->type == REDIS_LIST) signalListAsReady(db, key);
    if (server.cluster_enabled) slotToKeyAdd(key);
 }
```

显然就是把`key`先弄成一个`sds`，然后加到 db 的 dict 里。

`dbOverWrite`<br>

```
void dbOverwrite(redisDb *db, robj *key, robj *val) {
    dictEntry *de = dictFind(db->dict,key->ptr);

    redisAssertWithInfo(NULL,key,de != NULL);
    dictReplace(db->dict, key->ptr, val);
}
```

# GET #

也是调用了`lookupKey`。


# SETRANGE #

对 int 编码和 embstr 编码，都转换成 raw 编码，然后直接修改。

# GETRANGE #
对于 int 编码，拷贝整数值成字符串，然后返回范围的字符。

# INCRBY/DECRBY #

先 check 一发类型，然后再 check 一下能不能转成 long long，然后再 add，指向新的数。

# INCRBY/DECRBY FLOAT #

例行 check，然后转成`long double`，再转回来覆盖。

# APPEND #

```
o = lookupKeyWrite(c->db,c->argv[1]);
    if (o == NULL) {
        /* Create the key */
        c->argv[2] = tryObjectEncoding(c->argv[2]);
        dbAdd(c->db,c->argv[1],c->argv[2]);
        incrRefCount(c->argv[2]);
        totlen = stringObjectLen(c->argv[2]);
    }
```

也就是说如果是空的 key，直接 add，否则调用`sdscatLen`连接两个 sds.

# STRLEN #

直接查找一发`value`然后调用`stringObjectLen`来得到长度。O(1)，如果是`long long`类型的话要转换成字符串。这里用了一个黑科技。
