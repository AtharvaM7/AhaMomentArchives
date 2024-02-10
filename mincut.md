# Min-Cut 
## Building Blocks 
- If r > a and s < b, then $$\frac{a}{b} < \frac{r}{s}$$.

- In a graph of n nodes if l is the least degree in the graph, then $$|E| \geq \frac{ln}{2}$$.

- The limit as n approaches infinity:
  $$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$$

- Say the probability of an event happening is $$p(E) = \frac{1}{k},$$ then the probability of an event not occurring is $$p(\bar{E}) = 1 - \frac{1}{k},$$ and the probability of an event not happening twice is $$P(\bar {E}) = \left(1 - \frac{1}{k}\right)^2.$$After repeating a process n times, the probability of an event not happening is $$P(\bar{E}) = \left(1 - \frac{1}{k}\right)^n$$.

#### Example
The probability of a doctor contracting sars-cov-2 is $\frac{1}{100}$.The probabilioty of him/her contracting the infection after meeting 100 patients is ______. 

Let E be the event of not getting infected.Then, $$p(E)=1- \frac{1}{100}.$$The probability of him not contracting the virus after meeting 100 patients is $$p(E)= \left(1 - \frac{1}{100}\right)^{100} \approx \frac{1}{e} < \frac{1}{2}$$.
so, $$p(\bar{E})=1-p(E)$$ $$p(\bar{E}) \approx 1-\frac{1}{e}$$ $$p(\bar{E})> \frac{1}{2}.$$
The probability of the doctor contracting the virus after examining 100 patients is $(1- \frac{1}{100})^2$ which is greater than $\frac{1}{2}.$




- Also, $$\lim_{n \to \infty} (1-\frac{1}{n})^{nlogn} = \frac{1}{n}$$.

## Problem

![Alt text](https://raw.githubusercontent.com/Yat-98/Image/main/min.jpg "FIG (i)")
- A cut $S \subseteq E$ is an edge such that a graph $G'(E,E \setminus S)$ has more components than `G(V,E)`.
- Our aim is to find a minimum cut `S` that separates the graph `G` into `A` and `B` whose $B = V \setminus A$ that is, minimize the number of edges across the partition.
- The upper bound for the size of `S` is the minimum degree of the graph `G`. The size of `S` can never exceed the minimum degree of a graph.

* In fig. 1, the minimum degree of a graph is 3 while the size of `S` is 2.

## Algorithm

1. Pick an edge e=xy from the graph uniformly at random.
2. Fuse the two nodes of the edge e-xy into a single node.
3. Repeat the step 1 & 2 till the resulting graph shrinks to a graph of 2 nodes.
4. The edges between these two nodes now are a cut in the original graph \(g\). As a&b in a way represent multiple nodes that were contracted to these nodes. And thus, removing the edge set \(E'\) should disconnect the graph as the fused nodes were separated by \(E'\).

![Alt text](https://raw.githubusercontent.com/Yat-98/Image/main/fuse.jpg "FIG (ii)")

>**_Terminology:_** "Uniformly at random" refers to the unprejudicially & fairness in selection where each element has an equal probability of being selected.

Repeat the algorithm, randomly select an edge and fuse the two nodes into one till you are left with two nodes, multiple times. The minimum most cut is the 'min cut', with very high probability.

## Analysis:
- Let \(D\) be the minimum cut of a graph \(G\). If any edge in this cut is picked and fused, the resulting graph won't have \(D\). However, if the algorithm does not select any of these cuts, then \(D\) will be contained in the resulting graph.
                                                                                                                                                                  
- Let \(k\) be the minimum degree in the graph, and \(E\) be the event of touching an edge in \(D\). We know that,$|D|=s$ $\leq$ k $$total no. of edges \geq \frac{nk}{2}$$ 
$$P(E) = \frac{|D|}{Total no. of Edges} \leq \frac{k}{nk/2} \leq \frac{2}{n}$$
$$P(\bar{E}) \geq 1- \frac{2}{n}.$$
This is in the first attempt.Probability of $\bar{E}$ in the second attempt can be given by, $$P(E) \leq \frac{2}{n-1}$$ [as one edge has been picked up already] 
$$(\bar{E}) \leq 1- \frac{2}{n-1}.$$ Similarly, in $r^{th}$ attempt, 
$$P(\bar{E}) \leq 1-\frac{2}{n-r+1}$$
Probability of not picking an edge from D is given by: $$= (1-\frac{2}{n})(1-\frac{2}{n-1})........$$ $$= (\frac{n-2}{n})(\frac{n-3}{n-1})(\frac{n-4}{n-2})........(2)(1)$$ $$= \frac{2}{n(n-1)}$$ $$= \frac{1}{\binom{n}{2}}$$
The probability with which the algorithn returns the min-cut is at least $\frac{1}{\binom{n}{2}}.$ So, the probability of the algorithm failing is at most $1-\frac{1}{\binom{n}{2}}.$ Let T be the event of our algorithm failing. Repeating, the the algorithm multiple times, reduces our error probability. Say, we iterate through the algorithm $\binom{n}{2}$ times, \
 
$$P(T) \leq (1-\frac{1}{\binom{n}{2}})^{\binom{n}{2}}$$

$$P(T) \leq \frac{1}{e}$$

After $\binom{n}{2} log(\binom{n}{2})$ iterations,\

$$P(T) \leq (1-\frac{1}{\binom{n}{2}})^{\binom{n}{2} log(\binom{n}{2})}$$

$$P(T) \leq \frac{2}{\binom{n}{2}}$$

Thus, after a certain number of iterartions, we can declare our min-cut with a very high probability.
