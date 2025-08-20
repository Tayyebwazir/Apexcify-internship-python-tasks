import streamlit as st
import csv
from datetime import datetime


STOCK_PRICES = {
    "AAPL": 180.50,  # Apple
    "TSLA": 250.75,  # Tesla
    "GOOGL": 2800.25, # Google
    "MSFT": 415.30,   # Microsoft
    "AMZN": 3200.40,  # Amazon
    "META": 320.15,   # Meta (Facebook)
    "NVDA": 450.80,   # NVIDIA
    "NFLX": 380.90,   # Netflix
    "AMD": 95.60,     # AMD
    "INTC": 28.45     # Intel
}

def calculate_portfolio_value(portfolio):
    """
    Calculate total investment value based on stock quantities and prices
    """
    total_value = 0.0
    portfolio_details = []
    
    for stock_symbol, quantity in portfolio.items():
        if stock_symbol in STOCK_PRICES:
            stock_price = STOCK_PRICES[stock_symbol]
            stock_value = stock_price * quantity  
            total_value += stock_value
            
            portfolio_details.append({
                "stock": stock_symbol,
                "quantity": quantity,
                "price": stock_price,
                "total_value": stock_value
            })
        else:
            st.warning(f"Stock {stock_symbol} not found in our database!")
    
    return total_value, portfolio_details

# Function to save portfolio to text file (Key Concept: File Handling)
def save_portfolio_txt(portfolio_details, total_value, filename="portfolio.txt"):
    """
    Save portfolio details to a text file
    """
    try:
        with open(filename, "w") as file:
            file.write("=== STOCK PORTFOLIO REPORT ===\n")
            file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("-" * 40 + "\n")
            
            for item in portfolio_details:
                file.write(f"Stock: {item['stock']}\n")
                file.write(f"Quantity: {item['quantity']}\n")
                file.write(f"Price per share: ${item['price']:.2f}\n")
                file.write(f"Total Value: ${item['total_value']:.2f}\n")
                file.write("-" * 40 + "\n")
            
            file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
        
        return True
    except Exception as e:
        st.error(f"Error saving to text file: {e}")
        return False

# Function to save portfolio to CSV file (Key Concept: File Handling)
def save_portfolio_csv(portfolio_details, total_value, filename="portfolio.csv"):
    """
    Save portfolio details to a CSV file
    """
    try:
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Stock_Symbol", "Quantity", "Price_Per_Share", "Total_Value"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write portfolio data
            for item in portfolio_details:
                writer.writerow({
                    "Stock_Symbol": item['stock'],
                    "Quantity": item['quantity'],
                    "Price_Per_Share": item['price'],
                    "Total_Value": item['total_value']
                })
            
            # Write total row
            writer.writerow({
                "Stock_Symbol": "TOTAL",
                "Quantity": "",
                "Price_Per_Share": "",
                "Total_Value": total_value
            })
        
        return True
    except Exception as e:
        st.error(f"Error saving to CSV file: {e}")
        return False

