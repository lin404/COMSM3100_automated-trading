# Performance Comparison of Automated Trading Algorithms

## Proposed Approach/Methodology/Research Questions

- Simulation of multi-venue

  - London Stock Exchange’s Turquoise PlatoTM venue
  - Bristol Stock Exchange (BSE) open-source simulator
  - Simulation of lit-market, dark-market(with different liquidity)

- Exploration of AA and ZIP

  - perform cross-market trading.
  - compare the performance.
  - analyse the performance.


For the purposes of this study, I will be focusing on one major exchange Turquoise (majority owned by London Stock Exchange).
The reason why I have concentrated on explaining agent research
with relation to financial markets in this paper is due to their large and increasing presence in
financial exchanges, with every major exchange (NYSE, NASDAQ, LSE) operating as a version
of a CDA.

TURQUOISE PLATO will be used as the trading venues.
Turquoise (majority owned by LSE) and Plato Partnership (not-for-profit consortium comprising buy and sell side) 
Turquoise Plato Block Discovery (TPBD) is a partnership between the LSE’s Turquoise and the Plato Partnership, a not-for-profit consortium of large buy- and sell-side firms. 
Trading mechanism, Conditional order service aimed at trading larger blocks. Interacts with Plato Uncross and matches conditional orders at randomised intervals. Includes size priority in the matching logic and user defined minimum execution size

Specify the degree of risk aversion (that is, how much to penalize variance relative to expected cost), which indicates the level of trading aggressiveness or passiveness.
Aggressive trading is associated with higher cost and less risk, whereas passive trading is associated with lower market impact and higher risk. An arithmetic random walk is often the most popular model for specifying the dynamics of future market prices. Given specifications of all the factors, an optimal trading strategy for a specific trading objective might be obtained by solving the corresponding stochastic dynamic optimization problem.