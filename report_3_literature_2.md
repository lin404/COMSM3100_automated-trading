# Performance Comparison of Automated Trading Algorithms

We report on a series of simulation experiments in which we study the performance of adaptive automated trading strategies on a trading venue that offers a coupled pair of trading exchanges: one a dark pool and the other a lit pool. Our model is directly inspired by the London Stock Exchange’s Turquoise PlatoTM venue which offers dark-pool functionality alongside the complementary lit-pool trading venue called Turquoise LitTM. We refer to this generic structure as a coupled venue. In this paper we report on our experience from taking adaptive trading strategies that have previously been demonstrated in the literature to work well on traditional lit limit-order-book (LOB) markets, and modifying them to be able to take advantage of the trading opportunities offered by a CV. Specifically, we study the GDX and ZIP trading algorithms, adapted for trading on a coupled venue (CV): our CV is an appropriately modified version of the Bristol Stock Exchange (BSE) open-source simulator of a LOB-based financial market. Our primary findings are WHAT and WHAT and WHAT.

## Literature Review/Technical Background/Competitor Analysis - 2

Execept original work, what we know about AA and ZIP is largely based upon empirical studies that investigate their performance in continuous double auction (CDA) markets. A. J. Bagnall and I. E. Toft 


### [Evaluation of the “Adaptive-Aggressive” Trading-Agent Strategy Against Human Traders in CDA: AA Wins](https://www.researchgate.net/profile/Dave_Cliff/publication/267767159_Evaluation_of_the_Adaptive-Aggressive_Trading-Agent_Strategy_Against_Human_Traders_in_CDA_AA_Wins/links/54b791d40cf2bd04be33a4e5.pdf)

the performance of Adaptive Aggressive (AA), a new agent strategy, and ZIP, GD and GDX are investigated in both humans vs. agent and agent vs. agent contexts. Open Exchange (OpEx), an experimental algorithmic trading platform, is used to simulate an electronic trading system. Multiple instances can be developed in Agent Host using OpEx framework. Each Agent implements one specific algorithm and has its own configuration settings. GD algorithm seeks an order price which maximises the product of the “belief” functions built from the observed market data. Addition to that, GDX employs Dynamic Programming (DP) to price orders. The Adaptive Aggressiveness (AA) trading algorithm contains two individual components, a short-term and a long-term one. The short-term learning mechanism is used to react promptly to market fluctuations. The long-term learning process aid in making bidding decisions. In total, nine of human vs. agent experiments was implemented, three for each of ZIP, GDX and AA. Overall, the agents performed better than humans. In addition, AA performed the best which gained 27% profit greater than humans. AA, ZIP and GDX were compared to each other in pure robot vs. robot markets. In result, GDX beat ZIP, and AA defeated both GDX and ZIP. Moreover, the mean number of rounds per experiment won of AA is higher than GDX. 


Previous research have established that AA offers the best performance of any published bidding strategy.

A makes a similar point / builds on the work of B 

2. [Zero Intelligence Plus and Gjerstad-Dickhaut Agents for Sealed Bid Auctions](https://pdfs.semanticscholar.org/ddd6/67a415a71c1ac17270ed2cc8ddac06234d16.pdf)

In the same vein,

3. [TOO FAST – TOO FURIOUS: Faster Financial-Market Trading Agents Can Give Less Efficient Markets](https://www.researchgate.net/profile/John_Cartlidge/publication/273060607_Too_fast_too_furious_Faster_financial_market_trading_agents_can_give_less_efficient_markets/links/55882dfa08aeb29944448104.pdf)


X has been found to oppose the anti-inflammatory actions of Y on Z (Alourfi, 2004).

4. [Exhaustive Testing of Trader-agents in Realistically Dynamic Continuous Double Auction Markets: AA Does Not Dominate](local)

