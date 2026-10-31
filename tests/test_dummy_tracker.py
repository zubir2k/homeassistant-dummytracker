"""End-to-end tests for Dummy Device Tracker."""
from homeassistant.config_entries import ConfigEntryState
from homeassistant.const import CONF_LATITUDE, CONF_LOCATION, CONF_LONGITUDE, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.dummy_tracker.const import CONF_ENTITY_NAME, DOMAIN

LOC = {CONF_LATITUDE: 2.99, CONF_LONGITUDE: 101.79}


async def test_user_flow_and_entity(hass: HomeAssistant) -> None:
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    assert result["type"] is FlowResultType.FORM
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_LOCATION: LOC, CONF_NAME: "Test Pin"}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    state = hass.states.get("device_tracker.dummy_test_pin")
    assert state is not None
    assert state.attributes["latitude"] == 2.99
    assert state.attributes["longitude"] == 101.79
    assert state.attributes["friendly_name"] == "Test Pin"

    # duplicate aborts
    result = await hass.config_entries.flow.async_init(DOMAIN, context={"source": "user"})
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_LOCATION: LOC, CONF_NAME: "Test Pin"}
    )
    assert result["type"] is FlowResultType.ABORT


async def test_options_flow_moves_tracker(hass: HomeAssistant) -> None:
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id="dummy_tracker_Office",
        data={**LOC, CONF_ENTITY_NAME: "Office"},
        title="Office",
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert hass.states.get("device_tracker.dummy_office").attributes["latitude"] == 2.99

    result = await hass.config_entries.options.async_init(entry.entry_id)
    assert result["type"] is FlowResultType.FORM
    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {CONF_LOCATION: {CONF_LATITUDE: 3.15, CONF_LONGITUDE: 101.71}},
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    state = hass.states.get("device_tracker.dummy_office")
    assert state.attributes["latitude"] == 3.15
    assert state.attributes["longitude"] == 101.71

    assert await hass.config_entries.async_unload(entry.entry_id)
    assert entry.state is ConfigEntryState.NOT_LOADED
