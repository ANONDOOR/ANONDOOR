import urllib3
import json
import requests

def iptracker(ip):

	url = 'http://ipinfo.io/{0}/json'.format(ip)

	http = urllib3.PoolManager()

	response =  http.request('GET', url)
	data = requests.get(url).json()

	IP=data['ip']
	org=data['org']
	city = data['city']
	country=data['country']
	region=data['region']

	print('Detalles de IP\n ')
	print('IP : {4} \nRegion : {1} \nPais : {2} \nCiudad : {3} \nISP : {0}'.format(org,region,country,city,IP))
	print("se ha guarado en: UbicacionesIP.txt")
	w = open("UbicacionesIP.txt","a+")
	w.write(str('\nIP : {4} \nRegion : {1} \nPais : {2} \nCiudad : {3} \nISP : {0}\n'.format(org,region,country,city,IP)))




