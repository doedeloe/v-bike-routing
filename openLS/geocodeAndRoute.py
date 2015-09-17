#!/usr/bin/python

from geocoding import *
from routeService import *
from openLSmisc import *

from geocodeDummyResponses import RESPONSES

import xml.etree.ElementTree as ET

ns = {'xlss': "http://www.opengis.net/xls"}

def main():
    adresses = readAdressesFromInputFiles()
    requests = geocodeRequestsFromAdresses(adresses)
    geocodeResponses = sendORSGeocodeRequest(requests)
    geocodeFile = open('geocode.txt','w')
    for response in geocodeResponses:
        geocodeFile.write(response)
    geocodeFile.close()
    #geocodeResponses= RESPONSES
    if len(geocodeResponses) > 1:
        startPoints = geocodeResponses.pop(0)
        print startPoints
        stopPoints = geocodeResponses.pop()
        startPoint = extractFirstEntry(startPoints)
        stopPoint = extractFirstEntry(stopPoints)
        waypoints = []
        for adress in geocodeResponses:
            waypoint = extractFirstEntry(adress)
            waypoints.append(waypoint)
        request = generateRoutingRequest(startPoint,stopPoint,waypoints)
        requestFile = open("routingRequest.txt",'w')
        requestFile.write(request)
        requestFile.close()
        route = sendORSRoutingRequest(request)
        routeFile = open('route.txt','w')
        routeFile.write(route)
        routeFile.close()

def extractFirstEntry(response):
    global ns
    point = None
    root = ET.fromstring(response)
    responseList = findElementInNode(root,'{http://www.opengis.net/xls}GeocodeResponseList')
    print responseList.attrib
    numberOfResponses = int(responseList.attrib['numberOfGeocodedAddresses'])
    if numberOfResponses > 0:
        firstEntry = responseList.find('{http://www.opengis.net/xls}GeocodedAddress')
        point = firstEntry.find('{http://www.opengis.net/gml}Point')
    return point

def findElementInNode(node,element):
    for child in node:
        foundElement = child.find(element)
        if foundElement is not None:
            return foundElement
        else:
            if len(child) > 0:
                foundElement = findElementInNode(child,element)
                if foundElement is not None:
                    return foundElement
    return None

if __name__ == '__main__':
    main()

