# Assignment — Use Case 3: E-Commerce Review Intelligence
## GenAI Course · Sessions 3–6 Capstone Assignment

---

## Overview

You are building an **AI-powered review analysis system** for an e-commerce seller.

The seller receives 500–2000 customer reviews every day on platforms like Flipkart and Amazon. Reading them manually is impossible. Your job is to build a pipeline that automatically reads, understands, and extracts structured intelligence from every review — overnight, in bulk, at near-zero cost.

**This is a real product.** Everything you build here maps directly to a production system a startup would ship.

---

## Problem Statement

A seller selling phone accessories on Flipkart gets 1000+ reviews per day.

**Current situation (without AI):**
- A support executive reads reviews manually — 2–3 hours per day
- Urgent complaints (safety issues, defective batch) get noticed 2–3 days late
- No trend visibility — are complaints about the charging cable increasing or decreasing?
- No time to reply to negative reviews individually

**Your task:** Replace this manual process with an automated LangChain pipeline.

---

## What You Will Build

A Python script or Jupyter notebook that takes a list of customer reviews and produces structured analysis for each one.

### Input

```python
reviews = [
    {
        "review_id": "R001",
        "product": "USB-C Fast Charging Cable 2m",
        "rating": 2,
        "text": "Bought this 3 weeks ago. The cable stopped working after just 10 days. The connector gets very hot during charging which is dangerous. Worst purchase ever. Demanding a full refund."
    },
    {
        "review_id": "R002",
        "product": "USB-C Fast Charging Cable 2m",
        "rating": 5,
        "text": "Excellent build quality! Charges my phone from 0 to 100 in 45 minutes. The braided design looks premium and feels durable. Using it daily for 2 months, no issues at all."
    },
    {
        "review_id": "R003",
        "product": "USB-C Fast Charging Cable 2m",
        "rating": 3,
        "text": "Charging speed is good but the cable length is a bit short for my setup. Also the connector is slightly loose in my phone port. Decent for the price though."
    },
    {
        "review_id": "R004",
        "product": "USB-C Fast Charging Cable 2m",
        "rating": 1,
        "text": "SCAM PRODUCT. This is not fast charging at all. Same speed as a normal cable. The product images are misleading. I will be filing a complaint with consumer court if no action is taken."
    },
    {
        "review_id": "R005",
        "product": "USB-C Fast Charging Cable 2m",
        "rating": 4,
        "text": "Pretty good cable. Fast charging works well with my Samsung. Build quality seems solid. Only complaint is the packaging could be better — box was damaged when delivered."
    }
]
```

### Expected Output (for each review)

```python
(
    review_id="R001",
    sentiment="Negative",
    confidence=0.97,
    features=["connector heating", "cable durability", "charging speed"],
    summary="Cable stopped working after 10 days with dangerous connector overheating.",
    urgent=True,
    urgency_reason="Safety concern: connector overheating reported. Potential product defect.",
    suggested_reply="We sincerely apologize for this experience. Connector overheating is a serious concern and we are escalating this immediately. Please DM us your order ID for a full refund and replacement."
)
```
