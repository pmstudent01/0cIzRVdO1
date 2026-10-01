"""Vehicle Service application package.

Thin, convenient wrapper around the generated ``vehicle_service_collection_sdk``
plus a command-line interface implementing the Vehicle Service API.
"""

from .config import AppConfig
from .client import VehicleServiceApp

__all__ = ["AppConfig", "VehicleServiceApp"]
__version__ = "1.0.0"
