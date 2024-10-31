**Goal:** Determine the best performing text search algorithm between the three algorithms mentioned below.

**Algorithms:**
- _KMP search_
- _Boyer-Moore search_
- _Rabin-Karp search_

**Text data used for testing:**
- "стаття 1.txt"
- "стаття 2 (1).txt"

Variations:
- when search cannot find results
- when search can find results

**Results:**
After performing the analysis, it seems that at least for the considered cases, for all of them actually, the winning algorithm is the Boyer-Moore string search algorithm.
It consistently outperformed both the KMP and the Rabin-Karp algorithms in cases when the pattern can be found and when it cannot be found.
It has always outperformed the second-best algorithm, KMP search, by at least around three times, while Rabin-Karp took the third place in all tests mentioned.
