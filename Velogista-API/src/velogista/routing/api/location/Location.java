package velogista.routing.api.location;

/**
 * Classes of this interface represent named locations in the physical world.
 * 
 * The name of the location should always be set and unique over all instances of the class.
 * 
 * Postal address and geo-coordinates are optional and can be NULL if the information is not present yet.
 * 
 * @author falk
 */
public interface Location {

	/**
	 * Returns the name of this location
	 * 
	 * @return Name of this location. May NOT be NULL!
	 */
	public String getName();

	/**
	 * Return the postal address of this location. Can be NULL if postal address is unknown.
	 * 
	 * @return Postal address of this location or NULL.
	 */
	public PostalAddress getPostalAddress();

	/**
	 * Returns geographic coordinates for this location. Can be NULL if coordinates are unknown.
	 * 
	 * @return Geo-coordinates for this location or NULL.
	 */
	public GeoCoordinates getGeoCoordinates();
}
