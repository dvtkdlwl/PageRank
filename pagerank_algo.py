"""
PageRank Algorithm Implementation

Implements PageRank using both sampling-based estimation
and iterative convergence methods.
"""

import os
import random
import re

DAMPING = 0.85
DEFAULT_SAMPLES = 10000
CONVERGENCE_THRESHOLD = 0.001


def crawl(directory):
    """
    Parses a directory of HTML pages and extracts links between them.

    Returns a dictionary where each key is a page name, and values are
    the set of other pages in the corpus that the page links to.
    """
    pages = {}

    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue

        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r'<a\s+(?:[^>]*?)href="([^"]*)"', contents)
            pages[filename] = set(links) - {filename}

    for page in pages:
        pages[page] = {link for link in pages[page] if link in pages}

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Returns a probability distribution over pages representing
    the likelihood of transitioning to each page from the current page.

    With probability `damping_factor`, transitions occur via links
    from the current page. With probability `1 - damping_factor`,
    transitions occur uniformly across all pages.
    """
    distribution = {}
    pages = list(corpus.keys())
    links = corpus[page]

    for p in pages:
        distribution[p] = (1 - damping_factor) / len(pages)

    if links:
        for link in links:
            distribution[link] += damping_factor / len(links)
    else:
        for p in pages:
            distribution[p] += damping_factor / len(pages)

    return distribution


def sample_pagerank(corpus, damping_factor=DAMPING, samples=DEFAULT_SAMPLES):
    """
    Returns PageRank values for each page by sampling transitions
    according to the transition model.

    Sampling begins from a randomly selected page. The returned
    dictionary maps page names to estimated PageRank values,
    which sum to 1.
    """
    pages = list(corpus.keys())
    ranks = {page: 0 for page in pages}

    current_page = random.choice(pages)

    for _ in range(samples):
        ranks[current_page] += 1
        probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(
            population=list(probabilities.keys()),
            weights=list(probabilities.values())
        )[0]

    for page in ranks:
        ranks[page] /= samples

    return ranks


def iterate_pagerank(corpus, damping_factor=DAMPING):
    """
    Returns PageRank values for each page by iteratively applying
    the PageRank update rule until convergence.

    PageRank values are updated until no value changes by more
    than the convergence threshold. Returned values sum to 1.
    """
    num_pages = len(corpus)
    ranks = {page: 1 / num_pages for page in corpus}

    while True:
        new_ranks = {}

        for page in corpus:
            rank = (1 - damping_factor) / num_pages

            for possible_page in corpus:
                if corpus[possible_page]:
                    if page in corpus[possible_page]:
                        rank += damping_factor * (
                            ranks[possible_page] / len(corpus[possible_page])
                        )
                else:
                    rank += damping_factor * (ranks[possible_page] / num_pages)

            new_ranks[page] = rank

        if all(
            abs(new_ranks[page] - ranks[page]) < CONVERGENCE_THRESHOLD
            for page in ranks
        ):
            break

        ranks = new_ranks

    return ranks
