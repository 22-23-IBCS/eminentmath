class CurrencyConverter:
    def __init__(self):
        self.countries = ['USA', 'India', 'Japan', 'UK', 'China', 'Australia']
        self.conversion_rates = {
            'usa': 1.0,
            'india': 0.013,
            'japan': 0.0093,
            'uk': 1.29,
            'china': 0.15,
            'australia': 0.72
        }
        self.currencies = {
            'usa': 'USD',
            'india': 'INR',
            'japan': 'JPY',
            'uk': 'GBP',
            'china': 'CNY',
            'australia': 'AUD'
        }

    def get_countries(self):
        return self.countries

    def get_conversion_rate(self, country):
        return self.conversion_rates[country]

    def convert(self, amount, from_country, to_country):
        initial_amount = amount
        #print(self.conversion_rates[from_country])
        #print(self.conversion_rates[to_country])
        amount = amount / self.conversion_rates[from_country]
        amount = amount * self.conversion_rates[to_country]
        return amount

    def print_conversion(self, amount, from_country, to_country):
        converted_amount = self.convert(amount, from_country, to_country)
        from_currency = self.currencies[from_country]
        to_currency = self.currencies[to_country]
        print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')


def main():

    cc = CurrencyConverter()
    
    while True:
        
        print('Available countries to convert to:', cc.get_countries())
        from_country = input('Enter the country to convert from: ')
        if from_country.lower() in ['quit', 'exit']:
            break
        to_country = input('Enter the country to convert to: ')
        if to_country.lower() in ['quit', 'exit']:
            break
        amount = float(input('Enter the amount to convert: '))
        cc.print_conversion(amount, from_country.lower(), to_country.lower())

if __name__=="__main__":
    main()



