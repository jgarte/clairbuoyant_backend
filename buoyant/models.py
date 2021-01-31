from django.contrib.gis.db import models


class Buoy(models.Model):
    station_id = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    location = models.PointField(spatial_index=True, geography=True)
    elev = models.DecimalField("elevation", max_digits=9, decimal_places=6, null=True)
    pgm = models.CharField(max_length=50)
    buoy_type = models.CharField(max_length=10)
    met = models.CharField(max_length=1, default="n")
    currents = models.CharField(max_length=1, default="n")
    waterquality = models.CharField(max_length=1, default="n")
    dart = models.CharField(max_length=1, default="n")
    seq = models.PositiveSmallIntegerField("seq attribute", null=True)

    def __str__(self):
        return f"Buoy({self.station_id}:{self.name},location:{self.location})"


class Meteorological(models.Model):
    observation_date = models.DateTimeField()
    wind_dir = models.PositiveSmallIntegerField(null=True)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    wind_gust = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    wave_height = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    dom_wave_period = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    avg_wave_period = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    wave_dir = models.PositiveSmallIntegerField(null=True)
    sea_pressure = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    air_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sea_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    tide = models.CharField(max_length=6)
    dewpoint_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    station_visibility = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    pressure_tendency = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    buoy = models.ForeignKey(Buoy, on_delete=models.CASCADE)

    def __str__(self):
        return f"Meteorological({self.observation_date})"


# class Current(models.Model): ...
# 'bin',  # (count)
# 'depth',  # (m)
# 'direction_of_sea_water_velocity',  # (degree)
# 'sea_water_speed',  # (c/s)
# 'upward_sea_water_velocity',  # (c/s)
# 'error_velocity',  # (c/s)
# 'platform_orientation',  # (degree)
# 'platform_pitch_angle',  # (degree)
# 'platform_roll_angle',  # (degree)
# 'sea_water_temperature',  # (C)
# 'pct_good_3_beam',  # (%)
# 'pct_good_4_beam',  # (%)
# 'pct_rejected',  # (%)
# 'pct_bad',  # (%)
# 'echo_intensity_beam1',  # (count)
# 'echo_intensity_beam2',  # (count)
# 'echo_intensity_beam3',  # (count)
# 'echo_intensity_beam4',  # (count)
# 'correlation_magnitude_beam1',  # (count)
# 'correlation_magnitude_beam2',  # (count)
# 'correlation_magnitude_beam3',  # (count)
# 'correlation_magnitude_beam4',  # (count)
# 'quality_flags',


# class Wave(models.Model): ...
# "sea_surface_wave_significant_height",  # (m)
# "sea_surface_wave_peak_period",  # (s)
# "sea_surface_wave_mean_period",  # (s)
# "sea_surface_swell_wave_significant_height",  # (m)
# "sea_surface_swell_wave_period",  # (s)
# "sea_surface_wind_wave_significant_height",  # (m)
# "sea_surface_wind_wave_period",  # (s)
# "sea_water_temperature",  # (c)
# "sea_surface_wave_to_direction",  # (degree)
# "sea_surface_swell_wave_to_direction",  # (degree)
# "sea_surface_wind_wave_to_direction",  # (degree)
# "number_of_frequencies",  # (count)
# "center_frequencies",  # (Hz)
# "bandwidths",  # (Hz)
# "spectral_energy",  # (m**2/Hz)
# "mean_wave_direction",  # (degree)
# "principal_wave_direction",  # (degree)
# "polar_coordinate_r1",  # (1)
# "polar_coordinate_r2",  # (1)
# "calculation_method",
# "sampling_rate",  # (Hz)


# class Wind(models.Model): ...
