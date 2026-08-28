# Explanation

Use two passes:

1. **Left-to-right pass** to compute `left[i]`: earliest position in `s` where `t[i]` can be matched while keeping subsequence order.
2. **Right-to-left pass** to compute `right[i]`: latest position in `s` where `t[i]` can be matched while keeping subsequence order.

Then maximize `right[i + 1] - left[i]` for all `0 <= i < m - 1`.

This works because `left` gives the earliest valid placement of a prefix and `right` gives the latest valid placement of a suffix, producing the largest gap between two consecutive characters in `t`.

- Time complexity: `O(n + m)`
- Space complexity: `O(m)`
