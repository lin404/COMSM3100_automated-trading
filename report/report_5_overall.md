# Performance Comparison of Automated Trading Algorithms

## Abstract

In electronic financial markets, automatic algorithmic trading systems have largely replaced human traders. Along with the growth of automatic algorithmic trading systems, many of the world's major financial markets are experiencing changes as well, with the rise of dark pools markets being one of the most profound. These changes have created significant demand for automatic algorithmic trading systems that operate in multiple markets. This research aims to investigate if the existing, well-known automatic trading strategies, AA and ZIP, can operate successfully in multi-venue environments containing both light pools and dark pools.

## Executive Summary

### Aim and Objectives

The aim of this project is to examine which of the automated trading algorithms, Adaptive Aggressive (AA) or Zero-Intelligence Plus (ZIP) performs better in multi-venue environments.

Nowadays, there are many different types of electronic trading markets, in order to increase gains, more and more adaptive automated trading strategies are being applied. From among the numerous automated trading algorithms, I will take two leading adaptive trading strategies which were also used in a new study of agent-human dominance in markets - Cliff’s Zero-Intelligence-Plus (ZIP) strategy and Vytelingum’s Aggressive-Adaptive (AA) strategy. The Investigations into their performance in multi-venue environments has increased understanding of the strategies behind them, and resulted in the deployment of better preforming algorithms.

The objectives of this project are:

1. To research the modern electronic trading markets, understand and catalogue their differences, in order to create the proper simulation venues for implementing automated trading algorithms.
2. To develop a series of simulation experiments that will enable study into the performance of adaptive automated trading strategies.
3. To research the automated trading algorithms AA and ZIP in order to understand how they perform the trading, so as to properly evaluate the result when implementing them in simulation environments.
4. To implement AA and ZIP in simulation environments, review the results and demonstrate the simulation environments are realistic.
5. To investigate the performance of AA and ZIP in multiple simulated environments, and then to compare and analyze the results, while ensuring the experiments have both quantitative and qualitative aspects.
6. To identify the significant elements which affect performance, research the associated works and, ideally, improve how they perform.
7. To write up a thesis reflecting and evaluating the final product and work performed.

### Deliverables

- Based on London Stock Exchange’s Turquoise PlatoTM, to study the trading venues implemented in the real world, ensure simulation environments are close to the practical venues as much as possible.
- To use Bristol Stock Exchange (BSE) open-source to create a series of simulation trading venues. Explore how to apply BSE open-source, and once more understand the different trading venues.
- To implement algorithms AA and ZIP in these simulation environments, and verify these environments are a good model of real trading venues. Investigate and analyze the algorithms performance, classify the results and then identify the important factors and potential risks, with the aim being to demonstrate which algorithm performs better in which environment with what conditions.
- A thesis showing my understanding and knowledge about the different trading venues and the automated trading algorithms AA and ZIP, explaining the simulation experiments and evaluating the results.

### Added Value

The simulation trading venues may be used to explore other automated trading algorithms. The analysis may be extended to improve algorithms AA and ZIP or any other algorithms. Moreover, financial professionals and computer scientists may be interested in this project. The performance comparison may be applied to choose the right strategies for different trading environments. There may be applications for preventing markets being adversely impacted by high frequency automated trading, a new electronic market may be implemented to decrease the performance of the present automated trading algorithms. The result of this analysis may be computer scientists deploying even more powerful algorithms. The project could be expanded to test these trading strategies in real venues in order to explore how they perform in real commercial situations.

## Introduction

### The brief history of algorithmic trading

What is algorithmic trading? Automated trading systems usually refer to computer programs that create orders and automatically submit trades to an exchange. In general, these systems are deployed for highly liquid markets known as high-frequency trading (HFT).

Back in the 1602s, Amsterdam Stock Exchange, world's first stock market, formally begun trading in securities. In the 17th century, telegraph cables and a fleet of carrier pigeons were used to run a news delivery system. In 1983, Bloomberg released the world's first computerized system to provide real-time price feed to Wall Street firms.

Till 1998 U.S Securities and Exchange Commission (SEC) authorized electronic exchanges to open the door for computerized High-Frequency Trading. HFT was able to execute trades 1000 times faster than humans. And since that time high-frequency trading (HFT) has been used all over the world. The share of HFT trades has risen rapidly from 35% in 2005 to 56% in 2010.

