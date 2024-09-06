# Ohmconnect-event
Get information about the upcoming OhmHour event.

With this integration, you can access the scheduled start and end times of an upcoming OhmHour event, along with the total duration of the event.

# Installation

Copy the custom_components/ohmconnect-event folder and contents into your custom_components folder in Home Assistant.

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
1. Open [https://login.ohmconnect.com/api/v2/upcoming_events](https://login.ohmconnect.com/api/v2/upcoming_events) and log in.
2. Open your browser’s developer tools (right-click and select "Inspect", or press `F12`).
3. Navigate to the "Network" tab.
4. Refresh the page to capture the network activity.
5. Look for the `GET` request to the `/upcoming_events` endpoint.
6. Click on the request, then go to the `Headers` section.
7. Under the `Request Headers`, find the `Cookie:` field.
8. In the `Cookie` field, locate your session key (found after `session=`) and the track key (found after `ohm_track_key=`).

