# Ohmconnect-event
Get information about the upcoming OhmHour event.

With this integration, you can access the scheduled start and end times of an upcoming OhmHour event, along with the total duration of the event.

# Installation

### Install via HACS (Recommended)

1. Ensure HACS is installed in your Home Assistant setup.
2. Go to HACS and add this repository to the list of custom repositories.
3. Search for and install the "OhmConnect Event" integration from HACS.

### Manual Installation

1. Open the directory for your Home Assistant configuration (this is where the `configuration.yaml` file is located).
2. Check if there is a `custom_components` folder. If it doesn't exist, create one.
3. Inside the `custom_components` folder, create a new folder called `ohmconnect-event`.
4. Download the `ohmconnect-event.zip` file from the "Latest Release" section of this repository.
5. Extract the contents of the downloaded ZIP file into the `ohmconnect-event` folder you created.

# Configuration
In your configuration.yaml, add
````
sensor:
  - platform: ohmconnect-event
    session: !secret ohmconnect_event_session
    ohm_track_key: !secret ohmconnect_event_track_key
````
In your secrets.yaml, add
```
ohmconnect_event_session: "YOUR_SESSION_KEY"
ohmconnect_event_track_key: "YOUR_TRACK_KEY"
```

# How to get keys
1. Login to [OhmConnect](https://login.ohmconnect.com/) in you are not already.
2. Open [https://login.ohmconnect.com/api/v2/upcoming_events](https://login.ohmconnect.com/api/v2/upcoming_events).
3. Open your browser’s developer tools (right-click and select "Inspect", or press `F12`).
4. Navigate to the "Network" tab.
5. Refresh the page to capture the network activity.
6. Look for the `GET` request to the `/upcoming_events` endpoint.
7. Click on the request, then go to the `Headers` section.
8. Under the `Request Headers`, find the `Cookie:` field.
9. In the `Cookie` field, locate your session key (found after `session=`) and the track key (found after `ohm_track_key=`).

