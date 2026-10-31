"""Device tracker platform for the Dummy Device Tracker integration."""
from __future__ import annotations

from homeassistant.components.device_tracker import TrackerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.util import slugify

from .const import CONF_ENTITY_NAME, DEFAULT_GPS_ACCURACY, DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the Dummy Device Tracker from a config entry."""
    async_add_entities([DummyDeviceTracker(entry)])


class DummyDeviceTracker(TrackerEntity):
    """A device tracker pinned to a fixed GPS location.

    The location never changes on its own, so there is nothing to poll:
    the entity writes its state once, and the options flow reloads the
    entry when the pin is moved.
    """

    _attr_has_entity_name = True
    _attr_name = None  # Use the device name as the entity name.
    _attr_should_poll = False

    def __init__(self, entry: ConfigEntry) -> None:
        """Set up tracker."""
        # Options (set by the options flow) win over the original data.
        config = {**entry.data, **entry.options}
        entity_name: str = config[CONF_ENTITY_NAME]

        self._attr_latitude = float(config[CONF_LATITUDE])
        self._attr_longitude = float(config[CONF_LONGITUDE])
        self._attr_location_accuracy = DEFAULT_GPS_ACCURACY

        # Unique ID and entity ID kept compatible with v1.0.x.
        self._attr_unique_id = f"dummy_tracker_{entity_name}"
        self.entity_id = f"device_tracker.dummy_{slugify(entity_name)}"

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=entity_name,
            manufacturer="zubir2k",
            model="Dummy Device Tracker",
            entry_type=DeviceEntryType.SERVICE,
        )
