#!/usr/bin/python
from openLSmisc import *

REQUEST_GEOCODE_START_FREE_FORM_ADDRESS = "	<xls:Request methodName=\"GeocodeRequest\" requestID=\"123456789\" version=\"1.1\"><xls:GeocodeRequest><xls:Address countryCode=\"DE\">	<xls:freeFormAddress>"
REQUEST_GEOCODE_STOP_FREE_FORM_ADDRESS = "</xls:freeFormAddress></xls:Address></xls:GeocodeRequest>	</xls:Request>"

URL_OPENLS_GEOCODING_SERVICE = "http://openls.geog.uni-heidelberg.de/testing2015/geocoding"

def main():
    adresses = readAdressesFromInputFiles()
    requests = geocodeRequestsFromAdresses(adresses)
    geocodedAdresses = sendORSGeocodeRequest(requests)    
    #writeRequestsToFiles(requests)

def geocodeRequestsFromAdresses(adresses):
    requests = []
    for adress in adresses:
        request = generateGeocodeRequestFromAdress(adress)
        requests.append(request)
    return requests

def wrapGeocodeFreeFormAdressAroundAdress(adress):
    global REQUEST_GEOCODE_START_FREE_FORM_ADDRESS
    global REQUEST_GEOCODE_STOP_FREE_FORM_ADDRESS 
    freeFormRequestBody = "{0} {1} {2}".format(REQUEST_GEOCODE_START_FREE_FORM_ADDRESS,adress,REQUEST_GEOCODE_STOP_FREE_FORM_ADDRESS)
    return freeFormRequestBody

def generateGeocodeRequestFromAdress(adress):
    freeFormRequestHeader = "<xls:RequestHeader/>"
    freeFormRequestBody = wrapGeocodeFreeFormAdressAroundAdress(adress)
    return wrapXLSAroundRequest("{0} {1}".format(freeFormRequestHeader,freeFormRequestBody))

def sendORSGeocodeRequest(requests):
    global URL_OPENLS_GEOCODING_SERVICE
    return sendRequestsToURL(requests,URL_OPENLS_GEOCODING_SERVICE)

def writeRequestsToFiles(requests):
    i = 0
    for request in requests:
        outfile = open("geocode_request_{0}".format(i), 'w')
        outfile.write(request)
        i = i+1
        outfile.close()

def splitLineToPieces(line,seperators):
    pass
    
if __name__ == '__main__':
    main()

