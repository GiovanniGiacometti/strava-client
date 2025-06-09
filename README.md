# Strava Client 🏃🚴‍♂️

A lightweight, hackable Python wrapper for the Strava API that simplifies authentication and data access. Perfect for developers who want to build custom Strava applications without the complexity of full-featured clients.

## 🚀 Getting started

The project is published on PyPI and can be installed using pip:

```bash
pip install strava-client
```

or using `uv`:

```bash
uv add strava-client
```

## 🏗️ Usage

The library is designed to be simple and easy to use. However, a few steps are needed to set it up. While it requires some care, it aims at removing some of the tediousness of Stava authentication process.

### 📝 Setup 

#### Creating a Strava Application

The first thing you need to do before using this library is creating a Strava application. The process isn't complex but requires a few steps. It is well described in the [Strava API documentation](https://developers.strava.com/docs/getting-started), but here we try to make it simpler.

In short, a Strava application is an entity registered in your account that allows the interaction with the Strava API. It can be used for various operations, such as accessing past activities data or uploading new activities. 

An application is characterized by a few important pieces of information:

- `client_id`: the id of the application.
- `client_secret`: a secret code assigned to the application.
- `access_token`: a token that allows the application to access data.

These information are created and provided as soon as the application is created. However, you still need to authorize the application to access your data. Specifically, you need to interact with the Strava API to request an authorization code for specific [scopes](https://developers.strava.com/docs/authentication/#detailsaboutrequestingaccess), which will then be exchanged for a new access token and a refresh token, which can be used to renew the access token when it expires. 

The good news is that `strava-client` can take care of this process for you (partially, at least)!

#### Authentication

Once you have the application, we need to pass the its information to the library. There are 2 possibilities:
- insert them in a file called `.strava.secrets`. You can find an example of how the file should look like in the file named `.strava.secrets.example`. Notice that you can change the name name of the settings file by changing the related variable in the `constants.py` file. 
- insert them in a `.env` file and use the `load_dotenv` function from the `dotenv` package to load them before creating the `StravaClient` class. As in the other option, you can check out the example file to see the required structure.

This magic is powered by the [pydantic_settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) package. For more information, check out the definition of the model and the expected types in the `strava_client/models/settings.py` file.

Then, you can instantiate the client as follows:

```python
from strava_client.client import StravaClient
from dotenv import load_dotenv()

# load_dotenv() # if needed..

# Initialize with default scopes (read, activity:read_all)
client = StravaClient()

# Or customize your scopes
client = StravaClient(scopes=['read', 'activity:read_all', 'profile:read_all'])
```

Upon instantiation, the secrets will be automatically loaded (either from the file or from the environment variables).

If the refresh token is provided, the client will assume that the authentication process was already completed and no more steps are needed to interact with the API.

Otherwise, it will automatically initiate the authentication procedure (the same described in the documentation). A browser window will open: you only need to authorize the application and paste the callback URL in the terminal. The client will take care of the rest.

When the process is completed, the client will save the new access token and the refresh token in a `.strava.secrets` file, so that you can reuse them in the future.

### 💁 Call API!

Once the client is authenticated, you can start interacting with the API. 

Before making a request, the client checks if the access token is still valid. If not, it will automatically refresh it, using the refresh token, and save the new access token in the settings file. You don't need to worry about it!

Currently, 2 methods are implemented:
- [`get_activities`](https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities), which allows you to retrieve the activities of the authenticated user.
- [`get_activity_stream`](https://developers.strava.com/docs/reference/#api-Streams-getActivityStreams), which allows you to retrieve the given activity streams of data (such as distance, velocity, ...).

You can find some examples of how to use them in the `examples` folder.

Here is an example of how to use the `get_activities` method

```python
# Get all activities
activities = client.get_activities()

# Activities are returned as typed StravaActivity objects
for activity in activities:
    print(f"{activity.name}: {activity.distance}m on {activity.start_date}")
```

If you need other methods, let me know and I will be happy to implement them! Or you can do that yourself, following the instructions in the next section.

## 🛠️ Development

We use `uv` as package manager. You can install it following the [documentation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer). Then, once you have cloned the repo, you can run the following command to create the environment and install the dependencies:

```bash
make dev-sync
```

### 🧪 Extending the client
The client is designed to be easily extended. You can add new API endpoints by first creating the appropriate Pydantic model for the response and then adding a new method to the `StravaClient` class. You can leverage the existing authentication and request infrastructure to streamline the process.

## 📝 Disclaimer

This project is just meant to be a simple and lightweight wrapper around the Strava API. It is not meant to be a full-fledged production-ready client, but rather a starting point that you can extend to fit your needs. If you need more functionalities, you can checkout the awesome library [stravalib](https://github.com/stravalib/stravalib).
