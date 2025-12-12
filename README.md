# 🤖 Crypto Trading Bot (Testnet)

A Python-based command-line interface (CLI) trading bot designed for the Binance Futures Testnet. This bot allows users to place various types of orders and check their wallet balance in a safe, simulated environment.

## 🌟 Features

*   **Market Orders**: Instantly buy or sell crypto at the current market price.
*   **Limit Orders**: Set a specific price to buy or sell.
*   **Stop-Limit Orders**: Advanced ordering with stop triggers and limit execution prices.
*   **Wallet Balance**: Check your current USDT balance on the Futures Testnet.
*   **Logging**: Automatically logs all trade activities and errors to `Trading log` for review.

## 🛠️ Prerequisites

*   Python 3.12.3 or Above
*   A Binance Futures Testnet Account (Get API keys from [testnet.binancefuture.com](https://testnet.binancefuture.com/))

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd Stock_trading_bot
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys**
    Create a `.env` file in the root directory and add your Binance Testnet keys:
    ```env
    API_KEY=your_testnet_api_key_here
    API_SECRET=your_testnet_api_secret_here
    ```

## 💻 Usage

Run the main display script to start the interactive bot:

```bash
python display.py
```

### Menu Options
1.  **Place Market Order**: Enter symbol (e.g., BTCUSDT), side (BUY/SELL), and quantity.
2.  **Place Limit Order**: Includes price entry.
3.  **Place Stop-Limit Order**: Includes trigger price and execution price.
4.  **Check Balance**: Displays current USDT balance.
5.  **Exit**: Closes the application.

## 📂 Project Structure

*   `display.py`: Main entry point. Handles user input, menu display, and interaction.
*   `logic.py`: Contains the `BasicBot` class with core trading logic and Binance API connections.
*   `requirements.txt`: List of Python dependencies.
*   `.env`: Stores sensitive API credentials (not uploaded to GitHub).
*   `Trading log`: Stores logs of bot activity.

## ⚠️ Disclaimer

This bot is configured for the **Binance Testnet** by default. Use at your own risk. Always test thoroughly in the simulation environment before modifying the code for real trading. The authors are not responsible for any financial losses.
