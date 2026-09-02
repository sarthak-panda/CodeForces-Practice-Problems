Use two DFS passes with rerooting:

1. Root the tree at node `1`.
2. First DFS computes:
   - `subtree_size[u]`: number of nodes in `u`'s subtree.
   - `ans[1]`: sum of distances from root to all nodes (accumulate depth).
3. Second DFS reroots answers:
   - If moving root from `u` to child `v`, then:
     - nodes in `v`'s subtree get 1 closer (`subtree_size[v]` nodes)
     - all other nodes get 1 farther (`n - subtree_size[v]` nodes)
   - So:
     `ans[v] = ans[u] - subtree_size[v] + (n - subtree_size[v])`
4. DFS over edges once more to fill all `ans[v]`.

Overall complexity is linear because each edge is processed constant times.
