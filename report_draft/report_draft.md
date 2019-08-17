# Draft

## 0_abstract

In electronic financial markets, automatic algorithmic trading systems have largely replaced human traders. Along with the growth of automatic algorithmic trading systems, many of the world's major financial markets are experiencing changes as well, with the rise of dark pools markets being one of the most profound. These changes have created significant demand for automatic algorithmic trading systems that operate in multiple markets. This research aims to investigate if the existing, well-known automatic trading strategies, AA and ZIP, can operate successfully in multi-venue environments containing both light pools and dark pools.

## 1_introduction

tells the reader the whole story of the thesis, condensed into a few pages

## 2_Background

explains the wider real-world context for the work done here (e.g.: summarise recent changes in financial markets).

## 3_Relevant Literature

summarises the key academic / peer-reviewed papers/articles/books that your work draws upon or builds on.

## 4_Problem Statement

recap of the key bits of the Ch2 and Ch3 and a statement/plan for the work you will be describing in the rest of the thesis, i.e. this is where you tell the reader exactly what you set out to do.

## 5_Design Issues

discussion of any design decisions and/or implementation issues.

### description

* bid/ask
- The ask price is what a seller is willing to take for it
- The bid price is what a buyer is willing to pay for it

* order flow
- customer orders
- traders
- orders

* Minimum Indication Value - MIV (P27)
* Minimum Notification Value - MNV (P28)

### conquer

* Weighted Random Selection - choose BI or BDN
- 2 approaches
- Python3.6 -> method choices from random module
- results?
- reference:
https://medium.com/@peterkellyonline/weighted-random-selection-3ff222917eb6
https://softwareengineering.stackexchange.com/questions/150616/get-weighted-random-item

* ISSUE-1 zip-zip error occurred.
- quantity is reduced after partial filled -> however dark pool/lit pool depends on quantity
- ZIP only market -> process_order_take -> partial filled -> cancel error occurred
- ISHV market -> process_LIM only -> add to book, no order executed -> del 'CAN' order
- condition of process_order_take/process_LIM
best price (Bid: oprice >= self.bids.lob[0][0] | Ask: oprice <= self.asks.lob[0][0])
ISHV ask-200, bid-1 is the best forever

**drk pool orders keep in drk pool**

* solutions:
- all lit or all drk
- use ISHV instead of ZIP only -> no process_order_take?
- after partial filled, delete order or remove order to lit
- only generate big block orders with BI or BDN orders

### implementation
> 5.2 Event Model P16

* use ZIP only
- add marketid to keep partial executed orders in drk_pool
- the quantity of order is 1-200, 200-300, give a weight 0.5-1 to generate small_block and big_block orders

* generate BI/BDN orders
- add subtype(BI/BDN), limited_price, MES to Order
- add bi_weight/bdn_weight, reputation to Trader
- BI orders quotes

* add BI/BDN orders to order book
- del_bi_order when bi_quotes > bi_max_quotes
- delete BDN on bi_book when BDN == 'CAN'
- delete BDN order when order is executed in ExchDrk
- add Discovery process_order, generate order_id in market_session(). send BI/BDN to Discovery, send BDN/others to Exchange.
- filter out ineligible orders, give any value to miv/mnv
- add orders to bi_book
- A BI which has been matched will then be expired automatically.(P46) -> not add BI to book when match is found

* match orders
> 11.0 Matching Priority (P41, P47)
- add MES = 1, limit_price for matching
- add OSR when BI found match.
- delete full fill BI from quotes, do not add to book
- update order.qty when partial filled, add to book
- BDN order do not update order.qty and always add to book

* return OSR (Order Submission Request)
- record OSR in Discovery for update reputation later
- list of osr, osr includes original order, Executed Price, Size and Time
- add request of QBO to trader QBO_order list -> no matter FULL/PARTIAL fill

* generate QBO
- random choice normal order/QBO
- check expired orders
- set up price and qty

* add QBO to order book
* update reputation
> 5.3.5 Reputational Scoring P23
- score calculation
- reputation score should be stored in discovery
- Composite Reputational Score? --> TODO

* report format -->Confirm if have any?

## 6_Results

this could easily be more than one chapter, depending on how many different sets of results you generated

## 7_Analysis and Discussion

in-depth discussion of the results and their implications etc

## 8_Further Work

what you would do if you had another week, another month, another year to work on your project

## 9_Conclusions

basically here you summarise the entire thesis, in past-tense

