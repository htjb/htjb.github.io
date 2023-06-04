---
title: My Work
---

Below is a summary of some of my most recent work.

- [Piecewise Normalizing Flows](#piecewise-normalizing-flows)
- [Joint Constraints on the first galaxies](#joint-constraints-on-the-first-galaxies)
- [margarine: Marginal Bayesian Statistics](#margarine-marginal-bayesian-statistics)
- [Astrophysical constraints on the first galaxies from SARAS3](#astrophysical-constraints-on-the-first-galaxies-from-saras3)

## Piecewise Normalizing Flows

- [Paper](https://arxiv.org/abs/2305.02930)
- TLDR: Using clustering algorithms to improve the accuracy of normalizing
flows when learning multi-modal distributions.

In this paper I demonstrated how we can exploit clustering algorithms
to improve the accuracy of normalizing flows when learning highly multi-modal
distributions.

Normalizing flows can be used to perform density estimation and are a bijective
and differentiable transformation between a known base distribution and
a target distribution. The transformation is often represented by
a neural network that can be optimised to learn the target. Once learnt
we can draw samples from the flow and calculate probabilities for a given
set of samples on the distribution.

The flows typically struggle to learn multi-modal distributions because the
topology of the base distribution is so different to the topology of the
target distribution. A number of methods exist to improve the accuracy of 
flows on multi-modal distributions but we often find that the
learned distributions feature bridges between the modes that are not present
in the target.

In our work we showed that we can break the target distribution up into
different clusters and train normalizing flows on each cluster. We discuss
how to sample from this piecewise distribution and how to calcualte probabilities
on it in the papaer.

The below figure shows how our piecewise normalizing flow approach
performs in comparison to a single noramlizing flow (MAF) and an alternative
approach detailed in [Stimper et al. 2022](https://proceedings.mlr.press/v151/stimper22a).

<center><img src="{{ site.url }}/assets/piecewise_normalising_flows.png" width="70%" alt-text="Benchmark Examples"></center>


## Joint Constraints on the first galaxies

- [Paper](https://arxiv.org/abs/2301.03298)
- TLDR: Using a novel machine learning Bayesian workflow to derive joint
constraints on the properties of the first galaxies with data from 21-cm
cosmology experiments.

Under construction.

## margarine: Marginal Bayesian Statistics

- [Paper One](https://arxiv.org/abs/2205.12841)
- [Paper Two](https://arxiv.org/abs/2207.11457)
- TLDR: Using normalizing flows to build of nuisance-free or marginal
Bayesian workflow.

Under construction.

## Astrophysical constraints on the first galaxies from SARAS3

- [Paper](https://www.nature.com/articles/s41550-022-01825-6)
- [Preprint](https://arxiv.org/abs/2212.00464)
- Publisher: Nature Astronomy
- TLDR: The first constraints from 21-cm cosmology on the properties of the first galaxies 200
million years after the Big Bang.

Under construction.