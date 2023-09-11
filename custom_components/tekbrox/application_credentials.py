"""application_credentials platform the Brafalocks integration."""

from homeassistant.components.application_credentials import (
    AuthorizationServer,
    ClientCredential,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow

from .api import TTLockAuthImplementation
from .const import OAUTH2_TOKEN


async def async_get_auth_implementation(
    hass: HomeAssistant, auth_domain: str, credential: ClientCredential
) -> config_entry_oauth2_flow.AbstractOAuth2Implementation:
    """Return custom auth implementation."""
    return TTLockAuthImplementation(
        hass,
        auth_domain,
        credential,
        AuthorizationServer(
            authorize_url="",
            token_url=OAUTH2_TOKEN,
        ),
    )
