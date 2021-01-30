"""NDBC Scraper Service."""
import datetime
import requests
import pytz
from bs4 import BeautifulSoup as bs
from buoyant.models import Buoy
from django.contrib.gis.geos import Point


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
    REALTIME_URL = "https://www.ndbc.noaa.gov/data/realtime2/"
    # OBS_ENDPOINT = "https://sdf.ndbc.noaa.gov/sos/server.php"

    def get_activestations():
        """Extract NDBC's activestations from `activestations.xml` endpoint."""
        xml_data = requests.get(ACTIVESTATIONS_XML).content

        soup = bs(xml_data, "xml")

        return soup.find_all("station")

    def parse_activestations(stations):
        parsed_stations_obj = []
        for station in stations:
            station = station.attrs
            lon, lat = float(station.get("lon", 0.0)), float(station.get("lat", 0.0))
            geo = Point(lon, lat)
            #! DevNote - emptyString handling is not Null in psql.
            parsed_stations_obj.append(
                Buoy(
                    location=geo,
                    station_id=station.get("id"),
                    name=station.get("name"),
                    owner=station.get("owner"),
                    elev=station.get("elev"),
                    pgm=station.get("pgm"),
                    buoy_type=station.get("type"),
                    met=station.get("met", ""),
                    currents=station.get("currents", ""),
                    waterquality=station.get("waterquality", ""),
                    dart=station.get("dart", ""),
                    seq=station.get("seq"),
                )
            )
        return parsed_stations_obj

    def persist_parsed(stations):
        Buoy.objects.bulk_create(stations)

    def get_realtime_meteorological_data(station):
        realtime_url = REALTIME_URL + f"{station.station_id}.txt"

        station_content = requests.get(realtime_url).text
        soup = bs(station_content, "lxml")
        table = soup.find("p")
        table_output = table.get_text()

        for line in table_output.splitlines()[2:]:
            line_list = (" ".join(line.split())).split(" ")
            observation_date = [int(datedata) for datedata in line_list[0:5]]
            observation_date = datetime.datetime(*observation_date, tzinfo=pytz.UTC)

            clean_line_list = [v if v != "MM" else None for v in line_list[5:]]
            record = {
                "observation_date": observation_date,
                "wind_dir": clean_line_list[0],
                "wind_speed": clean_line_list[1],
                "wind_gust": clean_line_list[2],
                "wave_height": clean_line_list[3],
                "dom_wave_period": clean_line_list[4],
                "avg_wave_period": clean_line_list[5],
                "wave_dir": clean_line_list[6],
                "sea_pressure": clean_line_list[7],
                "air_temp": clean_line_list[8],
                "sea_temp": clean_line_list[9],
                "dewpoint_temp": clean_line_list[10],
                "station_visibility": clean_line_list[11],
                "pressure_tendency": clean_line_list[12] or "MM",
                "tide": clean_line_list[13] or "MM",
            }
            station.meteorological_set.create(**record)

    def fetch_data(station_id, data):
        ...
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

    def seed_buoy_data():
        stations = parse_activestations(get_activestations())
        persist_parsed(stations)

    """
    # TODO - Redesign scraper functionality to seperate concerns (i.e., CRUD).
        ?# Additional Consideration: class vs fn, and scraper location?
        - Initial Seeding tasks:
            # Seed buoys table with Buoy information.
        - Updating:
            # Check buoy for updated attributes to signal whether further
                action is necessary; do not override data - only update particular cells.
        - Observations:
            # Create new observational records, which are dervived from a buoy.
    """

    def seed_meteorological_data():
        # for buoy in Buoy.objects.all():
        # get_realtime_meteorological_data(buoy)
        get_realtime_meteorological_data(Buoy.objects.get(station_id=44065))

    # seed_buoy_data()
    seed_meteorological_data()


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
