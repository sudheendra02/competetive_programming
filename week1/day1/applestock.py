def max_profit(stock_value):
	max_diff=stock_value[1]-stock_value[0]
	min=stock_value[0]
	for i in stock_value:
		if(i < 0):
			return "stock value cannot be negative"
	for i in stock_value[1:len(stock_value)]:
		diff = i - min
		if (diff>max_diff):
			max_diff=diff
		if i<min:
			min=i
	return max_diff


			

if __name__ == '__main__':
	stock_value=[-1]
	if(len(stock_value)<2):
		print("there should be atleast 2 values")
	else:
		print(max_profit(stock_value))