"""High-level Vehicle Service client built on the generated Postman SDK.

Wraps ``vehicle_service_collection_sdk.VehicleServiceCollectionSdk`` so callers
work with simple keyword arguments instead of SDK model objects.
"""

from __future__ import annotations

from typing import Any, Optional

from vehicle_service_collection_sdk import VehicleServiceCollectionSdk
from vehicle_service_collection_sdk.models import CreateAVehicleRequest

from .config import AppConfig


class VehicleServiceApp:
    """Convenience wrapper around the Vehicle Service SDK.

    :param config: Optional :class:`AppConfig`. When omitted, configuration is
        read from environment variables via :meth:`AppConfig.from_env`.
    """

    def __init__(self, config: Optional[AppConfig] = None):
        self.config = config or AppConfig.from_env()
        self._sdk = VehicleServiceCollectionSdk(
            api_key=self.config.api_key,
            base_url=self.config.base_url,
            timeout=self.config.timeout,
        )

    @property
    def sdk(self) -> VehicleServiceCollectionSdk:
        """The underlying generated SDK client, exposed for advanced use."""
        return self._sdk

    # ----- Read ---------------------------------------------------------
    def list_vehicles(self) -> Any:
        """Return all vehicles (``GET /vehicles``)."""
        return self._sdk.vehicle_service_collection_sdk.get_all_vehicles()

    def get_vehicle(self, vehicle_id: str) -> Any:
        """Return a single vehicle by id (``GET /vehicles/:id``)."""
        return self._sdk.vehicle_service_collection_sdk.retrieve_a_vehicle(vehicle_id)

    # ----- Write --------------------------------------------------------
    def create_vehicle(
        self,
        *,
        nick_name: Optional[str] = None,
        vin: Optional[str] = None,
        make: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[str] = None,
        miles: Optional[int] = None,
    ) -> Any:
        """Create a vehicle (``POST /vehicles``)."""
        request_body = CreateAVehicleRequest(
            nick_name=nick_name,
            vin=vin,
            make=make,
            model=model,
            year=year,
            miles=miles,
        )
        return self._sdk.vehicle_service_collection_sdk.create_a_vehicle(request_body)

    def update_vehicle(
        self,
        vehicle_id: str,
        *,
        nick_name: Optional[str] = None,
        vin: Optional[str] = None,
        make: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[str] = None,
        miles: Optional[int] = None,
    ) -> Any:
        """Update an existing vehicle (``PATCH /vehicles/:id``)."""
        request_body = CreateAVehicleRequest(
            nick_name=nick_name,
            vin=vin,
            make=make,
            model=model,
            year=year,
            miles=miles,
        )
        # SDK signature: update_a_collection(request_body, id_)
        return self._sdk.vehicle_service_collection_sdk.update_a_collection(
            request_body, vehicle_id
        )

    def delete_vehicle(self, vehicle_id: str) -> Any:
        """Delete a vehicle by id (``DELETE /vehicles/:id``)."""
        return self._sdk.vehicle_service_collection_sdk.delete_a_vehicle(vehicle_id)
