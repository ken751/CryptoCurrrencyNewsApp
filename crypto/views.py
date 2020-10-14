from django.shortcuts import render


def home(request):
	import requests 
	import json
	key = '890ea83ba7c3cc1f6756b675e5c711e0a8c9292b06bb3153844fb2a0ded7c70e' 
	

	#Grab Crypto Price Data
	price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD&api_key={key}')
	price = json.loads(price_request.content)

	#Grab Crypto News
	api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={key}')
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
	if request.method == 'POST':
		import requests 
		import json 
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html',{'quote':quote, 'crypto': crypto})

	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html',{'notfound': notfound})
