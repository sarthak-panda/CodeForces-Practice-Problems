# Intuition Behind the LCM Knapsack Solution

This solution solves the massive $10^{18}$ capacity knapsack problem in milliseconds by combining math with Python's infinite-precision integers. 

The core challenge is that $W \le 10^{18}$ is far too large for a standard Dynamic Programming (DP) array. However, the item weights are incredibly small (1 through 8). We exploit this using the **Least Common Multiple (LCM)**.

---

**The Magic Constants Explained**

**Why `840`?**
840 is the Least Common Multiple of all possible weights (1, 2, 3, 4, 5, 6, 7, 8). 
This is the perfect "mega-block" size. Because 840 divides perfectly by every weight, you can build an 840-weight block using *only* 3s (280 items), or *only* 7s (120 items). Once bundled, these blocks become universally interchangeable, allowing us to ignore millions of individual items and just count "blocks."

**Why `14000`?**
When we bundle items into 840-blocks, we intentionally leave a small "buffer" pile of loose items. Why? Because 840-blocks are unbreakable. 

* **The "Locked Block" Example:** Imagine your target is $W = 10$. You have 280 weight-3 items and 1 weight-7 item. If you eagerly pack all 280 weight-3 items into a single unbreakable 840-block, you're left with just the 7, missing the perfect $3+7=10$. 
* To prevent this, we leave one block un-converted along with remainder (Note `extra = (C[i] - limit) // limit` here we left that one additional block unconverted), hence we leave at most `2 * (840/w) - 1` items loose per weight to ensure the DP has enough overlapping combinations to bridge any gaps.
* The maximum weight this leftover buffer pile can possibly have is roughly `1680` per item type. 
* With 8 item types: $8 \times 1680 = 13440$. 

The `14000` in the loop is simply a safe, rounded-up ceiling for the absolute maximum possible loose weight.

---

**How the Code Works: Step-by-Step**

**Step 1: The Bundling**
We iterate through all 8 weights. For each weight, we calculate how many items make exactly 840 weight (`limit = 840 // weight`). We leave at least `limit` items behind as our "loose change" buffer, and permanently package the rest into our `blocks` counter.

**Step 2: The Bitmask DP**
Now we only have a tiny handful of loose items left. We use a single Python integer (`dp`) as our DP array.
* `dp = 1` means a weight of `0` is reachable (the 0th bit is 1).
* `dp << weight` takes every reachable sum and adds `weight` to it simultaneously.
* `dp |=` merges the new sums with the old ones. 
Because Python integers can have arbitrary lengths, this processes the entire knapsack DP in just 3 lines of code.

**Step 3: Final Assembly**
We check every reachable weight in our loose pile (from 0 up to 13440). For every valid loose weight `w` that fits inside `W`, we figure out how many 840-blocks we can stuff into the remaining gap (`W - w`). We track the maximum combined total, which gives us the absolute optimal answer.


**Your 3-Step Playbook for the Future:**
- Find the LCM of all available small sizes.
- Create a Buffer. Never greedily pack all your items. Always leave roughly $2 \times$ LCM worth of items in a "loose change" pile.
- DP the Loose Change. Run your standard array or bitmask on the tiny buffer pile, then multiply the LCM blocks to fill the remaining distance.