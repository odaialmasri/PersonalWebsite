def create_dicit():
	country_capital={
	"palestine":"Jerusalem",
	"Egypt":"kahera",
	"USA":"DC",
	"Germany":"Berlin"
	}

	return country_capital

def print_output(dectionary,country):
	print("the capital of"+country+"is"+dectionary(country))

def main():
	dectionary=create_dicit()
	country = input("Enter Your The country,enter to quite:")

	while (country != ""):

		if country in dectionary :
			print_output(dectionary,country)
		else:

			print("Try agine")
		country1 =input("Enter Your The country,enter to quite:")



	# if key in dectionary():
	# 	print_output(dectionary,key)

		


if __name__ == "__main__":
	main()