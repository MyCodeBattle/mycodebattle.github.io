---
title: C++ 中的赋值操作和自增操作的原子性
layout: post
date: 2016-03-06
categories: 
---

做题时碰到个有争议的题目。

题意大概是这样的。
两个线程并行运行下面的代码，问可能的结果。

~~~
void fun() {
    ++x;
    printf("%d", x);
}
~~~

这题的关键是`++x`在 C++ 中并不像在 Java 中一样不是原子操作。所以这题就变成了考虑 printf 的并行性。

我们来看一下 ++x 的汇编代码。

~~~
int main() {
    int a = 0;
    ++a;
    return 0;
}
~~~

~~~
_main:
LFB9:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$0, 12(%esp)
	addl	$1, 12(%esp)
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
~~~

显然，编译器只用一条语句就完成了自增操作。

而赋值语句

~~~
int main() {
    c = a;
    return 0;
}
~~~

~~~
_main:
LFB8:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$100, 12(%esp)
	movl	$0, 8(%esp)
	movl	12(%esp), %eax
	movl	%eax, 8(%esp)
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
~~~

一共用了三步，所以不是原子的。
