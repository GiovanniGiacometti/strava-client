from strava_client.client import StravaClient
from strava_client.enums.auth import StravaScope


if __name__ == "__main__":
    client = StravaClient(
        scopes=[
            StravaScope.READ,
            StravaScope.ACTIVITY_READ,
            StravaScope.ACTIVITY_READ_ALL,
        ]
    )

    res = client.get_activity_stream(
        id="13486661060",
        keys=[
            "velocity_smooth",
        ],
    )
