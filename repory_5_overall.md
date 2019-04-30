# Performance Comparison of Automated Trading Algorithms

## Abstract

IN PROCESSING

## Executive Summary

### Aim and Objectives

The aim of this project is to examine which automated trading algorithms Adaptive Aggressive (AA) and Zero-Intelligence Plus (ZIP) performs better in multi-venue environments.

Nowadays, there are many different types of electronic trading markets, in order to increase gains, more and more adaptive automated trading strategies are being applied. From among the numerous automated trading algorithms, I will take two leading adaptive trading strategies which were also used in a new study of agent-human dominance in markets - Cliff’s Zero-Intelligence-Plus (ZIP) strategy and Vytelingum’s Aggressive-Adaptive (AA) strategy. The Investigations into their performance in multi-venue environments has increased understanding of the strategies behind them, and resulted in the deployment of better preforming algorithms.

The objectives of this project are:

1. To research the modern electronic trading markets, understand and catalogue their differences, in order to create the proper simulation venues for implementing automated trading algorithms.
2. To develop a series of simulation experiments that will enable study into the performance of adaptive automated trading strategies.
3. To research the automated trading algorithms AA and ZIP in order to understand how they perform the trading, so as to properly evaluate the result when implementing them in simulation environments.
4. To implement AA and ZIP in simulation environments, verify the results and demonstrate the simulation environments are realistic.
5. To investigate the performance of AA and ZIP in multiple simulated environments, and then to compare and analyze the results, while ensuring the experiments have both quantitative and qualitative aspects.
6. To identify the valid elements which affect performance, research the associated works and, ideally, improve how they perform.
7. To write up a thesis reflecting and evaluating the final product and work performed.

### Deliverables

- Based on London Stock Exchange’s Turquoise PlatoTM,  to study the trading venues implemented in the real world, ensure simulation environments are close to the practical venues as much as possible.
- To use Bristol Stock Exchange (BSE) open-source to create a series of simulation trading venues. Explore how to apply BSE open-source, and once more understand the different trading venues.
- To implement algorithms AA and ZIP in these simulation environments, and verify these environments are a good model of real trading venues. Investigate and analyze the algorithms performance, classify the results and then identify the important factors and potential risks, with the aim being to demonstrate which algorithm performs better in which environment with what conditions.
- A thesis showing my understanding and knowledge about the different trading venue and automated trading algorithms AA and ZIP, explaining the simulation experiments and evaluating the results.

### Added Value

The simulation trading venues may be used to explore other automated trading algorithms. The analysis may be extended to improve algorithms AA and ZIP or any other algorithms. Moreover, a wide range of people may be interested in this project which including financial professionals and computer scientists. The performance comparison may be applied to choose the right strategies for different trading environments. In economics and finance, for preventing the market being impacted by high frequency automated trading, a new electronic market may be implemented to decrease the performance of the present automated trading algorithms. The result of this analysis may be computer scientists deploying even more powerful algorithms. If my project were to be applied in real venues then it would give a more precise analysis on how they perform in practice.

## Introduction

### The brief history of algo trading and electronic markets

IN PROCESSING

### The impact of algorithmic trading on markets / interaction

IN PROCESSING

## Literature Review/Technical Background/Competitor Analysis

A considerable amount of literature has been published on algorithmic trading. To better understand algorithmic trading, the [study](1) of Nuti, Mirghaemi, Treleaven and Yingsaeree give a review of algorithmic trading. Due to their study, the type of trading can be categorised into the broker and proprietary. Both AA and ZIP trading algorithms can be considered as broker algorithmic trading systems, the strategy behind is to minimize the cost of trading by minimizing market impact cost or execution time, optimizing the price, and so on. Nuti et al. describe the trading process of algorithmic trading can be split into four steps: pre-trade analysis, trading signal generation, trade execution, and post-trade analysis. Algorithmic trading can be used at any stage of the trading process for various purposes, such as market making, spread trading, arbitrage, and macrotrading. Both AA and ZIP trading algorithms are used in trade execution for spread trading. In view of Nuti et al.'s summary, there are many variants to the order book model, market orders and limit orders are two main types of trades. Both AA and ZIP trading algorithms use limit orders. A limit order guarantees the execution price, but it may be executed only partially or not at all. Nuti et al. state different exchanges will accept different order types. When choosing proper trading venues, liquidity, trading mechanism, degree of trader anonymity, and differential execution costs are considered as some of the most important factors. In general, a highly liquid market is preferred, owing to the fast trade execution and low transaction costs. Consequently, to better develop/implement an algorithmic trading system, understanding of the market microstructure, and how the market sorts out orders and executes trades is of paramount importance.

To date, a large and growing body of literature has investigated various strategies of algorithmic trading. In this paper, I will be focusing on Adaptive-Aggressive (AA) strategy and Zero-Intelligence-Plus (ZIP) strategy. In particular, both trading strategies are designed to focus on one specific type of market, the Continuous Double Auction (CDA).

