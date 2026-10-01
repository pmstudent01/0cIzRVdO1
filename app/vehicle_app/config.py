"""Application configuration, loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_BASE_URL = "http://localhost:4500"
DEFAULT_TIMEOUT = 30.0


@dataclass(frozen=True)
class AppConfig:
    """Runtime configuration for the Vehicle Service app.

    :param base_url: Base URL of the Vehicle Service API.
    :param api_key: Value sent in the ``X-API-Key`` header (may be empty).
    :param timeout: Per-request timeout, in seconds.
    """

    base_url: str = DEFAULT_BASE_URL
    api_key: str | None = None
    timeout: float = DEFAULT_TIMEOUT

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Build config from environment variables, falling back to defaults."""
        base_url = os.getenv("VEHICLE_API_BASE_URL", DEFAULT_BASE_URL).strip()
        api_key = os.getenv("VEHICLE_API_KEY") or None

        raw_timeout = os.getenv("VEHICLE_API_TIMEOUT")
        try:
            timeout = float(raw_timeout) if raw_timeout else DEFAULT_TIMEOUT
        except ValueError:
            timeout = DEFAULT_TIMEOUT

        return cls(base_url=base_url or DEFAULT_BASE_URL, api_key=api_key, timeout=timeout)
