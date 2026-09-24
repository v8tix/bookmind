<span id="page-0-0"></span>

# Quiet Queues

## How Backpressure Keeps Systems Honest

Ilse Moravec-Adjei

Brightwater Technical Press, 2025

<span id="page-1-0"></span>

# *contents*

*preface vii*

# *1 [Why queues back up](#page-12-0) 1*

1.1 Arrival and service rates 2 ■ 1.2 Little's law in practice 3

# *2 [Backpressure as a contract](#page-16-0) 5*

2.1 Saying no early 6 ■ 2.2 Where to push back 7

<span id="page-7-0"></span>

# *preface*

This short book collects what I learned running message pipelines for a logistics company. It assumes you have operated at least one queue in production.

<span id="page-12-0"></span>

# *1 Why queues back up*

A queue is a promise that work will be done later. When work arrives faster than it can be served, the queue grows, and every item in it waits longer. Nothing about a queue makes it drain on its own; only a change in arrival or service rate does.

<span id="page-13-0"></span>

## 1.1 Arrival and service rates

If items arrive at 120 per second and a worker pool serves 100 per second, the backlog grows by 20 items every second, without limit. Adding workers raises the service rate, but only until a shared dependency, such as a database, becomes the bottleneck.

<span id="page-14-0"></span>

## 1.2 Little's law in practice

Little's law says the average number of items in a system equals the arrival rate times the average time each item spends there. A queue holding 6,000 items at 100 items per second means each new item waits about a minute.

<span id="page-16-0"></span>

# *2 Backpressure as a contract*

Chapter 1 showed that a growing queue only hides overload; it does not absorb it. This chapter asks what a system should do instead.

<span id="page-17-0"></span>

## 2.1 Saying no early

My central claim is that a bounded queue that rejects work early is kinder than an unbounded one that accepts everything and fails late. A caller that gets an immediate "busy, retry later" can slow down, route elsewhere, or tell its user. A caller whose request sits in a queue for ten minutes and then times out has lost those options, and has spent resources the whole time.

<span id="page-18-0"></span>

## 2.2 Where to push back

Push back at the edge where a decision can still be made: the API gateway or the producer, not a worker deep inside the pipeline. Rejections should carry a reason and a suggested wait, so that callers back off instead of retrying at once and making the overload worse.