On May 6th 2010, a world-scale stock market crash swept Wall Street, it is known as the Flash Crash, HFT firms were accused of causing it. However, this couldn't stop the growth of HFT. The share of HFT increased to 70% of total US equity trading by 2012. Along with markets moving to become fully electronic, various evolved markets have been created. In Feb 2014, the HFT tool provider Perseus started accepting bitcoin for its services.

### The impact of algorithmic trading on markets

What is algorithmic trading? Automated trading systems usually refer to computer programs that create orders and automatically submit trades to an exchange. In general, these systems are deployed for highly liquid markets known as high-frequency trading (HFT).

Back in the 1602s, Amsterdam Stock Exchange, world's first stock market, formally begun trading in securities. In the 17th century, telegraph cables and a fleet of carrier pigeons were used to run a news delivery system. In 1983, Bloomberg released the world's first computerized system to provide real-time price feed to Wall Street firms.

Till 1998 U.S Securities and Exchange Commission (SEC) authorized electronic exchanges to open the door for computerized High-Frequency Trading. HFT was able to execute trades 1000 times faster than humans. And since that time high-frequency trading (HFT) has been used all over the world. The share of HFT trades has risen rapidly from 35% in 2005 to 56% in 2010.

On May 6th 2010, a world-scale stock market crash swept Wall Street, it is known as the Flash Crash, HFT firms were accused of causing it. However, this couldn't stop the growth of HFT. The share of HFT increased to 70% of total US equity trading by 2012. Along with markets moving to become fully electronic, various evolved markets have been created. In Feb 2014, the HFT tool provider Perseus started accepting bitcoin for its services.

### The impact of algorithmic trading on markets

During the past decade, as a result of the computerisation of orders, the world has gradually been moving towards electronic trading. There is a large volume of published studies describing the role of algorithmic trading in electronic financial markets. A large and growing body of [literature](12,13,14,15) has investigated the impact of algorithmic trading on the financial markets. The related [literature](13,14) has highlighted that algorithmic trading may affect the liquidity and volatility of the markets it is operating in.

