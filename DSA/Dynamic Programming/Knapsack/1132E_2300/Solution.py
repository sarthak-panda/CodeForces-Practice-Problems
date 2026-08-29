W = int(input())
C = list(map(int, input().split()))

blocks = 0
# STEP 1: Bundle excess items into blocks of weight 840
for i in range(8):
    weight = i + 1
    limit = 840 // weight
    if C[i] > limit:
        extra = (C[i] - limit) // limit
        blocks += extra
        C[i] -= extra * limit

# STEP 2: Use an integer as a DP bitmask for the leftover items
dp = 1
for weight, count in enumerate(C, 1):
    for _ in range(count):
        dp |= (dp << weight)

# STEP 3: Find the best combination
ans = 0
for w in range(14000): # The max possible weight of leftovers is ~13440
    if (dp >> w) & 1 and w <= W:
        # Add as many 840-blocks as will fit without exceeding W
        ans = max(ans, w + min(blocks, (W - w) // 840) * 840)

print(ans)