ZIP was introduced by D. Cliff and J. Bruten in 1997. A short [article](2) was published by D. Cliff, it gives the simple interpretation of ZIP. Assume, for buyers, each trader has a maximum pay price l, but quotes a less price p in the market; for sellers, each trader has a minimum sell price l, but quotes a greater price p in the market. ZIP uses m to represent the difference between l and p which is determined by the trader’s margin. By applying a decision tree machine learning model based on observable market data, ZIP agents will raise or lower its margin to maximise the profit. Commenting on entry strategy of ZIP, D. Cliff argues `At the core of the ZIP family of algorithms is a minimally-simplistic set of qualitative heuristics (that is, some rough rules-of-thumb) for adjusting trader i’s margin m at time t – denoted by mi(t). These heuristics depend on four things: (1) i’s current quote-price pi(t); (2) whether i is still active in the market (i.e., still attempting to trade, or just watching); (3) whether the last price quoted in the marketplace q(t-1) was an offer or a bid; and (4) whether q(t-1) was accepted by a counterparty or not.`

In contrast, AA is a fairly recent strategy, published by P. Vytelingum as part of his PhD research in 2006. In Chapter 5 of the PhD [thesis](3), Vytelingum described the concept of strategy applied in AA. In a nutshell, one of the distinguishing features of AA trading algorithm is that it contains two individual adaptive components: a short-term and a long-term learning of the agent’s bidding behaviour. The short-term learning mechanism attempts to promptly respond to market fluctuations. When a bid or ask appears in the market, the agent will update aggressiveness of its bidding based on market data observed. Here, if the agent couldn't transact, it will raise the aggressiveness to increase its chances of transaction; if it did transact, it will reduce the aggressiveness to become more passive in order to increase its profits. The level of trading aggressiveness or passiveness indicates the degree of risk aversion. Higher aggressiveness is associated with higher cost and less risk. Conversely, lower aggressiveness is associated with lower market impact but higher risk. On the other hand, in case of any systematic changes or market shocks, the long-term learning process aid in making bidding decisions. Vytelingum's strategy is to update an aggressiveness model after every successful transaction based on market information observed.

Except for original work, what we know about ZIP is largely based upon empirical studies that investigate its performance in a particular market. In the [report](4) published by R. Das, J. E. Hanson, J. O. Kephart, and G. Tesauro in 2001, it illustrated that ZIP agents outperformed human traders in all experiments. Due to the description in the report: The members of the IBM Watson Experimental Economics Laboratory (WEEL) developed GEM which is a special-purpose distributed system for experimental economics. Magenta is a prototype agent environment developed at IBM Resea. Das et al. developed a hybrid system combined GEM with Magenta for the experiments with humans and agents. In the experiments, two different time periods are used for the different algorithms: “fast” agents were defined as 1 second, and “slow” agents were defined as 5 seconds. The results presented in the experiments employed Gjerstad-Dickhaut (GD) fast agents and ZIP slow agents. The interviews with human subjects draw our attention to a weakness in the ZIP strategy. That is if using a specific non-optimal human strategy such as ‘fixed-profit-ratio’, the ZIP agents performed badly. However, Das et al. implemented a modification to the ZIP strategy. As Das et al. observe: `Preliminary results show that the modified ZIP agents retain high efficiency and are not easily misled by the fixed-profit-ratio agent.`. In conclusion, the agents utilized established algorithms, ZIP and GD, outperform non-expert human subjects. As the further work, Das et al. suggest testing their bidding agents against professional equities or commodities traders would assist to uncover more weaknesses in the strategies, thereby leading to significant improvements in the strategies.

To date, several studies have investigated the role of AA trader-agent strategy in the markets. A conference [paper](5) was published by J. Cartlidge, C. Szostek, M. De Luca and D. Cliff in 2012. They explored the performance of AA-ultra and AA-slow to investigate markets efficiency. AA-ultra is a fast trader-agents which interval time is 0.1s, and AA-slow is slow trader-agents which interval time is 10s and agents perform further internal calculations every 2.5s. For a market simulation environment, they applied a new series of artificial trading experiments using the OpEx experimental economics system first introduced at ICAART2011. Every time the market was reset before starting the experiment. Each experiment lasted 20 minutes. 3 buyers and 3 sellers each, a total of 6 human participants and 6 trader-agents traded in the market. AA-slow and AA-ultra were homogeneously configured as the trader-agents respectively. As the results presented through their experiments, Smith’s alpha values are lower for AA-slow experiments compared to AA-ultra in every replenishment cycle, indicating that slow trader-agents improve market convergence. In comparison with agents, humans perform better when trading against the slower trader-agents. Moreover, the profit dispersion of agents is similar under condition AA-slow and AA-ultra, yet the profit dispersion of humans and the market is apparently lower under condition AA-slow. Evidence from the study propose that slow trader-agents contribute a competitive equilibrium in the markets overall, and slow-agent markets have higher efficiency.

