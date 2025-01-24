"""Options flow for Dummy Device Tracker integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE, CONF_LOCATION
from homeassistant.helpers.selector import LocationSelector

DOMAIN = "dummy_tracker"

class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Dummy Device Tracker."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            lat: float = user_input[CONF_LOCATION][CONF_LATITUDE]
            lon: float = user_input[CONF_LOCATION][CONF_LONGITUDE]
            
            # Preserve the original entity name
            entity_name = self.config_entry.data.get("entity_name", f"location_{lat}_{lon}")

            return self.async_create_entry(
                title=entity_name,
                data={
                    CONF_LATITUDE: lat, 
                    CONF_LONGITUDE: lon,
                    "entity_name": entity_name,
                }
            )

        # Get current location from config entry
        current_location = {
            CONF_LATITUDE: self.config_entry.data[CONF_LATITUDE],
            CONF_LONGITUDE: self.config_entry.data[CONF_LONGITUDE],
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_LOCATION, 
                        default=current_location
                    ): LocationSelector(),
                }
            ),
        )