# Console-based version for demonstration
def console_portfolio_tracker():
    """
    Console version of the portfolio tracker for learning purposes
    """
    print("=== STOCK PORTFOLIO TRACKER (Console Version) ===")
    print("Available stocks:", list(STOCK_PRICES.keys()))
    print("-" * 50)
    
    portfolio = {}  # Dictionary to store user's portfolio
    
    while True:
        # Input/Output operations
        stock_input = input("Enter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock_input == 'DONE':
            break
        
        if stock_input in STOCK_PRICES:
            try:
                quantity = int(input(f"Enter quantity for {stock_input}: "))
                if quantity > 0:
                    portfolio[stock_input] = quantity
                    print(f"Added {quantity} shares of {stock_input}")
                else:
                    print("Quantity must be positive!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print(f"Stock {stock_input} not available. Available stocks: {list(STOCK_PRICES.keys())}")
        
        print("-" * 30)
    
    # Calculate and display results
    if portfolio:
        total_value, details = calculate_portfolio_value(portfolio)
        
        print("\n=== PORTFOLIO SUMMARY ===")
        for item in details:
            print(f"{item['stock']}: {item['quantity']} shares × ${item['price']:.2f} = ${item['total_value']:.2f}")
        
        print(f"\nTOTAL PORTFOLIO VALUE: ${total_value:.2f}")
        
        # File saving option
        save_option = input("\nSave to file? (txt/csv/no): ").lower()
        if save_option == 'txt':
            if save_portfolio_txt(details, total_value):
                print("Portfolio saved to portfolio.txt")
        elif save_option == 'csv':
            if save_portfolio_csv(details, total_value):
                print("Portfolio saved to portfolio.csv")
    else:
        print("No stocks added to portfolio!")

# Main Streamlit application
def main():
    """
    Main function for Streamlit UI
    """
    # Page configuration
    st.set_page_config(
        page_title="Stock Portfolio Tracker",
        page_icon="📈",
        layout="centered"
    )
    
    # Title
    st.title("📈 Simple Stock Portfolio Tracker")
    st.write("Track your investments with predefined stock prices")
    
    # Display available stocks
    st.subheader("Available Stocks")
    col1, col2 = st.columns(2)
    
    stock_list = list(STOCK_PRICES.items())
    mid_point = len(stock_list) // 2
    
    with col1:
        for stock, price in stock_list[:mid_point]:
            st.write(f"**{stock}**: ${price:.2f}")
    
    with col2:
        for stock, price in stock_list[mid_point:]:
            st.write(f"**{stock}**: ${price:.2f}")
    
    # Initialize session state for portfolio
    if "portfolio" not in st.session_state:
        st.session_state.portfolio = {}
    
    # Input section
    st.subheader("Add Stocks to Portfolio")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        selected_stock = st.selectbox(
            "Select Stock:",
            options=list(STOCK_PRICES.keys()),
            key="stock_selector"
        )
    
    with col2:
        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10000,
            value=1,
            key="quantity_input"
        )
    
    with col3:
        st.write("") # Empty space for alignment
        add_button = st.button("Add Stock", type="primary")
    
    # Add stock to portfolio
    if add_button:
        if selected_stock in st.session_state.portfolio:
            st.session_state.portfolio[selected_stock] += quantity
            st.success(f"Added {quantity} more shares of {selected_stock}")
        else:
            st.session_state.portfolio[selected_stock] = quantity
            st.success(f"Added {quantity} shares of {selected_stock}")
    
    # Display current portfolio
    if st.session_state.portfolio:
        st.subheader("Current Portfolio")
        
        # Calculate portfolio value
        total_value, portfolio_details = calculate_portfolio_value(st.session_state.portfolio)
        
        # Display portfolio table
        for item in portfolio_details:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"**{item['stock']}**")
            with col2:
                st.write(f"{item['quantity']} shares")
            with col3:
                st.write(f"${item['price']:.2f}/share")
            with col4:
                st.write(f"**${item['total_value']:.2f}**")
        
        # Total value
        st.write("---")
        st.write(f"## Total Portfolio Value: ${total_value:.2f}")
        
        # File saving options
        st.subheader("Save Portfolio")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Save as TXT"):
                if save_portfolio_txt(portfolio_details, total_value):
                    st.success("Portfolio saved to portfolio.txt")
        
        with col2:
            if st.button("Save as CSV"):
                if save_portfolio_csv(portfolio_details, total_value):
                    st.success("Portfolio saved to portfolio.csv")
        
        with col3:
            if st.button("Clear Portfolio"):
                st.session_state.portfolio = {}
                st.success("Portfolio cleared!")
                st.rerun()
    
    else:
        st.info("No stocks in portfolio yet. Add some stocks above!")
    
    # Sidebar with information
    st.sidebar.title("Key Concepts Used")
    st.sidebar.write("""
    **Dictionary:** Stock prices stored in STOCK_PRICES dictionary
    
    **Input/Output:** User inputs stock selection and quantities
    
    **Basic Arithmetic:** Calculating total values (price × quantity)
    
    **File Handling:** Save results to .txt or .csv files
    """)
    
    # Demo button
    if st.sidebar.button("Run Console Demo"):
        st.sidebar.write("Check your terminal for console demo!")
        # Note: Console demo won't work in Streamlit cloud, only locally

# Example function showing dictionary usage
def demonstrate_concepts():
    """
    Function to demonstrate key programming concepts
    """
    print("=== DEMONSTRATING KEY CONCEPTS ===\n")
    
    # 1. Dictionary usage
    print("1. DICTIONARY USAGE:")
    print("Stock prices dictionary:", STOCK_PRICES)
    print(f"AAPL price: ${STOCK_PRICES['AAPL']}")
    print()
    
    # 2. Basic arithmetic
    print("2. BASIC ARITHMETIC:")
    shares = 10
    price = STOCK_PRICES['AAPL']
    total = shares * price
    print(f"{shares} shares × ${price} = ${total}")
    print()
    
    # 3. Input/Output (simulated)
    print("3. INPUT/OUTPUT SIMULATION:")
    sample_portfolio = {"AAPL": 10, "TSLA": 5}
    print(f"Sample input portfolio: {sample_portfolio}")
    
    total_value, details = calculate_portfolio_value(sample_portfolio)
    print(f"Calculated total value: ${total_value:.2f}")
    print()
    
    # 4. File handling demonstration
    print("4. FILE HANDLING:")
    print("Saving sample portfolio to files...")
    save_portfolio_txt(details, total_value, "demo_portfolio.txt")
    save_portfolio_csv(details, total_value, "demo_portfolio.csv")
    print("Files saved successfully!")

# Run the application
if __name__ == "__main__":
    main()
    
    # Uncomment to run concept demonstration
    # demonstrate_concepts()
    
    # Uncomment to run console version
    # console_portfolio_tracker()