Many changes in the equity markets and their trading processes has occurred. The most obvious change is that trading has become incredibly fast (High-Frequency Trading). A Lit or light pool market will allow traders to see the amount of liquidity that is posted on the bid and offer the order book for security. However, HFT became so pervasive that it grew increasingly difficult to execute large trades through a single exchange. Because large HFT orders had to be spread among multiple exchanges, this would alert trading competitors who could then get in front of the order and snatch up the inventory, driving up share prices. All of this occurred within milliseconds of the initial order being placed. To avoid the transparency of public exchanges and ensure liquidity for large block trades, several of the investment banks established private exchanges, which came to be known as dark pools. Dark pools are a type of platform that allows the trading of large blocks of shares without revealing quantities or prices publicly (to other traders) until trades are completed. (it's not my words)

On the other hands, some exchanges are made for better performance of HFT, such as Ultrahigh-frequency trading. Ultrahigh-frequency trading offers powerful computers to help buying and selling off stocks at extremely fast speed. Algorithms run in Ultrahigh-frequency trading can scan dozens of markets at once, execute thousands of orders a second, and alter strategies in a matter of milliseconds. It is an extremely fitting environment for HFT. However, this has resulted in HFT accounting for 73% of all equity trading volume in the USA.

As well as Exchange traded funds and so on, the innovation of markets is influencing the future of algorithmic trading systems. It is hard not to say algorithmic trading and markets are having an effect on each other. There are more and more strategies and algorithms employed by high-frequency traders to make money. Searching for the best strategy is becoming a significant subject. Due to the proliferation of the types of markets, there is an increasing need to monitor and bid in multiple venues in order to procure the best deal for the desired good.

## Literature Review/Technical Background/Competitor Analysis

### Literature Review of Algorithmic trading systems

Algorithmic trading systems have been widely used in all major markets around the world. A considerable amount of literature has been published on algorithmic trading. To better understand algorithmic trading, the [study](1) of Nuti, Mirghaemi, Treleaven and Yingsaeree give a review of algorithmic trading. According to their study, the type of trading can be categorised into the broker and proprietary. Both AA and ZIP trading algorithms can be considered as broker algorithmic trading systems since the strategy behind is to minimize the cost of trading by minimizing market impact cost or execution time, optimizing the price, and so on. Nuti et al. describe the trading process of algorithmic trading can be split into four steps: pre-trade analysis, trading signal generation, trade execution, and post-trade analysis. Algorithmic trading can be used at any stage of the trading process for various purposes, such as market making, spread trading, arbitrage, and macrotrading. Both AA and ZIP trading algorithms are used in trade execution for spread trading. In view of Nuti et al.'s summary, there are many variants to the order book model, market orders and limit orders are two main types of trades. Both AA and ZIP trading algorithms use limit orders. A limit order guarantees the execution price but it may be executed only partially or not at all. Nuti et al. state different exchanges will accept different order types. When choosing proper trading venues, liquidity, trading mechanism, degree of trader anonymity, and differential execution costs are considered as some of the most important factors. In general, a highly liquid market is preferred, owing to the fast trade execution and low transaction costs. Consequently, to better develop/implement an algorithmic trading system, understanding of the market microstructure, and how the market sorts out orders and executes trades is of paramount importance.

### Literature Review of AA and ZIP trading strategies

To date, a large and growing body of literature has investigated various strategies of algorithmic trading. In this paper, I will be focusing on Adaptive-Aggressive (AA) strategy and Zero-Intelligence-Plus (ZIP) strategy. In particular, both trading strategies are designed to focus on one specific type of market, the Continuous Double Auction (CDA).

ZIP was introduced by D. Cliff and J. Bruten in 1997. A short [article](2) was published by D. Cliff which gives the simple interpretation of ZIP. Assume, for buyers, each trader has a maximum pay price l, but quotes a less price p in the market; for sellers, each trader has a minimum sell price l, but quotes a greater price p in the market. ZIP uses m to represent the difference between l and p which is determined by the trader’s margin. By applying a decision tree machine learning model based on observable market data, ZIP agents will raise or lower its margin to maximise the profit. Commenting on entry strategy of ZIP, D. Cliff argues "At the core of the ZIP family of algorithms is a minimally-simplistic set of qualitative heuristics (that is, some rough rules-of-thumb) for adjusting trader i’s margin m at time t – denoted by mi(t). These heuristics depend on four things: (1) i’s current quote-price pi(t); (2) whether i is still active in the market (i.e., still attempting to trade, or just watching); (3) whether the last price quoted in the marketplace q(t-1) was an offer or a bid; and (4) whether q(t-1) was accepted by a counterparty or not."

In contrast, AA is a fairly recent strategy, published by P. Vytelingum as part of his PhD research in 2006. In Chapter 5 of the PhD [thesis](3), Vytelingum described the concept of strategy applied in AA. In a nutshell, one of the distinguishing features of AA trading algorithm is that it contains two individual adaptive components: a short-term and a long-term learning of the agent’s bidding behaviour. The short-term learning mechanism attempts to promptly respond to market fluctuations. When a bid or ask appears in the market, the agent will update aggressiveness of its bidding based on market data observed. Here, if the agent couldn not transact, it will raise the aggressiveness to increase its chances of transaction; if it did transact, it will reduce the aggressiveness to become more passive in order to increase its profits. The level of trading aggressiveness or passiveness indicates the degree of risk aversion. Higher aggressiveness is associated with higher cost and less risk. Conversely, lower aggressiveness is associated with lower market impact but higher risk. On the other hand, in case of any systematic changes or market shocks, the long-term learning process aid in making bidding decisions. Vytelingum's strategy is to update an aggressiveness model after every successful transaction based on market information observed.

### Literature Review of performance exploration of AA and ZIP trading strategies

Except for the original work, what we know about ZIP is largely based upon empirical studies that investigate its performance in a particular market. In the [report](4) published by R. Das, J. E. Hanson, J. O. Kephart, and G. Tesauro in 2001, it illustrated that ZIP agents outperformed human traders in all experiments. According to the description in the report: The members of the IBM Watson Experimental Economics Laboratory (WEEL) developed GEM, which is a special-purpose distributed system for experimental economics. Magenta is a prototype agent environment developed at IBM Resea. Das et al. developed a hybrid system combining GEM with Magenta for the experiments with humans and agents. In the experiments, two different time periods are used for the different algorithms: “fast” agents were defined as 1 second, and “slow” agents were defined as 5 seconds. The results presented in the experiments employed Gjerstad-Dickhaut (GD) fast agents and ZIP slow agents. The interviews with human subjects draw our attention to a weakness in the ZIP strategy. That is if using a specific non-optimal human strategy such as ‘fixed-profit-ratio’, the ZIP agents performed badly. However, Das et al. implemented a modification to the ZIP strategy. As Das et al. observe: "Preliminary results show that the modified ZIP agents retain high efficiency and are not easily misled by the fixed-profit-ratio agent.". In conclusion, the agents utilized established algorithms, ZIP and GD, outperform non-expert human subjects. As the further work, Das et al. suggest testing their bidding agents against professional equities or commodities traders would assist to uncover more weaknesses in the strategies, thereby leading to significant improvements in the strategies.

To date, several studies have investigated the role of AA trader-agent strategy in the markets. A conference [paper](5) was published by J. Cartlidge, C. Szostek, M. De Luca and D. Cliff in 2012. They explored the performance of AA-ultra and AA-slow to investigate markets efficiency. AA-ultra is a fast trader-agents which interval time is 0.1s, and AA-slow is slow trader-agents which interval time is 10s and agents perform further internal calculations every 2.5s. For a market simulation environment, they applied a new series of artificial trading experiments using the OpEx experimental economics system first introduced at ICAART2011. Every time the market was reset before starting the experiment. Each experiment lasted 20 minutes. 3 buyers and 3 sellers each, a total of 6 human participants and 6 trader-agents traded in the market. AA-slow and AA-ultra were homogeneously configured as the trader-agents respectively. The results of their experiments show that Smith’s alpha values are lower for AA-slow experiments compared to AA-ultra in every replenishment cycle, indicating that slow trader-agents improve market convergence. In comparison with agents, humans perform better when trading against the slower trader-agents. Moreover, the profit dispersion of agents is similar under condition AA-slow and AA-ultra, yet the profit dispersion of humans and the market is apparently lower under condition AA-slow. Evidence from the study propose that slow trader-agents contribute a competitive equilibrium in the markets overall, and slow-agent markets have higher efficiency.

In a similar vein, M. De Luca and D. Cliff in 2015 [investigated](6) the performance of AA, ZIP, Gjerstad-Dickhaut (GD) and GDX in both humans vs. agent and agent vs. agent contexts. They used Open Exchange (OpEx), an experimental algorithmic trading platform, to simulate an electronic trading system. A primary characteristic of using OpEx framework is that multiple instances can be developed in Agent Host. In other words, multiple agents can be implemented at the same time, and each agent applies one specific algorithm and has its own configuration settings. Not only AA and ZIP but also GD and GDX strategies are explored in their study. The GD agent forms belief functions by using observed market data. GDX is a modified GD strategy, it employs Dynamic Programming (DP) to price orders. M. De Luca et al. made a similar build on the work of previous research. They implemented nine of human vs. agent experiments, three for each of ZIP, GDX and AA. Differ from previous work reported, they used 1s as the timing rule for the experiments, aim to simplify the comparison of the performances of the different trading agents. Overall, the agents performed better than humans. In addition, AA performed the best gaining 27% greater profit than humans. In pure agent vs. agent markets, AA, ZIP and GDX competitively traded against each other. In result, GDX beat ZIP, and AA defeated both GDX and ZIP. Moreover, the mean number of rounds per experiment won by AA is higher than GDX.

Much of the current literature on algorithmic trading systems have begun to pay particular attention to the appropriately simulated environment. Several previous research has established that AA offers the best performance of any published bidding strategy. However, [according](7) to D. Cliff (2019), AA agents perform poorly in real-world markets. To date, most researchers investigating AA and ZIP have utilised Open Exchange (OpEx) or ExPo, whereas Bristol Stock Exchange (BSE) was applied in D. Cliff's research. In addition to this, MAA, a modified AA, was implemented to run in a LOB-based market. While, for the purpose of evaluating the performance of the original AA, only the microprice modification was applied in MAA. In the experiments, AA was against three other strategies: ZIC, ZIP, and a BSE built-in strategy SHVR. Moreover, trader-strategy ratios and supply and demand schedules (SDSs) are altered during the experiments. According to Vach (2015), ratios of the various strategies active in the market could heavily affect the measured performance of AA. To avoid this issue, various trading strategies with any given ratio were performed in the market, the performance of trading strategies was calculated summary statistics over a large number of trials collected. In previous studies, SDSs either were set as constant or went through one or more step-changes in the experiments. Apparently, it is not a natural behaviour in real-world markets. This behaviour was improved in Cliff's experiments. Thanks to BSE, a look-up table (LUTs) of real-world financial was used in experiments. A set of experiments were run where the market’s underlying equilibrium price was varied dynamically, aiming to explore whether AA dominates. The results of the experiments reveal that MAA performs significantly worse than either SHVR or ZIP in more realistic environments.

### Literature Review of simulator

Once again, the former example of research (D.Cliff ICAART2019) validates that an experiment environment closer to real-world financial markets is significantly important as the study of automated trading algorithms is mainly based on observational knowledge. For this study, BSE will be employed to simulate a LOB-based financial market.

BSE is an open source software developed and extended by D. Cliff since 2012. In 2018, [BSE](8) is released as a public-domain platform for teaching and research. Due to Cliff's description in the report, BSE LOB can handle a variety of types of order with different priority, including market orders (MKT), limit orders (LIM), good-for-day (GFD), fill-or-kill (FOK), all-or-nothing (AON), immediate-or-cancel (IOC), Iceberg orders (ICE), and so on. As utilized in research (D.Cliff ICAART2019), being able to set more nature supply and demand schedules is a significant characteristic of BSE. In addition to that, a very important feature for this study is that multiple trading venues can be built using BSE as orders can be dealt between two or more trading venues.

### Literature Review of Block Trading

Up to now, the majority of popular research about AA and ZIP has focused on regular-sized bids and offers. However, there are relatively few studies in the area of block trading using any published bidding strategy. A [study](9) of dark pool trading through agent-based modelling was published by S. Y. K. Mo, M. Paddrik and S. Y. Yang in 2013. In their work, a framework of modelling dark pool markets through an agent-based model was introduced. Zhu's [finding](11) illustrates three types of dark pool markets based on their trading mechanisms: matching at exchange prices, non-displayed limit order books and electronic market makers. S. Y. K. Mo et al. simulated the dark pool of matching at the exchange price, the most prevalent and simplified dark pool type. Its mechanism is that matches the mid-point of the bid and ask price from the exchange and behaves as a crossing network that executes randomly. They suggested a set of assumptions to govern market mechanics and traders' behaviours is important to construct an accurate dark pool market, including dark pool market mechanism, participants, price data and no price impact to the market.

In this study, the experiment model will be based on Turquoise Plato™ venue including the Turquoise Plato Block Discovery™ and Turquoise Plato Uncross™. Its majority is owned by the London Stock Exchange (LSE). As documented in the regular website, Turquoise Plato™ has conditional order service aimed at trading larger blocks. Turquoise Plato Block Discovery interacts with Plato Uncross and matches conditional orders at randomised intervals. Size priority in the matching logic and user-defined minimum execution size are included in its trading mechanism.

### Literature Review of Multiple Markets Trading

Moreover, there is a relatively small body of literature that is concerned with if/how AA and ZIP strategies select optimal trades in multi-venue environments. P. Anthony and N. R. Jennings [developed](10) a framework to investigate if an autonomous agent can successfully bid across multiple auctions. They employed genetic algorithms (GAs) aiming to determine what strategies are appropriate and effective in the markets. They defined four environments for experiments. The first one is where there is a short bidding time and a small number of active auctions. The second environment is where there is a short bidding time but a large number of active auctions. In the third environment, the bidding time is relatively long and there is a small number of active auctions. The last environment is where there is a long bidding time with many active auctions. The results of these experiments presented that GAs can be used to successfully evolve bidding strategies for different auction contexts. Reasoning by analogy, I assume adaptive automated trading strategies, AA and ZIP, can operate well in multi-venue environments.

## Proposed Approach/Methodology/Research Questions

### Participants

I will apply AA and ZIP as strategies to design automated trading agents. Since there is a large volume of the lecture has investigated the performance of AA and ZIP. There are loads of information that can be referred to in this study. They contribute to the understanding of AA and ZIP in different environments. Instead of investigating their general performance, this study will focus on investigating their performance in a particular situation. In most of the research, both ZIP and AA were presented as achieving a good performance compared to other published strategies, with AA being described as the best strategy once. This conclusion about AA was, however, changed when changing the experiment environment. It will be useful to record its performance in multiple venues, a new approach that differs from the previous research.

### Simulation Materials

I will use Bristol Stock Exchange (BSE) open-source simulator to set up the experiment environments. It is a relatively new simulator in this field. The BSE GitHub repository provides source-code for the trading algorithms of ZIP and AA. Moreover, a built-in strategy SHVR in BSE will be used as a competitor robot trader against AA and ZIP agents. Documented by D. Cliff, thanks to its distinguished features, varying supply and demand schedules can be set to simulate a closer real-world market. As additional value, this study can contribute to the better understanding and usage of BSE.
  
### Simulation Design

The market mechanics used in the London Stock Exchange’s Turquoise Plato™ venue will be applied in the experiment environment. Due to the description in the regular document, there are two discrete order books for complementary liquidity in Turquoise: Turquoise Lit™ and Turquoise Plato™. Turquoise Lit™ combines simple limit and iceberg orders with Large-In-Scale hidden orders, whereas Turquoise Plato™ is a Price-referencing Order Book. In addition, Turquoise Plato™ contains two mechanisms provided by Turquoise Plato Uncross™ and Turquoise Plato Block Discovery™. Turquoise Plato Uncross™ allows only larger and less time-sensitive passive orders. Turquoise Plato Block Discovery™ requires block orders to be sent to Turquoise Plato Uncross™ in order to maximise available liquidity.

Both light pool and dark pool markets in this study will be designed based on the aforementioned Turquoise venue. To accurately construct the markets, it is important to define the market mechanics and traders' behaviours.

- Light pool market mechanism: This type of market aims to match the orders immediately. It combines limit orders and iceberg orders with Large In Scale hidden orders. Orders will be executed on a price, display type and time priority basis. The priority among the orders is: limit orders will have the highest priority, iceberg orders come in second, and LIS Hidden orders have the lowest priority.
- Light pool market participants: Traders in this market will be informed with opportunity to benefit from rebates. Aggressive orders are allowed to trade in the market, aiming to increase the market liquidity.

- Dark pool market mechanism: This type of market matches the mid-point of the bid and ask price from the exchange. It executes trades randomly at a set number of times during a specific time period as a crossing network. This market has size priority and user-defined minimum execution size. Under size priority, larger orders will have less time-sensitive, participants can rest larger orders for longer to achieve better execution quality in this type of market. Under user-defined minimum execution size, participants can initiate a trade with an aggressive order. In addition, without preference to time-sensitive, participants can initiate and choose the execution time.
- Dark pool market participants: Uninformed traders can trade in this market and each trader is expected to trade at each given time period, aiming to avoid price impact. Only passive orders from buyers and sellers are allowed in this market.

### Experiment Procedure

The aim of these experiments is to determine which strategy is more effective in particular environments. AA, ZIP and SHVR traders will run in the three different environments: only light pool market, only dark pool market, the market combined light pool with block orders. The performance will be evaluated and measured as average profitability per trader, compared against other trading strategies. The combination will be AA vs. ZIP, AA vs. SHVR, ZIP vs. SHVR. The experiments will be implemented under a variety of supply and demand schedules. Additionally, the simulation markets will have varying population sizes. For any given population size, the experiments will be implemented across an exhaustive sequence of strategy-ratios.

## Reference

1. [Algorithmic Trading](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/5696713/authors#authors)
2. [My Family and Other Algorithms](https://eprints.soton.ac.uk/264236/1/ZIP_1500wV2_ep.pdf)
3. [P. Vytelingum. The Structure and Behaviour of the Continuous Double Auction. PhD thesis, University of Southampton, 2006.](https://eprints.soton.ac.uk/263234/1/THESIS.pdf)
4. [R. Das, J. E. Hanson, J. O. Kephart, and G. Tesauro. Agent-human interactions in the continuous double auction. The Proceedings of the International Joint Conferences on Artificial Intelligence (IJCAI), Seattle, USA (August, 2001), 2001.](https://s3.amazonaws.com/academia.edu.documents/44417575/das.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1556512970&Signature=JT7dTpWP0YqQRQx1avBwaZBS3uk%3D&response-content-disposition=inline%3B%20filename%3DAgent-Human_Interactions_in_the_Continuo.pdf)
5. [TOO FAST – TOO FURIOUS: Faster Financial-Market Trading Agents Can Give Less Efficient Markets](https://www.researchgate.net/profile/John_Cartlidge/publication/273060607_Too_fast_too_furious_Faster_financial_market_trading_agents_can_give_less_efficient_markets/links/55882dfa08aeb29944448104.pdf)
6. [Evaluation of the “Adaptive-Aggressive” Trading-Agent Strategy Against Human Traders in CDA: AA Wins](https://www.researchgate.net/profile/Dave_Cliff/publication/267767159_Evaluation_of_the_Adaptive-Aggressive_Trading-Agent_Strategy_Against_Human_Traders_in_CDA_AA_Wins/links/54b791d40cf2bd04be33a4e5.pdf)
7. [Exhaustive Testing of Trader-agents in Realistically Dynamic Continuous Double Auction Markets: AA Does Not Dominate](local)
8. [An Open-Source Limit-Order-Book Exchange for Teaching and Research](https://ieeexplore-ieee-org.bris.idm.oclc.org/abstract/document/8628760)
9. [A study of dark pool trading using an agent-based model](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6611692/references#references)
10. [Evolving Bidding Strategies for Multiple Auctions](http://www.frontiersinai.com/ecai/ecai2002/pdf/p0178.pdf)
11. [H. Zhu, "Do Dark Pools Harm Price Discovery?," Available at SSRN 1712173, 2012.]()
12. [Rise of the Machines: Algorithmic Trading in the Foreign Exchange Market](https://onlinelibrary-wiley-com.bris.idm.oclc.org/doi/full/10.1111/jofi.12186)
13. [Does Algorithmic Trading Improve Liquidity?](https://onlinelibrary-wiley-com.bris.idm.oclc.org/doi/full/10.1111/j.1540-6261.2010.01624.x)
14. [Algorithmic Trading and the Market for Liquidity](https://www-cambridge-org.bris.idm.oclc.org/core/services/aop-cambridge-core/content/view/C1A34D3767436529EA4F23DB1780273C/S0022109013000471a.pdf/algorithmic_trading_and_the_market_for_liquidity.pdf)
15. [Assessing the Impact of Algorithmic Trading on Markets: A Simulation Approach](https://pdfs.semanticscholar.org/820f/a261b451f5b57decf4f8ccf526247fcbc2ff.pdf)


## Gannt Chart of Project Plan

The overview of the figure1, task1 to task3 are design Phase, task4 is developing and test Phase, task5 and task6 are analysis phase. The draft will be written down to go through the whole phase.

Task1: the investigation of electronic trading markets
Description: Research and collect information about the electronic trading markets: Turquoise Lit and Turquoise Plato. To a better understanding, the pre-investigation of general electronic trading markets is considerable. Given that the design of the dark pool is more complex than the lit pool, 2 days are allocated for the study of Turquoise Plato.
Milestone: Milestone is reached when the design of markets is completed.
Deliverable: Write up the design of the markets which will be simulated. Get the review and feedback of the design.

Task2: the investigation of automated trading strategies
Description: Research and collect information about automated trading strategies: Adaptive Aggressive (AA) or Zero-Intelligence Plus (ZIP). The study of automated trading strategies is divided into theory and practice.
Milestone: Milestone is reached when the design of the algorithm of automated trading strategies is completed.
Deliverable: Write up the theory based algorithms of AA and ZIP. Get the review and feedback of algorithms design.

Task3: the investigation of the simulator
Description: Research and collect information about the simulator: Bristol Stock Exchange (BSE). The investigation of BSE is divided into the simulation of venues and agents. Three different agents will be built to compete in the market, one more day is allocated for the study of the simulation of agents than the simulation of venues.
Milestone: Milestone is reached when the development framework of BSE is completed.
Deliverable: Install the source code of BSE. Write up how to implement the BSE. Write up how to simulate the venues using BSE. Write up how to build the agents using BSE. Get the review and feedback of the draft.

Task4: experiment setups
Description: Build and test experiment environments and agents. The experiment environment and agents will be built based on the design. Given the rest performance comparison and analysis is based on experiments, 26 days are allocated for developing and testing the experiment environments and agents.
Milestones: Milestone is reached when the experiment environments and agents are completed.
Deliverable: Build a lit pool venue and an independent dark pool venue. Build a venue combines two venues with different mechanisms. Build three robot agents using AA, ZIP and SHVR strategies respectively. Repeat test and modification, aiming to guarantee the quality of the experiment.

Task5: performance comparison/analysis of the automated trading agents
Description: Collect and analyze the data of the experiments. Assume there is no more code modification, 9 days in total are allocated to investigate the results of experiments.
Milestones: Milestone is reached when the experiments and analysis of results are completed.
Deliverable: Different scenarios will be designed and executed: the performance when AA and ZIP are applied in a single venue, the performance when AA and ZIP are applied in multiple venues. The combination will be AA vs. ZIP, ZIP vs. SHVR, AA vs. SHVE and AA vs. ZIP vs. SHVE. Each experiment will use different trader-strategy ratios and supply and demand schedules. Each experiment will be recorded and evaluated. Compare the performance when AA and ZIP are implemented in different situations.

Task6: final write-ups
Description: Summarize and modify the draft of the research process. Given that it's the research over two months, 10 days are allocated for writing up the thesis.
Milestones: Milestone is reached when the thesis is completed.
Deliverable: Write up the thesis based on the draft. Repeat review and edition, attempt to improve the quality of the thesis.

## Risk Analysis

There are a number of risks that could affect the progress of the project. The likelihood rating is on a scale 1-5 where each point p represents a p/5 probability of incidence. In the same way, severity indicates the p/5 possibility of the risk having implications for the project.

### Risk1

Misunderstand the mechanism used in Turquoise Plato.

likelihood: 2
severity: 3
Notes and Contingency: Keep in mind of review is important. If it occurs in the design phase, there is 1 buffer day to recover. If the mistake is realized in develop or test phase, there are 3 days to recover. If the recovery takes more time than expected, simulate a general dark pool instead of Turquoise Plato. The experiment environment may be not close to the real-world market, but the important scenario of environment that agents perform in multiple venues can be implemented as planned.

### Risk2

Misunderstand the theory of ZIP.

likelihood: 1
severity: 3
Notes and Contingency: The review in the design phase is important. If it occurs in the design phase, there is 1 buffer day to recover. If the mistake is realized in develop or test phase, there are 3 days to recover. Utilise the available source code provided by BSE.

### Risk3

Misunderstand the theory of AA.

likelihood: 2
severity: 3
Notes and Contingency: This would happen since the source code of AA doesn't provide publicly. The review in the design phase is important. If it occurs in the design phase, there is 1 buffer day to recover. If the mistake is realized in develop or test phase, there are 3 days to recover. Utilise the available source code provided by BSE.

### Risk4

The research about ZIP and AA takes more time than expected.

likelihood: 1
severity: 2
Notes and Contingency: Thanks to the large volume of the lecture, this should not happen. There is 1 day to recover in case it happened.

### Risk5

Setting up the development environment takes more time than expected.

likelihood: 1
severity: 2
Notes and Contingency: This may not happen since it's as open-source and has been used to exam the performance of AA and ZIP. If it happens, ask for experts.

### Risk6

The simulator does not provide a specific feature to simulate the markets designed.

likelihood: 1
severity: 4
Notes and Contingency: Research and investigate OpEx or ExOp replace BSE. If neither OpEx nor ExOp has no specific feature to simulate. Change the design of markets. I would be the worst case.

### Risk7

Development of the experiment environment takes more time than expected.

likelihood: 2
severity: 1
Notes and Contingency: It is a usual case happens during a project. There are 3 days as a buffer if the schedule is delayed. Fully utilise the available source code provided by BSE. Discuss with experts of BSE.

### Risk8

The scenarios of the experiment are not enough.

likelihood: 3
severity: 4
Notes and Contingency: This issue would affect the quantity of the experiments. Implement experiments by learning from the previous researches. Classify the experiments to cover different cases.

### Risk9

The results of the experiment are different from expected.

likelihood: 3
severity: 2
Notes and Contingency: This means either the experiment environment is wrong or unexpected results occurs. More experiments in the different scenarios with varying parameters, more deliberately analysis are considerable. Record and classify the results is required.

### Risk10

Writing up thesis takes more time than expected.

likelihood: 3
severity: 4
Notes and Contingency: This may happen when the edit delayed or the feedback is too bad. Tracking the progress of the project and keeping writing up the draft day by day is required.