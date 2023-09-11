"""Config flow for BrafaLocks."""
import logging
from typing import Any

import voluptuous as vol

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_entry_oauth2_flow

from .const import DOMAIN


class TTLockAuthFlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):  # type: ignore[call-arg]
    """Config flow to handle Brafalocks OAuth2 authentication."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    async def async_step_auth(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Create an entry for auth."""
        # Flow has been triggered by external data
        errors = {}
        if user_input is not None:
            session = await self.flow_impl.login(
                user_input[CONF_USERNAME], user_input[CONF_PASSWORD]
            )
            if "errmsg" in session:
                errors["base"] = session["errmsg"]
            else:
                self.external_data = session
                return await self.async_step_creation()

        return self.async_show_form(
            step_id="auth",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )
