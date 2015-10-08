package velogista.routing.api.location;

import java.util.List;

public interface LocationManager {

	/**
	 * Tries to complete the address- and coordinates-information in the supplied location.
	 * 
	 * If the location has no coordinates, geoocoding is performed. If there is no address, reverse geocoding is
	 * performed. If both address and coordinates are NULL, an IllegalArgumentException is thrown. If both are set, the
	 * method just returns a list with the given location as its only entry.
	 * 
	 * @param location
	 *            Location with either address or coordinates to find
	 * @return A list of candidates matching the given information
	 */
	public List<Location> find(Location location);

	/**
	 * Tries to find candidates of geographic locations that match the given postal address.
	 * 
	 * @param address
	 *            Postal address to find matching geographics locations for
	 * @return A list of candidates matching the given postal address
	 */
	public List<Location> geocode(PostalAddress address);

	/**
	 * Tries to find candidates of geographic locations that match the given postal address.
	 * 
	 * @param address
	 *            Postal address to find matching geographics locations for
	 * @return A list of candidates matching the given coordinates
	 */
	public List<Location> reverseGeocode(GeoCoordinates coordinates);

}
