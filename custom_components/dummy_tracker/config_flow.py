"""Config and options flow for the Dummy Device Tracker integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlowWithReload,
)
from homeassistant.const import CONF_LATITUDE, CONF_LOCATION, CONF_LONGITUDE, CONF_NAME
from homeassistant.core import callback
from homeassistant.helpers.selector import LocationSelector, TextSelector

from .const import CONF_ENTITY_NAME, DOMAIN


class DummyTrackerConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Dummy Device Tracker."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        if user_input is not None:
            lat: float = user_input[CONF_LOCATION][CONF_LATITUDE]
            lon: float = user_input[CONF_LOCATION][CONF_LONGITUDE]

            # Name is optional; fall back to the coordinates.
            entity_name = (user_input.get(CONF_NAME) or "").strip() or (
                f"location_{lat}_{lon}"
            )

            # Unique ID format kept from v1.0.x so existing entries still match.
            await self.async_set_unique_id(f"dummy_tracker_{entity_name}")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=entity_name,
                data={
                    CONF_LATITUDE: lat,
                    CONF_LONGITUDE: lon,
                    CONF_ENTITY_NAME: entity_name,
                },
            )

        home_location = {
            CONF_LATITUDE: self.hass.config.latitude,
            CONF_LONGITUDE: self.hass.config.longitude,
        }

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_LOCATION, default=home_location
                    ): LocationSelector(),
                    vol.Optional(CONF_NAME): TextSelector(),
                }
            ),
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> DummyTrackerOptionsFlow:
        """Create the options flow."""
        return DummyTrackerOptionsFlow()


class DummyTrackerOptionsFlow(OptionsFlowWithReload):
    """Move the dummy tracker to a new location."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(
                data={
                    CONF_LATITUDE: user_input[CONF_LOCATION][CONF_LATITUDE],
                    CONF_LONGITUDE: user_input[CONF_LOCATION][CONF_LONGITUDE],
                }
            )

        current = {**self.config_entry.data, **self.config_entry.options}
        current_location = {
            CONF_LATITUDE: current[CONF_LATITUDE],
            CONF_LONGITUDE: current[CONF_LONGITUDE],
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_LOCATION, default=current_location
                    ): LocationSelector(),
                }
            ),
        )
