# Performance Comparison of Automated Trading Algorithms

## Proposed Approach/Methodology/Research Questions

### Participants

I will apply AA and ZIP as strategies to design automated trading agents. Because there is a large volume of the lecture has investigated the performance of AA and ZIP. There are loads of information can be referred to in this study. They contribute to the well understanding of AA and ZIP in different environments. Instead of investigating their general performance, this study will force on investigating their performance in a particular situation. In most of the research, both ZIP and AA were presented has a good performance compared to other published strategies. Plus, AA was claimed as the best strategy once, then the conclusion about AA was changed when changing the experiment environment. It will be interesting to recover its performance in multiple venues, a new approach differs from the previous researches.

### Simulation Materials

I will use Bristol Stock Exchange (BSE) open-source simulator to set up the experiment environments. It's a relatively new simulator in this field. The BSE GitHub repository provides source-code for the trading algorithms of ZIP and AA. Moreover, a built-in strategy SHVR in BSE will be used as a competitor robot trader against to AA and ZIP agents. Documented by Cliff, thanks to its distinguished features, varying supply and demand schedules can be set to simulate a closer real-world market. As the additional value, this study can contribute to the better understanding and usage of BSE.
  
### Simulation Design

The market mechanics used in the London Stock Exchange’s Turquoise Plato™ venue will be applied in the experiment environment. Due to the description in the regular document, there are two discrete order books for complementary liquidity in Turquoise: Turquoise Lit™ and Turquoise Plato™. Turquoise Lit™ combines simple limit and iceberg orders with Large-In-Scale hidden orders, whereas Turquoise Plato™ is a Price-referencing Order Book. In addition, Turquoise Plato™ contains two mechanisms provided by Turquoise Plato Uncross™ and Turquoise Plato Block Discovery™. Turquoise Plato Uncross™ allows only larger and less time-sensitive passive orders. Turquoise Plato Block Discovery™ requires block orders have to be sent to Turquoise Plato Uncross™ in order to maximise available liquidity.

Both light pool and dark pool market in this study will be designed based on detailed Turquoise. To accurately construct the markets, it is important to define the market mechanics and traders' behaviors.

- Light pool market mechanism: This type of market aims to match the orders immeditaly. It combines limit orders and iceberg orders with Large In Scale hidden orders. Orders will be executed on a price, display type, time priority basis. The priority among the orders is: limit orders will have the highest priority, iceberg orders come to second, LIS Hidden orders have the lowest priority.
- Light pool market participants: Traders in this market will be informed with opportunity to benefit from rebates. Aggressive orders are allowed to trade in the market, aiming to increase the market liquidity.

- Dark pool market mechanism: This type of market matches the mid-point of the bid and ask price from the exchange. It executes trades randomly at a set number of times during a specific time period as a crossing network. This market has size priority and user-defined minimum execution size. Under size priority, larger orders will have less time-sensitive, participants can rest larger orders for longer to achieve better execution quality in this type of market. Under user-defined minimum execution size,  participants can initiate a trade with an aggressive order. In addition, without preference to time-sensitive, participants can initiate and choose the execution time.
- Dark pool market participants: Uninformed traders can trade in this market and each trader is expected to trade at each given time period, aiming to avoid price impact. Only passive orders from buyers and sellers are allowed in this market.

### Experiment Procedure

The aim of these experiments is to determine which stratagy is more effective in particular environments. AA, ZIP and SHVR traders will run in the three different environments: only light pool market, only dark pool market, the market combined light pool with block oders. The performance will be evaluated and measured as average profitability per trader, when it against other trading strategies. The combination will be AA vs. ZIP, AA vs. SHVR, ZIP vs. SHVR. The experiments will be implemented under a variety of supply and demand schedules. Additionally, The simulation markets will have varying population sizes. For any one population size, the experiments will be implemented across an exhaustive sequence of strategy-ratios.