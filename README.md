# NSE Stock Analysis App

A Streamlit application to extract real-time and historical data from the National Stock Exchange (NSE) of India. This app provides various analytical tools for stock market data, including Bhavcopy, stock delivery data, open interest analysis, and more.

## Features

- **Bhavcopy Display**: Fetch and download Bhavcopy data for specified dates and segments (Cash or FnO).
- **Stock Delivery Data**: Analyze delivery data with candlestick chart visualizations.
- **High/Low Delivery**: Identify stocks with the highest and lowest delivery percentages.
- **Stock OI Data**: Examine open interest data with visual representations.
- **Future Builtup**: Categorize built-ups for futures data (long/short).
- **Historical Option Chain**: Retrieve historical option chain data for specific symbols and dates.
- **Put Call Ratio**: Analyze the put-call ratio with visualizations.
- **Max Pain**: Calculate and visualize the max pain point for options.

## Prerequisites

- Python 3.6 or higher
- Required libraries:
  - `streamlit`
  - `pandas`
  - `matplotlib`
  - `mplfinance`
  - `plotly`
  - `git+https://github.com/boyalasaiganesh/pynse.git`

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/boyalasaiganesh/pynse.git
cd pynse
pip install -r requirements.txt
