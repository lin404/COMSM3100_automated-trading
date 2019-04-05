# Proposal

## Executive Summary

### Aim and Objectives

The aim of this project is to examine which automated trading algorithms AA and ZIP performs better in multi-venue environments.

Nowadays, there are many different types of electronic trading markets, in order to increase the gain, more and more adaptive automated trading strategies are applied. Among the numerous automated trading algorithms, AA and ZIP are two of the most popular algorithms. Investigating their performance in multi-venue environments supports to understand the strategies behind them, and deploy better algorithms.

The objectives of this project are to:

1. Week 1: research the modern electronic trading markets, understand and catalogue their difference, in order to create the proper simulation environments for implementing automated trading algorithms.
2. Week 2-4: develop a series of simulation experiments that enable studying the performance of adaptive automated trading strategies.
3. Week 4-5: research the automated trading algorithms AA and ZIP, understand how they perform the trading, so as to evaluate the proper result when implementing them in simulation environments.
4. Week 5-6: implement AA and ZIP in simulation environments, verify the results, demonstrate the simulation environments.
5. Week 6-8: investigate the performance of AA and ZIP in simulation multiple venues, compare and analyze the results. Ensure the experiments are quantitative and qualitative.
6. Week 8-11: identify the valid elements which affecting performance, research the associated works, ideally improve their performance.
7. Week 11-12: write up a thesis reflecting and evaluating the final product and work performed.

### Deliverables

- Based on London Stock Exchange’s Turquoise PlatoTM, study about the trading venues implemented in the real world, ensure simulation environments are close to the practical venues as much as possible.
- Use Bristol Stock Exchange (BSE) open-source to create a series of simulation trading venues. Explore how to apply BSE open-source, and once more understand the different trading venues.
- Implement algorithms AA and ZIP in simulation environments. Based on relevant works, verify the environment. Investigate and analyze the performance, classify the results. Identify effective factors and potential elements. Demonstrate which algorithm performs better in which environment with what conditions.
- a thesis showing my understanding and knowledge about the different trading venue and automated trading algorithms AA and ZIP, explaining the simulation experiments and evaluating the work results.

### Added Value

The simulation trading venues may be used to explore other automated trading algorithms. The analysis may be extended to improve algorithms AA and ZIP or any other algorithms. Moreover, a wide range of people may be interested in this project which including financial professional and computer scientists. The performance comparison may be applied to choose the right strategies for different trading environments. In economy and finance, for preventing the market impact from high frequency automated trading, a new electronic market may be implemented to decrease the performance of the present automated trading algorithms. The results analysis may negotiate computer scientists to deploy more powerful algorithms. If my project were to be applied in real venues then it would give a more precise analysis on how they perform in practice.

--------------------------------------- didn't polish from here --------------------------------------

## Introduction/Motivation

### The brief history of algo trading and electronic markets

Back in the 1980s, program trading was used on the New York Stock Exchange, with arbitrage traders pre-programming orders to automatically trade when the S&P500’s future and index prices were far apart. As markets moved to become fully electronic, human presence on a trading floor gradually became redundant, and the rise of high-frequency traders emerged. A special class of algo traders with speed and latency advantage of their trading software emerged to react faster to order flows.

### The impact of algorithmic trading on markets / interaction

Many changes in the equity markets and their trading processes have occurred. The most obvious change is that trading has become incredibly fast (High-Frequency Trading). A Lit or light pool market will allow traders to see the amount of liquidity that is posted on the bid and offer of the order book for security. However, HFT became so pervasive that it grew increasingly difficult to execute large trades through a single exchange. Because large HFT orders had to be spread among multiple exchanges, it alerted trading competitors who could then get in front of the order and snatch up the inventory, driving up share prices. All of this occurred within milliseconds of the initial order being placed. To avoid the transparency of public exchanges and ensure liquidity for large block trades, several of the investment banks established private exchanges, which came to be known as dark pools.

## Literature Review/Technical Background/Competitor Analysis

- Strategies for automated trading.
- Performance analysis of AA and ZIP.

## Proposed Approach/Methodology/Research Questions

- Simulation of multi-venue

  - London Stock Exchange’s Turquoise PlatoTM venue
  - Bristol Stock Exchange (BSE) open-source simulator
  - Simulation of lit-market, dark-market(with different liquidity)

- Exploration of AA and ZIP

  - perform cross-market trading.
  - compare the performance.
  - analyse the performance.
