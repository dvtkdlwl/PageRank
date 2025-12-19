# PageRank Algorithm (Sampling & Iteration)

The PageRank Algorithm is an incredibly popular, yet rather simple algorithm that was used by Google in its early days. This repository presents a standalone reimplementation of the same, using both
sampling-based estimation and iterative convergence methods.

---

## Overview

The module computes PageRank values for a collection of linked pages using:

- **Sampling-based PageRank**
  - Estimates rank values by simulating random walks through the graph
- **Iterative PageRank**
  - Repeatedly applies the PageRank update rule until convergence

Both approaches return normalized PageRank scores that sum to 1.

---

## Key Concepts

- Markov chains
- Random sampling
- Graph traversal
- Iterative numerical convergence
- Probability distributions

---

## Module Contents

- `crawl(directory)`  
  Parses a directory of HTML files and extracts the link graph.

- `transition_model(corpus, page, damping_factor)`  
  Computes transition probabilities from a given page.

- `sample_pagerank(corpus, damping_factor, samples)`  
  Estimates PageRank values via random sampling.

- `iterate_pagerank(corpus, damping_factor)`  
  Computes PageRank values via iterative convergence.

---

## Note

This implementation is based on concepts from
**Harvard’s CS50 Introduction to Artificial Intelligence with Python**. 

The code has been refactored and reframed as a standalone algorithmic
implementation and is shared for **educational and portfolio
demonstration purposes**.

It is not intended for reuse as coursework solutions.
