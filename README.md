# Comparison of the performance of pattern-matching algorithms in genetics

# Introduction
In the context of DNA sequencing, the aim of this work is to compare the performance of different pattern matching algorithms.

# Pattern Matching Algorithms
We implement three different algorithms and, given a chromosome sequence, test them on patterns of different lengths. 
- Naive 
- Boyer Moore (a python implementation of Ben Langmead,Johns Hopkins University)
- Knuth Morris Pratt
  
|Algo| Worst case | AVG case | Best Case |
|-|-|-|-|
| Naive| O(m*n)| O(m*n)| O(n) |
| Boyer Moore| O(m*n) | O(n) **sublinear** | O(n/m)|
| Knuth Morris Pratt| O(n) | O(n)| O(n)|



m = length of pattern
n = length of sequence
# Sequence and pattern
- Selected Sequence: *Human chromosome 11* from [National Library of Medicine](https://www.ncbi.nlm.nih.gov/guide/genes-expression/) in FASTA format.
- Sets of patterns of variable length: 10, 25, 50, 80, 100, 250, 500, 750,1000, 1250, 1500, 1750, 2000
- For each category of pattern length we create 50 pattern (each pattern is randomly selected from chr11)
 
# Results
Each point represents the **median** running time of each category pattern (50 patterns) 
![image](https://github.com/user-attachments/assets/1f365f1a-5c1b-4aa9-a307-618955870362)




Each point represents the **mean** running time of each category pattern (50 patterns) 
![image](https://github.com/user-attachments/assets/bd41898e-7534-4c64-8352-e259582c4aa1)




- KMP guarantees linear time complexity, making it suitable for situations where consistent performance is crucial.
- Boyer-Moore is often the most efficient in practice, but its worst-case time complexity is the same as the naive approach.

# Bibliography

- **Fast pattern matching in strings**, Knuth, Morris, Pratt, 1977.

- **Genomic data science specialization**, Johns Hopkins University, AA VV (Coursera)

- **Algorithms on Strings, Trees, and sequences**, Dan Gusfield, Computer science and computational biology, 1997




