package velogista.routing.api.location;

public interface PostalAddress {

	/**
	 * Gibt den Namen der Person/Firma dieser Adresse zurück
	 * 
	 * @return Name der Person/Firma
	 */
	public String getName();

	/**
	 * Gibt Straße und Hausnummer dieser Adresse zurück
	 * 
	 * @return Straße und Hausnummer
	 */
	public String getStreet();

	/**
	 * Gibt Postleitzahl und Stadt dieser Adresse zurück
	 * 
	 * @return Postleitzahl und Stadt
	 */
	public String getCity();
}
