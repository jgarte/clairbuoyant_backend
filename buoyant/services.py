"""NDBC Scraper Service."""
# ? considering this namespace for scraping logic instead of model/view/admin
import requests
from bs4 import BeautifulSoup as bs


def NDBCScraper():
    """NDBC Scraper.

    Request Parameters for Observations.
        request = GetObservation
        service = SOS
        version = 1.0.0
        offering = urn:ioos:station:wmo::<station ID> for single station,
            or urn:ioos:network:noaa.nws.ndbc:all for use with collections.
        observedproperty = one of the following:
            air_pressure_at_sea_level
            air_temperature
            currents
            sea_floor_depth_below_sea_surface (water level for tsunami stations)
            sea_water_electrical_conductivity
            sea_water_salinity
            sea_water_temperature
            waves
        responseformat=text/csv
    """
    ACTIVESTATIONS_XML = "https://www.ndbc.noaa.gov/activestations.xml"
    # OBS_ENDPOINT = "https://sdf.ndbc.noaa.gov/sos/server.php"

    def get_station_xml():
        xml_data = requests.get(ACTIVESTATIONS_XML).content

        soup = bs(xml_data, "xml")
        stations = soup.find_all('station')
        print(len(stations))  # => 1439

        # Buoy.create!(
        # station_code: station[:id],
        # station_name: station[:name],
        # station_owner: station[:owner],
        # latitude: station[:lat], longitude: station[:lon],
        # pgm: station[:pgm], type: station[:type],
        # elev: station[:elev],
        # met: station[:met],
        # dart: station[:dart],
        # currents: station[:currents],
        # waterquality: station[:waterquality])

    def realtime_meteorological_data(station_id):
        pass
        # station_code string should be capitalized in url
        # capitalized_station_id = station_id.upcase
        # realtime_url = "https://www.ndbc.noaa.gov/data/realtime2/#{capitalized_station_id}.txt"
        # begin
        #     content = URI.open(realtime_url).read
        #     arr = []
        #     content.each_line { |row| arr.push(row)}
        #     self.fetch_data(station_id, arr)
        # rescue
        #     puts "404"
        #     nil

    def parse_realtime_meteorological_data(data):
        pass
        # data.map { |row| row.split(" ") }#.transpose

    def fetch_data(station_id, data):
        pass
        # buoy = Buoy.find_by(station_code: station_id)
        # data_arr_table = self.parse_realtime_meteorological_data(data)
        # data_arr_table.shift(2)
        # data_arr_table.each_with_index do | row, row_idx |
        #     puts "#{row}  #{row_idx}"
        #     # requires refactoring column names to correspond to incoming data
        #     # row.each_with_index do | datum, data_idx |
        #     time_s = row[0] + '-' + row[1] + '-' + row[2] + ' ' + row[3] + ':' + row[4]
        #     record = buoy.meteorological_data.build(
        #         recorded_data_at: DateTime.parse(time_s),
        #         wind_dir: row[5].to_i,
        #         wind_speed:row[6].to_f,
        #         wind_gust: row[7].to_f,
        #         wave_height: row[8].to_f,
        #         dom_wave_period: row[9].to_i,
        #         avg_wave_period: row[10].to_f,
        #         wave_dir: row[11].to_i,
        #         sea_pressure: row[12].to_f,
        #         air_temp: row[13].to_f,
        #         sea_temp: row[14].to_f,
        #         dewpoint_temp: row[15],
        #         station_visibility: row[16].to_f,
        #         pressure_tency: row[17],
        #         tide: row[18],
        #     )

    def run():
        get_station_xml()
        # Buoy.all.each do |buoy_obj|
        #     self.realtime_meteorological_data(buoy_obj.station_code)

    run()


"""NOTE: XML Data
<ows:Keywords>
    <ows:Keyword>Weather</ows:Keyword>
    <ows:Keyword>National Data Buoy Center</ows:Keyword>
    <ows:Keyword>NDBC</ows:Keyword>
    <ows:Keyword>Moored Buoy</ows:Keyword>
    <ows:Keyword>C-MAN</ows:Keyword>
    <ows:Keyword>DART</ows:Keyword>
    <ows:Keyword>TAO</ows:Keyword>
    <ows:Keyword>Air Temperature</ows:Keyword>
    <ows:Keyword>Barometric Pressure</ows:Keyword>
    <ows:Keyword>Conductivity</ows:Keyword>
    <ows:Keyword>Ocean Currents</ows:Keyword>
    <ows:Keyword>Salinity</ows:Keyword>
    <ows:Keyword>Water Level</ows:Keyword>
    <ows:Keyword>Water Temperature</ows:Keyword>
    <ows:Keyword>Waves</ows:Keyword>
    <ows:Keyword>Winds</ows:Keyword>
</ows:Keywords>

"""

"""NOTE:
 Update attributes if the below is checked 'y' / or other.
 - met: indicates whether the station has reported meteorological data in the
   past eight hours (y/n).
 - currents: indicates whether the station has reported water current data in
   the past eight hours (y/n).
 - waterquality: indicates whether the station has reported ocean chemistry
   data in the past eight hours (y/n).
 - dart: indicates whether the station has reported water column height/tsunami
   data in the past 24 hours (y/n).
"""

NDBCScraper()
