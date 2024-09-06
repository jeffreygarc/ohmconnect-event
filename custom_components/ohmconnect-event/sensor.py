import requests
import json
import logging
import voluptuous as vol
from datetime import datetime
from operator import length_hint

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "OhmConnect Event"

CONF_SESSION = "session"
CONF_OHM_TRACK_KEY = "ohm_track_key"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_SESSION): cv.string,
    vol.Required(CONF_OHM_TRACK_KEY): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the OhmConnect sensor."""
    name = config.get(CONF_NAME)
    session = config.get(CONF_SESSION)
    ohm_track_key = config.get(CONF_OHM_TRACK_KEY)

    # Initialize the sensor
    add_entities([OhmConnectEventSensor(name, session, ohm_track_key)], True)

class OhmConnectEventSensor(Entity):
    """Representation of an OhmConnect sensor."""

    def __init__(self, name, session, ohm_track_key):
        """Initialize the sensor."""
        self._name = name
        self._state = None
        self._start_dttm = None
        self._end_dttm = None
        self._duration = None
        self._session = session
        self._ohm_track_key = ohm_track_key
        self._unique_id = "ohmconnect_next_event"  # Generate unique ID
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the start timestamp as the state of the sensor."""
        return self._start_dttm

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return self._unique_id

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return "timestamp"

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "end_time": self._end_dttm,
            "duration": self._duration,
        }

    def update(self):
        """Fetch new state data for the sensor."""
        api_url = "https://login.ohmconnect.com/api/v2/upcoming_events"
        cookies = {
            'session': self._session,
            'ohm_track_key': self._ohm_track_key
        }

        try:
            response = requests.get(api_url, cookies=cookies)
            data = json.loads(response.text)

            ## Get the nearest event if there is more than one
            nearest_event = (length_hint(data) -1)

            self._start_dttm = data[nearest_event]["start_dttm"]  # Ensure this is in ISO format
            self._end_dttm = data[nearest_event]["end_dttm"]  # Ensure this is in ISO format
            _LOGGER.debug(f"Fetched OhmConnect event: {data[0]}")

            ## Calcualte duration
            dt_start = datetime.fromisoformat(self._start_dttm)
            dt_end = datetime.fromisoformat(self._end_dttm)
            duration = dt_end - dt_start

            ## Format duration into string

            hours, remainder = divmod(duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            self._duration =  f"{hours:02}:{minutes:02}:{seconds:02}"


        except Exception as e:
            _LOGGER.error(f"Error fetching data from OhmConnect: {e}")
            self._start_dttm = None
            self._end_dttm = None