In a similar vein, M. De Luca and D. Cliff in 2015 [investigated](6) the performance of AA, ZIP, Gjerstad-Dickhaut (GD) and GDX in both humans vs. agent and agent vs. agent contexts. They used Open Exchange (OpEx), an experimental algorithmic trading platform, to simulate an electronic trading system. A primary characteristic of using OpEx framework is that multiple instances can be developed in Agent Host. In another word, multiple agents can be implemented at the same time, and each agent applies one specific algorithm and has its own configuration settings. Not only AA and ZIP but also GD and GDX strategies are explored in their study. The GD agent forms belief functions by using observed market data. GDX is a modified GD strategy, it employs Dynamic Programming (DP) to price orders. M. De Luca et al. made a similar build on the work of previous research. They implemented nine of human vs. agent experiments, three for each of ZIP, GDX and AA. Differ from previous work reported, they used 1s as the timing rule for the experiments, aim to simplify the comparison of the performances of the different trading agents. Overall, the agents performed better than humans. In addition, AA performed the best which gained 27% profit greater than humans. In pure agent vs. agent markets, AA, ZIP and GDX competitively traded against each other. In result, GDX beat ZIP, and AA defeated both GDX and ZIP. Moreover, the mean number of rounds per experiment won of AA is higher than GDX.

IN PROCESSING

Several previous research have established that AA offers the best performance of any published bidding strategy. However, [according](7) to Dave Cliff (2019), AA agents perform poorly in real-world markets. To date, most researchers investigating AA and ZIP have utilised Open Exchange (OpEx) or ExPo, whereas Bristol Stock Exchange (BSE) was applied for the experiments.

Much of the current literature on algorithmic trading systems begun to pay particular attention to appropriate simulated environment. Once again, former example of research (D.Cliff ICAART2019) confirms that a experiment environment closer to real-world financial markets is significant important, since the study of automated trading algorithms is mainly based on observational studies. Thence, BSE will be employed to simulate a LOB-based financial market for this study.

BSE is an open source developed and extended by Dave Cliff since 2012. In 2018, [BSE](8) is released as public-domain platform for teaching and research. Algorithmic trading systems have been widely used in all major markets around the world. The people who can write algorithmic trading systems and use them quickly and reliably, not only high knowledge of arithmetic also rich experience are required. Moreover, will skilled students in University, offer students a environment where they can launch their own algo is in demand. Bristol Stock Exchange (BSE) was developed for students who can gain more experience through the practices.

Up to now, the majority of popular research has focused on regular-sized bids and offers. However, there are relatively few studies in the area of block trading. A [study](9) of dark pool trading was pubilished by S. Y. K. Mo, M. Paddrik and S. Y. Yang in 2013.

In addition, there is a relatively small body of literature that is concerned with if/how known adaptive automated trading strategies select optimal trade in multi-venue environments. ?

## Proposed Approach/Methodology/Research Questions

IN PROCESSING

- Simulation of multi-venue

  - London Stock Exchange’s Turquoise PlatoTM venue
  - Bristol Stock Exchange (BSE) open-source simulator
  - Simulation of lit-market, dark-market(with different liquidity)

- Exploration of AA and ZIP

  - perform cross-market trading.
  - compare the performance.
  - analyse the performance.

## Reference

1. [Algorithmic Trading](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/5696713/authors#authors)
2. [My Family and Other Algorithms](https://eprints.soton.ac.uk/264236/1/ZIP_1500wV2_ep.pdf)
3. [P. Vytelingum. The Structure and Behaviour of the Continuous Double Auction. PhD thesis, University of Southampton, 2006.](https://eprints.soton.ac.uk/263234/1/THESIS.pdf)
4. [R. Das, J. E. Hanson, J. O. Kephart, and G. Tesauro. Agent-human interactions in the continuous double auction. The Proceedings of the International Joint Conferences on Artificial Intelligence (IJCAI), Seattle, USA (August, 2001), 2001.](https://s3.amazonaws.com/academia.edu.documents/44417575/das.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1556512970&Signature=JT7dTpWP0YqQRQx1avBwaZBS3uk%3D&response-content-disposition=inline%3B%20filename%3DAgent-Human_Interactions_in_the_Continuo.pdf)
5. [TOO FAST – TOO FURIOUS: Faster Financial-Market Trading Agents Can Give Less Efficient Markets](https://www.researchgate.net/profile/John_Cartlidge/publication/273060607_Too_fast_too_furious_Faster_financial_market_trading_agents_can_give_less_efficient_markets/links/55882dfa08aeb29944448104.pdf)
6. [Evaluation of the “Adaptive-Aggressive” Trading-Agent Strategy Against Human Traders in CDA: AA Wins](https://www.researchgate.net/profile/Dave_Cliff/publication/267767159_Evaluation_of_the_Adaptive-Aggressive_Trading-Agent_Strategy_Against_Human_Traders_in_CDA_AA_Wins/links/54b791d40cf2bd04be33a4e5.pdf)
7. [Exhaustive Testing of Trader-agents in Realistically Dynamic Continuous Double Auction Markets: AA Does Not Dominate](local)
8. [An Open-Source Limit-Order-Book Exchange for Teaching and Research](https://ieeexplore.ieee.org/abstract/document/8628760)
9. [A study of dark pool trading using an agent-based model](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6611692/references#references)
10. [Limit order placement across multiple exchanges](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6327772) ??
