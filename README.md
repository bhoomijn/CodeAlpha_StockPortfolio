Enter quantity of AAPL: 4
Enter stock symbol (or 'done' to finish): done

Your Portfolio:
AAPL: 4 shares → $720

Total Portfolio Value: $720
Traceback (most recent call last):
  File "c:\Users\bhoom\OneDrive\New folder\python.py", line 40, in <module>
    f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
  File "C:\Users\bhoom\AppData\Local\Programs\Python\Python312\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 15: character maps to <undefined>
PS C:\Users\bhoom\OneDrive\New folder> 

2. Navigate to the folder:

cd CodeAlpha_StockPortfolio

3. Run the program:

python stock_tracker.py


🎯 Example Input/Output

Welcome to Stock Portfolio Tracker!
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 4
Enter stock symbol (or 'done' to finish): done

Your Portfolio:
AAPL: 4 shares --> $720

Total Portfolio Value: $720

Portfolio saved to portfolio.txt ✅
