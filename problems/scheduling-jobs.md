# Scheduling Jobs
Given N jobs where every job is represented by following three elements:

1. start Time
1. finish Time.
1. Profit or Value Associated.

Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

Example:

Input: Number of Jobs n = 4

| # | Start Time | Finish Time | Profit |
|---|------------|-------------| -------|
| 1 | 1          | 2           | 50     |
| 2 | 3          | 5           | 20     |
| 3 | 6          | 19          | 100    |
| 4 | 2          | 100         | 200    | 

Output: The maximum profit is 250.

We can get the maximum profit by scheduling jobs 1 and 4. Note that there is 
longer schedules possible Jobs 1, 2 and 3  but the profit with this
schedule is 20+50+100 which is less than 250.