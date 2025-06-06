"""Config flow for Dummy Device Tracker integration."""
from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE, CONF_LOCATION
from homeassistant.helpers.selector import LocationSelector

DOMAIN = "dummy_tracker"

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Dummy Device Tracker."""
    
    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            lat: float = user_input[CONF_LOCATION][CONF_LATITUDE]
            lon: float = user_input[CONF_LOCATION][CONF_LONGITUDE]
            
            # Make entity name optional
            entity_name = user_input.get("Entity Name", f"location_{lat}_{lon}")
            
            await self.async_set_unique_id(f"dummy_tracker_{entity_name}")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=entity_name,
                data={
                    CONF_LATITUDE: lat,
                    CONF_LONGITUDE: lon,
                    "entity_name": entity_name,
                }
            )

        home_location = {
            CONF_LATITUDE: self.hass.config.latitude,
            CONF_LONGITUDE: self.hass.config.longitude,
        }

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_LOCATION, default=home_location): LocationSelector(),
                    vol.Optional("Entity Name"): str,
                }
            ),
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        """Create the options flow."""
        from .options_flow import OptionsFlowHandler
        return OptionsFlowHandler(config_entry)
