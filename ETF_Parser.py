etf_inFile = open("Schwab_ETF.txt", 'r')
ticker_outFile = open("Schwab_ETF_tickers.txt", 'w')

for line in etf_inFile:
	ticker = (etf_inFile.readline()[0:4])
	ticker = ticker.strip()
	ticker_outFile.write(ticker)
	ticker_outFile.write(", ")