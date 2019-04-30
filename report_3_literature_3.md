# Performance Comparison of Automated Trading Algorithms

## Literature Review/Technical Background/Competitor Analysis - 3

Once again, the former example of research (D.Cliff ICAART2019) confirms that an experiment environment closer to real-world financial markets is significantly important as the study of automated trading algorithms is mainly based on observational knowledge. For this study, BSE will be employed to simulate a LOB-based financial market.

BSE is an open source developed and extended by Dave Cliff since 2012. In 2018, [BSE](1) is released as a public-domain platform for teaching and research. Due to Cliff's description in the report, BSE LOB can handle a variety of types of order with different priority, including market orders (MKT), limit orders (LIM), good-for-day (GFD), fill-or-kill (FOK), all-or-nothing (AON), immediate-or-cancel (IOC), Iceberg orders (ICE), and so on. As utilized in research (D.Cliff ICAART2019), being able to set more nature supply and demand schedules is a significant characteristic of BSE. Addition to that, a very important feature for this study is that multiple trading venues can be built using BSE as orders can be dealt between two or more trading venues.

Up to now, the majority of popular research has focused on regular-sized bids and offers. However, there are relatively few studies in the area of block trading. A [study](2) of dark pool trading was pubilished by S. Y. K. Mo, M. Paddrik and S. Y. Yang in 2013.



In addition, there is a relatively small body of literature that is concerned with if/how known adaptive automated trading strategies select optimal trade in multi-venue environments. ?

1. [An Open-Source Limit-Order-Book Exchange for Teaching and Research](https://ieeexplore.ieee.org/abstract/document/8628760)
2. [A study of dark pool trading using an agent-based model](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6611692/references#references)
3. [Limit order placement across multiple exchanges](https://ieeexplore-ieee-org.bris.idm.oclc.org/document/6327772)