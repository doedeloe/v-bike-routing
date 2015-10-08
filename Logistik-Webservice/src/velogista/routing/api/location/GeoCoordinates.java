package velogista.routing.api.location;

public interface GeoCoordinates {

	/**
	 * Gibt den Breitengrad als Fließkommazahl zurück
	 * 
	 * @return Breitengrad zwischen -90° und 90°
	 */
	public double getLatitude();

	/**
	 * Gibt den Längengrad als Fließkommazahl zurück
	 * 
	 * @return Längengrad zwischen -180° und 180°
	 */
	public double getLongitude();
}
