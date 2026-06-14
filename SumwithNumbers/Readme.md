
# Coin Change
 
This project contains three classic "coin change" style problems, each solved
three ways to illustrate the progression from plain recursion to dynamic
programming (memoization, then tabulation).
 
All three problems share the same setup: given a list of numbers (which can
be reused any number of times), can it be combined them to add up to a target?
 

 
### can_sum (`cansum.py`)
Returns `True`/`False` — can the target be reached at all?
 
- **`check_if_sum_exist_wodp`** — plain recursion. Tries every number,
  recurses on the remainder, and short-circuits on the first success.
  Correct but exponential time for larger targets.
- **`check_if_sum_exist_dp`** — same recursion, plus a memo dict keyed by
  the target amount. Once a target's answer (`True` or `False`) is known,
  it's cached and reused instantly.
- **`check_if_sum_exist_dp_tabular`** — bottom-up table. `table[i]` says
  whether sum `i` is reachable, built up from `table[0] = True` onward.
### how_sum (`howsum.py`)
Returns 1 valid combination of numbers that sums to the target, or
`None` if impossible.
 
- **`howsum_wdp`** — plain recursion, returns the first combination found.
- **`howsum_dp`** — same recursion with memoization, caching the first
  successful combination found for each target.
- **`howsum_wdp_tabular`** — bottom-up table. `table[i]` holds a valid
  combination summing to `i`, built from `table[0] = []` onward.
### best_how_sum (`best_how_sum.py`)
Returns the *shortest* valid combination of numbers that sums to the
target, or `None` if impossible.
 
- **`best_howsum_wodp`** — plain recursion. Explores every combination and
  keeps the shortest one found.
- **`best_howsum_wdp`** — same recursion with memoization, caching the
  shortest combination found for each target.
- **`best_howsum_wdp_tabular`** — bottom-up table. `table[i]` holds the
  shortest known combination summing to `i`, updated whenever a shorter
  one is found.
## Approach comparison
 
| Approach | How it works | Time complexity |
|---|---|---|
| Plain recursion | Re-solves the same sub-targets repeatedly | Exponential |
| Recursion + memo (top-down DP) | Caches each sub-target's answer the first time it's solved | Polynomial |
| Tabulation (bottom-up DP) | Fills an array from 0 up to the target, no recursion | Polynomial |
 
Each script times its three approaches with `time.time()` so we can see
the speed difference directly — the gap grows quickly as the target
increases.