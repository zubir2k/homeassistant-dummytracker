"""Support for Dummy Device Tracker."""
from __future__ import annotations

from homeassistant.components.device_tracker import SourceType, TrackerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE
import datetime
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Dummy Device Tracker from config entry."""
    coordinator = DummyDeviceCoordinator(hass, config_entry)
    await coordinator.async_config_entry_first_refresh()
    async_add_entities([DummyDeviceTracker(coordinator)])

class DummyDeviceCoordinator(DataUpdateCoordinator):
    """Dummy device coordinator."""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        """Initialize coordinator."""
        super().__init__(
            hass,
            logger=_LOGGER,
            name="Dummy Device Tracker",
            update_interval=datetime.timedelta(seconds=60),
        )
        self.config_entry = config_entry

    async def _async_update_data(self):
        """Update device location."""
        return {
            "latitude": self.config_entry.data[CONF_LATITUDE],
            "longitude": self.config_entry.data[CONF_LONGITUDE],
            "gps_accuracy": 10,
            "battery_level": 100,
        }

class DummyDeviceTracker(CoordinatorEntity, TrackerEntity):
    """Represent a tracked device."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: DummyDeviceCoordinator) -> None:
        """Set up tracker."""
        super().__init__(coordinator)
        
        # Get entity name from config or generate from coordinates
        entity_name = self.coordinator.config_entry.data.get("entity_name")

        # Set unique ID and entity ID
        self._attr_unique_id = f"dummy_tracker_{entity_name}"
        self.entity_id = f"device_tracker.dummy_{entity_name.lower().replace(' ', '_')}"
        
        # Set name for display
        self._attr_name = entity_name
        
    @property
    def source_type(self) -> SourceType:
        """Return the source type of the device."""
        return SourceType.GPS

    @property
    def latitude(self) -> float | None:
        """Return latitude value of the device."""
        return self.coordinator.data["latitude"]

    @property
    def longitude(self) -> float | None:
        """Return longitude value of the device."""
        return self.coordinator.data["longitude"]

    @property
    def location_accuracy(self) -> int:
        """Return the location accuracy of the device."""
        return self.coordinator.data["gps_accuracy"]

    @property
    def battery_level(self) -> int | None:
        """Return the battery level of the device."""
        return self.coordinator.data["battery_level"]