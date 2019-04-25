# Performance Comparison of Automated Trading Algorithms

## Literature Review/Technical Background/Competitor Analysis - 1

### [Evaluation of the “Adaptive-Aggressive” Trading-Agent Strategy Against Human Traders in CDA: AA Wins](https://www.researchgate.net/profile/Dave_Cliff/publication/267767159_Evaluation_of_the_Adaptive-Aggressive_Trading-Agent_Strategy_Against_Human_Traders_in_CDA_AA_Wins/links/54b791d40cf2bd04be33a4e5.pdf)

In 2001, IBM announced that ZIP and GD outperform the human traders in the continuous double auction (CDA) market. In a later paper, IBM reported GDX outperforms GD and ZIP in agent vs. agent CDA competitions. Hence, the performance of Adaptive Aggressive (AA), a new agent strategy, and ZIP, GD and GDX are investigated in both humans vs. agent and agent vs. agent contexts.
Open Exchange (OpEx), an experimental algorithmic trading platform, is used to simulate an electronic trading system. Multiple instances can be developed in Agent Host using OpEx framework. Each Agent implements one specific algorithm and has its own configuration settings. The strategy behinds Zero-Intelligence Plus (ZIP) algorithm is to use profit margin and adjust the margin according to market data observed. GD algorithm seeks an order price which maximises the product of the “belief” functions built from the observed market data. Addition to that, GDX employs Dynamic Programming (DP) to price orders. The Adaptive Aggressiveness (AA) trading algorithm contains two individual components, a short-term and a long-term one. The short-term learning mechanism is used to react promptly to market fluctuations. The long-term learning process aid in making bidding decisions. In total, nine of human vs. agent experiments was implemented, three for each of ZIP, GDX and AA. Overall, the agents performed better than humans. In addition, AA performed the best which gained 27% profit greater than humans. AA, ZIP and GDX were compared to each other in pure robot vs. robot markets. In result, GDX beat ZIP, and AA defeated both GDX and ZIP. Moreover, the mean number of rounds per experiment won of AA is higher than GDX.
As a conclusion, AA offers the best performance of any published bidding strategy.

### [An Open-Source Limit-Order-Book Exchange for Teaching and Research](https://ieeexplore.ieee.org/abstract/document/8628760)

Algorithmic trading systems have been widely used in all major markets around the world. The people who can write algorithmic trading systems and use them quickly and reliably, not only high knowledge of arithmetic also rich experience are required. Moreover, will skilled students in University, offer students a environment where they can launch their own algo is in demand. Bristol Stock Exchange (BSE) was developed for students who can gain more experience through the practices.




### [BSE: A Minimal Simulation of a Limit-Order-Book Stock Exchange](https://arxiv.org/abs/1809.06027)

### [A study of dark pool trading using an agent-based model](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6611692/references#references)