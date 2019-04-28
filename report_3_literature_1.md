# Performance Comparison of Automated Trading Algorithms

- Objective of the literature review
- Overview of the subject under consideration.
- Clear categorization of sources selected into those in support of your topic
- particular position, those opposed, and those offering completely different arguments.
- Discussion of both the distinctiveness of each source and its similarities with the others.

## Literature Review/Technical Background/Competitor Analysis - 1

During the past decade, as a result of the computerisation of orders, the world has gradually been moving towards electronic trading. A considerable amount of literature has been published on algorithmic trading. To better understand algorithmic trading, the [study](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/5696713) of Nuti, Mirghaemi, Treleaven and Yingsaeree give a review of algorithmic trading. The type of trading can be categorised into the broker and proprietary. Both AA and ZIP trading algorithms can be considered as broker algorithmic trading systems, the strategy behind is to minimize the cost of trading by minimizing market impact cost or execution time, optimizing the price, and so on. The trading process of algorithmic trading can be slite into four steps: pre-trade analysis, trading signal generation, trade execution, and post-trade analysis. Algorithmic trading can be used at any stage of the trading process for various purposes, such as market making, spread trading, arbitrage, and macrotrading. Both AA and ZIP trading algorithms are used in trade execution for spread trading. There are many variants to the order book model including limit orders, market orders, stop-loss orders, and so on. The two main types of trades are market orders and limit orders. Both AA and ZIP trading algorithms are used for limit orders. A limit order guarantees the execution price, but it may be executed only partially or not at all. Different exchanges will accept different order types. Choose proper trading venues, liquidity, trading mechanism, degree of trader anonymity, and differential execution costs are considered as some of the most important characteristics. In general, a highly liquid market is prefered, owing to the fast trade execution and low transaction costs. Consequently, in developing an algorithmic trading system, understanding of the market microstructure, and how trades occur and orders interact in a specific market is of paramount importance.

TURQUOISE PLATO will be used as the trading venues.
Turquoise (majority owned by LSE) and Plato Partnership (not-for-profit consortium comprising buy and sell side) provies trading services 
Turquoise Plato Block Discovery (TPBD) is a partnership between the LSE’s Turquoise and the Plato Partnership, a not-for-profit consortium of large buy- and sell-side firms. 
Trading mechanism, Conditional order service aimed at trading larger blocks. Interacts with Plato Uncross and matches conditional orders at randomised intervals. Includes size priority in the matching logic and user defined minimum execution size


Specify the degree of risk aversion (that is, how much to penalize variance relative to expected cost), which indicates the level of trading aggressiveness or passiveness.
Aggressive trading is associated with higher cost and less risk, whereas passive trading is associated with lower market impact and higher risk. An arithmetic random walk is often the most popular model for specifying the dynamics of future market prices. Given specifications of all the factors, an optimal trading strategy for a specific trading objective might be obtained by solving the corresponding stochastic dynamic optimization problem.


