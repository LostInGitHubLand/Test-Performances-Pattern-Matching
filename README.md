# Test-Performances-Pattern-Matching
Algorithms for DNA sequencing
# Introduction
In the context of DNA sequencing, the aim of this work is to compare the performance of different pattern matching algorithms.

# Algorithms,
We implement three different algorithms and, given a chromosome sequence, test them on patterns of different lengths. 
- Naive
- Boyer Moore
- Knuth Morris Pratt

# Sequence and pattern
- Selected Sequence: *Human chromosome 11*
- Sets of patterns of variable length: 10, 25, 50, 80, 100, 250, 500, 750,1000, 1250, 1500, 1750, 2000
- For each category of pattern length we create 50 pattern (each pattern is randomly selected from chr11)
- 
# Results
Each point represents the median running time of each category pattern (50 patterns) 
![image](https://github.com/user-attachments/assets/cf81901b-b576-4620-8198-54085edf1a9a)

Each point represents the avg running time of each category pattern (50 patterns) 
![image](https://github.com/user-attachments/assets/25fb8c50-3b1b-4505-b23c-8284e18b3a0e)

