# Performance Comparison of Automated Trading Algorithms

- Objective of the literature review
- Overview of the subject under consideration.
- Clear categorization of sources selected into those in support of your topic
- particular position, those opposed, and those offering completely different arguments.
- Discussion of both the distinctiveness of each source and its similarities with the others.


We report on a series of simulation experiments in which we study the performance of adaptive automated trading strategies on a trading venue that offers a coupled pair of trading exchanges: one a dark pool and the other a lit pool. Our model is directly inspired by the London Stock Exchange’s Turquoise PlatoTM venue which offers dark-pool functionality alongside the complementary lit-pool trading venue called Turquoise LitTM. We refer to this generic structure as a coupled venue. In this paper we report on our experience from taking adaptive trading strategies that have previously been demonstrated in the literature to work well on traditional lit limit-order-book (LOB) markets, and modifying them to be able to take advantage of the trading opportunities offered by a CV. Specifically, we study the GDX and ZIP trading algorithms, adapted for trading on a coupled venue (CV): our CV is an appropriately modified version of the Bristol Stock Exchange (BSE) open-source simulator of a LOB-based financial market. Our primary findings are WHAT and WHAT and WHAT.

## Literature Review/Technical Background/Competitor Analysis - 1

A considerable amount of literature has been published on algorithmic trading. To better understand algorithmic trading, the [study](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/5696713) of Nuti, Mirghaemi, Treleaven and Yingsaeree give a review of algorithmic trading. Due to their study, the type of trading can be categorised into the broker and proprietary. Both AA and ZIP trading algorithms can be considered as broker algorithmic trading systems, the strategy behind is to minimize the cost of trading by minimizing market impact cost or execution time, optimizing the price, and so on. Nuti et al. describe trading process of algorithmic trading can be slite into four steps: pre-trade analysis, trading signal generation, trade execution, and post-trade analysis. Algorithmic trading can be used at any stage of the trading process for various purposes, such as market making, spread trading, arbitrage, and macrotrading. Both AA and ZIP trading algorithms are used in trade execution for spread trading. In view of Nuti et al.'s summary, there are many variants to the order book model including limit orders, market orders, stop-loss orders, and so on. The two main types of trades are market orders and limit orders. Both AA and ZIP trading algorithms use limit orders. A limit order guarantees the execution price, but it may be executed only partially or not at all. Nuti et al. state different exchanges will accept different order types. Choose proper trading venues, liquidity, trading mechanism, degree of trader anonymity, and differential execution costs are considered as some of the most important characteristics. In general, a highly liquid market is prefered, owing to the fast trade execution and low transaction costs. Consequently, to better develop/implement an algorithmic trading system, understanding of the market microstructure, and how the market sorts out orders and executes trades is of paramount importance.

To date, a large and growing body of literature has investigated various strategies of algorithmic trading. In this paper, I will be focusing on Adaptive-Aggressive (AA) strategy and Zero-Intelligence-Plus (ZIP) strategy.
ZIP was introduced by D. Cliff and J. Bruten in 1997. A short [article](https://eprints.soton.ac.uk/264236/1/ZIP_1500wV2_ep.pdf) written by D. Cliff gives the simple interpretation of ZIP. Assume, for buyers, each trader has a maximum pay price l, but quotes a less price p in the market; for sellers, each trader has a minimum sell price l, but quotes a greater price p in the market. ZIP uses m to represent the difference between l and p which is determined by trader’s margin. By using a decistion tree machine learning model on observed market data, ZIP agents will raise or lower its margin to seek the best profit.
In contrast, AA is a fairly recent strategy, published by P. Vytelingum in 2006. The Adaptive Aggressiveness (AA) trading algorithm contains two individual components, a short-term and a long-term one. The short-term learning mechanism is used to react promptly to market fluctuations.







