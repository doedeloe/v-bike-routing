#!/usr/bin/python
import fileinput 
import urllib

XML_HEADER = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
XLS_OPEN = "<xls:XLS xmlns:xls=\"http://www.opengis.net/xls\" xmlns:sch=\"http://www.ascc.net/xml/schematron\" xmlns:gml=\"http://www.opengis.net/gml\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.opengis.net/xls http://schemas.opengis.net/ols/1.1.0/LocationUtilityService.xsd\" version=\"1.1\">"
XLS_CLOSE = "</xls:XLS>"
REQUEST_HEADER_OPEN = "<xls:RequestHeader>"
REQUEST_HEADER_CLOSE = "</xls:RequestHeader>"

def wrapXLSAroundRequest(request):
    global XLS_OPEN
    global XLS_CLOSE
    return "{0} {1} {2} {3}".format(XML_HEADER,XLS_OPEN,request,XLS_CLOSE)

def getDefaultRequestHeader():
    global REQUEST_HEADER_OPEN
    global REQUEST_HEADER_CLOSE
    return "{0} {1}".format(REQUEST_HEADER_OPEN,REQUEST_HEADER_CLOSE)

def sendRequestsToURL(requests,url):
    answers = []
    for request in requests:
        postData = { "REQUEST" : request }
        filehandle = urllib.urlopen(url,urllib.urlencode(postData))
        answer = filehandle.read()
        answers.append(answer)
    return answers

def sendRequestToURL(request,url):
    postData = { "REQUEST" : request }
    filehandle = urllib.urlopen(url,urllib.urlencode(postData))
    answer = filehandle.read()
    return answer

def readAdressesFromInputFiles():
    adresses = []
    for line in fileinput.input():
        if mightBeAdress(line):
            adresses.append(line)
    return adresses


def mightBeAdress(line):
    return True
