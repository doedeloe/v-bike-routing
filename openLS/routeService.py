#!/usr/bin/python
from openLSmisc import *

REQUEST_ROUTE_START = "<xls:Request methodName=\"RouteRequest\" version=\"1.1\" requestID=\"00\" maximumResponses=\"15\">		<xls:DetermineRouteRequest>			<xls:RoutePlan>				<xls:RoutePreference>Fastest</xls:RoutePreference>				<xls:ExtendedRoutePreference>					<xls:WeightingMethod>Fastest</xls:WeightingMethod>				</xls:ExtendedRoutePreference>				<xls:WayPointList>"
REQUEST_ROUTE_STOP = "</xls:WayPointList>				<xls:AvoidList />			</xls:RoutePlan>			<xls:RouteInstructionsRequest provideGeometry=\"true\" />			<xls:RouteGeometryRequest>			</xls:RouteGeometryRequest>		</xls:DetermineRouteRequest>	</xls:Request>"

URL_OPENLS_ROUTE_SERVICE = "http://openls.geog.uni-heidelberg.de/testing2015/routing"

def generateRoutingRequest(startPoint,endPoint,waypoints):
    requestHeader = getDefaultRequestHeader()
    requestBody = generateRouteRequestBody(startPoint,endPoint,waypoints)
    return wrapXLSAroundRequest("{0} {1}".format(requestHeader,requestBody))

def generateRouteRequestBody(startPoint,endPoint,waypoints):
    start = "<xls:StartPoint><xls:Position>{0}</xls:Position></xls:StartPoint>".format(extractPoint(startPoint))
    viapoints = ""
    for waypoint in waypoints:
        viapoints = "{0} <xls:ViaPoint><xls:Position>{1}</xls:Position></xls:ViaPoint>".format(viapoints,extractPoint(waypoint))
    stop = "<xls:EndPoint><xls:Position>{0}</xls:Position></xls:EndPoint>".format(extractPoint(endPoint))
    waypointlist = "{0} {1} {2}".format(start,viapoints,stop)
    return "{0} {1} {2}".format(REQUEST_ROUTE_START,waypointlist,REQUEST_ROUTE_STOP)

def extractPoint(point):
    position = point.find('{http://www.opengis.net/gml}pos')
    return "{0} {1} {2}".format("<gml:Point><gml:pos srsName=\"EPSG:4326\">", position.text, "</gml:pos></gml:Point>")

def sendORSRoutingRequest(request):
    global URL_OPENLS_ROUTE_SERVICE
    return sendRequestsToURL(request,URL_OPENLS_ROUTE_SERVICE)


    
    
