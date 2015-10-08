package velogista.routing.api.route;

/**
 * Route parameters adjust the behavior of a routing algorithm.
 * 
 * @author falk
 * 
 */
public interface RouteParameters {

	/**
	 * Returns the route type
	 * 
	 * @return FASTEST, SHORTEST, BICYCLE or PEDESTRIAN
	 */
	public RouteType getRouteType();

	/**
	 * Returns the generalization value for generating line shapes of the resulting route.
	 * 
	 * If this parameter is 0, then no shape simplification will be done and all shape points will be returned.
	 * 
	 * If the generalize parameter is > 0, it will be used as the tolerance distance (in meters) in the Douglas-Peucker
	 * Algorithm for line simplification.
	 */
	public int getLineGeneralization();
}
