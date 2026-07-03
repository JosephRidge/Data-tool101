import streamlit as st

st.title("Online Customer Segmentation and Analysis of a UK Online Retail Store")
st.caption("Automated Customer Segmentation Dashboard")

st.markdown(
"""
**Dataset Reference**

Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository.

https://doi.org/10.24432/C5BW33

Dataset: https://archive.ics.uci.edu/dataset/352/online+retail
"""
)

st.divider()

# ==========================
# Business Metrics
# ==========================
st.subheader("Business Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Revenue",
        "£9,747,747.93",
        border=True
    )
    st.metric(
        "Legitimate Revenue",
        "£8,300,065.81",
        border=True
    )
    st.metric(
        "Customers",
        "406,829",
        border=True
    )
    st.metric(
        "Countries",
        "38",
        border=True
    )

with col2:
    st.metric(
        "Potential Fraudulent Revenue",
        "£1,447,682.12",
        border=True
    )
    st.metric(
        "Purchases",
        "541,909",
        border=True
    )
    st.metric(
        "Ghost Customers",
        "135,080",
        border=True
    )
    st.metric(
        "Observation Period",
        "373 Days",
        border=True
    )

st.divider()

# ==========================
# Dataset Metrics
# ==========================
st.subheader("Dataset Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Flagged Purchases",
        "135,080",
        border=True
    )

with col2:
    st.metric(
        "Unique Stock Items",
        "4,070",
        border=True
    )

st.divider()

# ==========================
# Summary
# ==========================
st.subheader("Summary")

st.markdown("""
#### Sales Quantity

- Average quantity sold per transaction: **10 units**
- 25% of transactions contained **fewer than 1 unit**
- Median transaction quantity: **3 units**
- 75% of transactions contained **fewer than 10 units**

#### Customer Spending

- Average transaction value: **£17.99**
- 25% of transactions were below **£3.40**
- Median transaction value: **£9.75**
- 75% of transactions were below **£17.40**

#### Product Overview

- The dataset contains **4,070 unique stock items**.
- The highest-selling product is **Stock Code 85123A** (*WHITE HANGING HEART T-LIGHT HOLDER*).
- The **United Kingdom** generated the highest sales volume.

#### Data Quality

Invoice numbers appear multiple times because each invoice can contain several products. Each row represents an individual line item within an invoice rather than a separate purchase. This is expected in transactional retail datasets and should not be interpreted as duplicated transactions.
""")