package velogista.routing.api.route;

import java.util.List;

import velogista.routing.api.location.GeoCoordinates;
import velogista.routing.api.location.Location;

/**
 * An optimized route is the result of a routing process.
 * 
 * Based on the supplied RoutePrototype to this process, this optimized route contains stops sorted by solving the
 * Traveling Salesman Problem, a list of 'legs' which contain the instructions between stops and a list of geographic
 * coordinates that describe a line shape along the route.
 * 
 * @author falk
 * 
 */
public interface OptimizedRoute {

	/**
	 * Returns a list of sorted locations. The first and list locations are the start- and endpoints from the
	 * RoutePrototype this route was created from. The intermediate stops are sorted by solving the Traveling Salesman
	 * Problem.
	 * 
	 * @return List of sorted input locations
	 */
	public List<Location> getLocations();

	/**
	 * Returns a list of indices that describes the reordered input locations supplied in the RoutePrototype to this
	 * route. The first index is always 0 and the last is always the length of the supplied list of locations -1. The
	 * indices between are sorted by solving the Traveling Salesman Problem.
	 * 
	 * @return List of input indices sorted according to getLocations()
	 */
	public int[] getLocationIndices();

	/**
	 * Returns a list of legs that connect the locations of this route. This list is sorted matching the order of
	 * getLocations() and getLocationIndices() and always contains one entry less than these lists (because no leg
	 * leaves the endpoint of a route).
	 * 
	 * @return List of legs connecting the sorted locations
	 */
	public List<Leg> getLegs();

	/**
	 * Returns a list of geographic coordinates that approximate a line shape following this route. It can be used to
	 * render a line on a map representing this route. How detailed this line is (hence how long this list is, depends
	 * on the supplied generalization value int the RoutePrototype to this route.
	 * 
	 * @return List of coordinates that describe a line shape along the route
	 */
	public List<GeoCoordinates> getLineShape();
}
