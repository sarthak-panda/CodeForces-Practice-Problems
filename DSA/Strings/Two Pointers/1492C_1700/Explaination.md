# Solution Explanation

### Idea

We need to choose positions `p1 < p2 < ... < pm` in `s` such that:

```text
s[p1] = t[0]
s[p2] = t[1]
...
s[pm] = t[m-1]
````

We want to maximize the difference between two consecutive positions:

```text
max(p[i+1] - p[i])
```

Consider the simple case:

```text
s = abcdeabc
t = ac
```

We need positions `p1 < p2` such that:

```text
s[p1] = 'a'
s[p2] = 'c'
```

To maximize `p2 - p1`, we want:

* the **leftmost possible position** for `'a'`
* the **rightmost possible position** for `'c'`

Here:

```text
s = a b c d e a b c
    ↑             ↑
    0             7
```

So the maximum width is:

```text
7 - 0 = 7
```

For a longer `t`, we can apply exactly the same idea to every pair of consecutive characters.

For example, if:

```text
t = abc
```

we can split it as:

```text
a | bc
ab | c
```

For `a | bc`, we want `a` as far left as possible and the `bc` subsequence as far right as possible.

For `ab | c`, we want the `ab` subsequence as far left as possible and `c` as far right as possible.

This leads to two arrays.

### Approach

* `L[i]` = earliest position where `t[i]` can be matched when matching `t` from left to right.
* `R[i]` = latest position where `t[i]` can be matched when matching `t` from right to left.

We build `L` by scanning `s` from left to right.

We build `R` by scanning `s` from right to left.

For every adjacent pair `t[i]` and `t[i+1]`, the largest possible gap is:

```text
R[i+1] - L[i]
```

Therefore:

```text
answer = max(R[i+1] - L[i])
```

over all `i`.

### Complexity

* Time: `O(n)`
* Space: `O(m)`
