---
title: Lower Bound for Sorting
layout: post
mathjax: true
order: 5
permalink: /lowerbound/
---

# **Lower Bound for Sorting**
# **Sorting Techniques Analysis**

Out of all the sorting techniques that we know of:

- **Bubble Sort** takes $$O(n^2)$$
- **Merge Sort** takes $$O(n \log n)$$

Other sorting algorithms do exist, but the minimum complexity for a sorting algorithm that we know of is $O(n \log n)$.

# **Quest for a Better Sorting Algorithm**

Our quest for a better sorting algorithm begins here. But does a better sorting algorithm even exist?

# **PREREQUISITES:**

## **1. Stirling’s Approximation:**

We are familiar with the factorial $n!$:

$$ n! = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1 $$

Now, approximate every number less than $n$ to be $n$:

Therefore, $$n! \approx n \cdot n \cdot \ldots \cdot n$$.

Hence, $$n! \approx n^n$$.

## **Logarithm of Factorial $$\log(n!)$$:**

$$ \log(n!) = \log(n) + \log(n-1) + \log(n-2) + \ldots + \log(1) $$

$$ \log(n!) = \sum_{k=1}^{n} \log{k} \approx \int_{1}^{n} \log{x} \,dx $$

Solving the integral:

$$ \int_{1}^{n} \log(x) \,dx = n\log(n) - n + 1 $$

Hence, $$\log(n!) \approx O(n \log n)$$.

## **Height of Binary Tree with $$n$$ Nodes is $$\log n$$:**

What do we basically do in the sorting process?

1. Take any two elements, say $$a$$ and $$b$$, and then compare them; either $$a < b$$ or $$b < a$$.
2. Now, accordingly, we compare continuously and continuously and swap if required. (This is a constant operation). For example, consider the initial configuration.
3. We proceed with the compare and swap.
[Alt Text](https://drive.google.com/uc?export=view&id=1DUBObkkSi5-MOKoSHPAB5udotYHPtkay)
# Sorting and Configuration Graphs

We know that for a list of n numbers, we have n! possible configurations.

Now, let’s add a touch of graphs to it. You have a configuration graph where each node is a configuration.

**Question:** How is one configuration linked to another configuration?

**Answer:** An edge appears between any two configurations post comparison and swap if required. Starting with any configuration, we travel across the path, making comparisons and swaps. Towards the end of the entire path, we get our sorted configuration.

If there exists no other better algorithm to sort, the path through the nodes of the configuration must be of length O(n log n).

Now, let us try proving the above statement.

**Graph for the n! Configurations:**
![Alt Text](https://drive.google.com/uc?export=view&id=1TPT2QeFhDnt2Xhfr8)
For the two entities you chose initially, denoted as 'a' and 'b', there are only two possible relationships: either $$ a < b $$ or $$ b < a $$. [Assuming $$ a \neq b $$ for the time being]

![Alt Text](https://drive.google.com/uc?export=view&id=1ce7-6Jadz2t9z7NYSM94O384ypdWGf91)

# Binary Tree Analysis

Don’t you think this is a binary tree?

By the time you reach the sorted configuration, what would be the length of the path traveled? It would be the length of the binary tree.

What is the height of the binary tree? The total configurations are $$ n! $$. Height would then be $$ \log n! $$ (Hint: we derived something useful initially).

Correct! The height of the binary tree = length of the path traveled = $$ \log(n!) \approx n \log n $$.

Now, you know that for any sorting algorithm, it would only traverse down the binary tree of all possible $$ n! $$ configurations. Therefore, the path would be $$ n \log n $$.

Hence, proved.


