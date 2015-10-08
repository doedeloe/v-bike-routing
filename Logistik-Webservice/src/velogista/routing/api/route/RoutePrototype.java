package velogista.routing.api.route;

import java.util.List;

import velogista.routing.api.location.Location;

/**
 * Classes of this interface represent a blueprint for a route optimization.
 * 
 * Instances contain all information that is need to perform routing and create an OptimizedRoute.
 * 
 * This information consists of: - start- and end-locations of the route - intermediate stops to be sorted by following
 * the Travelling Salesman - parameters to adjust the routing algorithm (like fastest/shortest route)
 */
public interface RoutePrototype extends OptimizedRoute {

	/**
	 * Returns the start location of the route to optimize. An OptimizedRoute based on this prototype should always
	 * return this location as its first stop.
	 * 
	 * @return Start location
	 */
	public Location getStart();

	/**
	 * Returns the end location of the route to optimize. An OptimizedRoute based on this prototype should always return
	 * this location as its last stop.
	 * 
	 * @return End location
	 */
	public Location getEnd();

	/**
	 * Returns the intermediate stops to optimize. An OptimizedRoute will contain these locations reordered by the
	 * routing algorithm.
	 * 
	 * @return Intermediate stop
	 */
	public List<Location> getStops();

	/**
	 * Returns parameters that adjust the routing algorithm
	 * 
	 * @return Route parameters
	 */
	public RouteParameters getParameters();
}
