# Performance Comparison of Automated Trading Algorithms

## Executive Summary

We report on a series of simulation experiments in which we study the performance of adaptive automated trading strategies on a trading venue that offers a coupled pair of trading exchanges: one a dark pool and the other a lit pool. Our model is directly inspired by the London Stock Exchange’s Turquoise PlatoTM venue which offers dark-pool functionality alongside the complementary lit-pool trading venue called Turquoise LitTM. We refer to this generic structure as a coupled venue. In this paper we report on our experience from taking adaptive trading strategies that have previously been demonstrated in the literature to work well on traditional lit limit-order-book (LOB) markets, and modifying them to be able to take advantage of the trading opportunities offered by a CV. Specifically, we study the GDX and ZIP trading algorithms, adapted for trading on a coupled venue (CV): our CV is an appropriately modified version of the Bristol Stock Exchange (BSE) open-source simulator of a LOB-based financial market. Our primary findings are WHAT and WHAT and WHAT.

### Aim and Objectives

The aim of this project is to examine which automated trading algorithms Adaptive Aggressive (AA) and Zero-Intelligence Plus (ZIP) performs better in multi-venue environments.

Nowadays, there are many different types of electronic trading markets, in order to increase the gain, more and more adaptive automated trading strategies are applied. Among the numerous automated trading algorithms,  I will take two leading adaptive trading strategies which were also used in this new study of agent-human dominance in markets - Cliff’s Zero-Intelligence-Plus (ZIP) strategy and Vytelingum’s Aggressive-Adaptive (AA) strategy. Investigating their performance in multi-venue environments supports to understand the strategies behind them, and deploy better algorithms.

The objectives of this project are to:

1. research the modern electronic trading markets, understand and catalogue their difference, in order to create the proper simulation environments for implementing automated trading algorithms.
2. develop a series of simulation experiments that enable studying the performance of adaptive automated trading strategies.
3. research the automated trading algorithms AA and ZIP, understand how they perform the trading, so as to evaluate the proper result when implementing them in simulation environments.
4. implement AA and ZIP in simulation environments, verify the results, demonstrate the simulation environments.
5. investigate the performance of AA and ZIP in simulation multiple venues, compare and analyze the results. Ensure the experiments are quantitative and qualitative.
6. identify the valid elements which affecting performance, research the associated works, ideally improve their performance.
7. write up a thesis reflecting and evaluating the final product and work performed.

### Deliverables

- Based on London Stock Exchange’s Turquoise PlatoTM, study about the trading venues implemented in the real world, ensure simulation environments are close to the practical venues as much as possible.
- Use Bristol Stock Exchange (BSE) open-source to create a series of simulation trading venues. Explore how to apply BSE open-source, and once more understand the different trading venues.
- Implement algorithms AA and ZIP in simulation environments. Based on relevant works, verify the environment. Investigate and analyze the performance, classify the results. Identify effective factors and potential elements. Demonstrate which algorithm performs better in which environment with what conditions.
- a thesis showing my understanding and knowledge about the different trading venue and automated trading algorithms AA and ZIP, explaining the simulation experiments and evaluating the work results.

### Added Value

The simulation trading venues may be used to explore other automated trading algorithms. The analysis may be extended to improve algorithms AA and ZIP or any other algorithms. Moreover, a wide range of people may be interested in this project which including financial professional and computer scientists. The performance comparison may be applied to choose the right strategies for different trading environments. In economy and finance, for preventing the market impact from high frequency automated trading, a new electronic market may be implemented to decrease the performance of the present automated trading algorithms. The results analysis may negotiate computer scientists to deploy more powerful algorithms. If my project were to be applied in real venues then it would give a more precise analysis on how they perform in practice.