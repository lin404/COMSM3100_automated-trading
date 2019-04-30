# Performance Comparison of Automated Trading Algorithms

## Literature Review/Technical Background/Competitor Analysis - 3

Once again, the former example of research (D.Cliff ICAART2019) validates that an experiment environment closer to real-world financial markets is significantly important as the study of automated trading algorithms is mainly based on observational knowledge. For this study, BSE will be employed to simulate a LOB-based financial market.

BSE is an open source developed and extended by Dave Cliff since 2012. In 2018, [BSE](1) is released as a public-domain platform for teaching and research. Due to Cliff's description in the report, BSE LOB can handle a variety of types of order with different priority, including market orders (MKT), limit orders (LIM), good-for-day (GFD), fill-or-kill (FOK), all-or-nothing (AON), immediate-or-cancel (IOC), Iceberg orders (ICE), and so on. As utilized in research (D.Cliff ICAART2019), being able to set varying nature supply and demand schedules is a significant characteristic of BSE. Addition to that, a very important feature for this study is that multiple trading venues can be built using BSE as orders can be dealt between two or more trading venues.

Up to now, the majority of popular research about AA and ZIP has focused on regular-sized bids and offers. However, there are relatively few studies in the area of block trading using any published bidding strategy. A [study](2) of dark pool trading through agent-based modelling was published by S. Y. K. Mo, M. Paddrik and S. Y. Yang in 2013. In their work, a framework of modelling dark pool markets through an agent-based model was introduced. Zhu's [finding](4) illustrates three types of dark pool markets based on their trading mechanisms: matching at exchange prices, non-displayed limit order books and electronic market makers. S. Y. K. Mo et al. simulated the dark pool of matching at the exchange price, the most prevalent and simplified dark pool type. Its mechanism is that matches the mid-point of the bid and ask price from the exchange and behaves as a crossing network that executes randomly. They suggested a set of assumptions to govern market mechanics and traders' behaviours is important to construct an accurate dark pool market, including dark pool market mechanism, participants, price data and no price impact to the market.

For the purposes of this study, the experiment model will be based on Turquoise Plato™ venue including the Turquoise Plato Block Discovery™ and Turquoise Plato Uncross™. It is majority owned by the London Stock Exchange (LSE). As documented in the regular website, Turquoise Plato™ has conditional order service aimed at trading larger blocks. Turquoise Plato Block Discovery interacts with Plato Uncross and matches conditional orders at randomised intervals. Size priority in the matching logic and user-defined minimum execution size are included in its trading mechanism.

In addition, there is a relatively small body of literature that is concerned with if/how known adaptive automated trading strategies select optimal trade in multi-venue environments. ?




1. [An Open-Source Limit-Order-Book Exchange for Teaching and Research](https://ieeexplore.ieee.org/abstract/document/8628760)
2. [A study of dark pool trading using an agent-based model](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6611692/references#references)
3. [Limit order placement across multiple exchanges](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6327772)
4. [H. Zhu, "Do Dark Pools Harm Price Discovery?," Available at SSRN 1712173, 2012.]()