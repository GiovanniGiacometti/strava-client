from datetime import datetime
from typing import Literal
from strava_client.enums.api import StravaSportType
from strava_client.models.base import StravaBaseModel


# Information about the Strava API can be found here:
# https://developers.strava.com/docs/reference/


class MetaAthlete(StravaBaseModel):
    """
    Strava athlete model, containing only the ID.
    """

    id: int


class StravaActivity(StravaBaseModel):
    """
    Model holding information about a Strava activity.
    In Strava it's actually called "SummaryActivity"
    (https://developers.strava.com/docs/reference/#api-models-SummaryActivity)
    """

    id: int
    external_id: str | None = None
    name: str  # The name of the activity
    athlete: MetaAthlete
    distance: float
    moving_time: int  # in seconds
    elapsed_time: int  # in seconds
    total_elevation_gain: float
    elev_high: float | None = None  # sometimes missing
    elev_low: float | None = None  # sometimes missing
    sport_type: StravaSportType
    start_date: datetime
    start_date_local: datetime
    timezone: str
    average_speed: float
    max_speed: float
    start_latlng: list[float]
    end_latlng: list[float]


class StravaBaseStream(StravaBaseModel):
    """
    Base class for Strava activity streams.
    In Strava it's actually called "StreamSet"
    (https://developers.strava.com/docs/reference/#api-models-StreamSet)
    """

    original_size: int  # Number of points in the stream
    resolution: Literal[
        "high", "medium", "low"
    ]  # The level of detail (sampling) in which this stream was sampled
    series_type: Literal[
        "distance", "time"
    ]  # The base series used in the case the stream was downsampled
    data: list[int | float]  # The data of the stream


class StravaActivityStream(StravaBaseModel):
    """
    Model holding information about a Strava activity stream set.
    In Strava it's actually called "SummaryActivity"
    (https://developers.strava.com/docs/reference/#api-models-SummaryActivity)
    """

    time: StravaBaseStream | None = None
    latlng: StravaBaseStream | None = None
    distance: StravaBaseStream | None = None
    altitude: StravaBaseStream | None = None
    velocity_smooth: StravaBaseStream | None = None
    heartrate: StravaBaseStream | None = None
    cadence: StravaBaseStream | None = None
    watts: StravaBaseStream | None = None
    temp: StravaBaseStream | None = None
    moving: StravaBaseStream | None = None
    grade_smooth: StravaBaseStream | None = None
