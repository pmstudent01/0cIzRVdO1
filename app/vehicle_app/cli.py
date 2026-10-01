"""Command-line interface for the Vehicle Service app."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .client import VehicleServiceApp
from .config import AppConfig


def _print(result: Any) -> None:
    """Pretty-print a result as JSON when possible, else as text."""
    try:
        # SDK models expose model_dump(); dicts/lists serialize directly.
        if hasattr(result, "model_dump"):
            result = result.model_dump()
        print(json.dumps(result, indent=2, default=str))
    except (TypeError, ValueError):
        print(result)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vehicle-cli",
        description="Interact with the Vehicle Service API via the generated SDK.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List all vehicles")

    p_get = sub.add_parser("get", help="Retrieve a vehicle by id")
    p_get.add_argument("vehicle_id", help="The vehicle id")

    def add_vehicle_fields(p: argparse.ArgumentParser) -> None:
        p.add_argument("--nick-name", dest="nick_name")
        p.add_argument("--vin")
        p.add_argument("--make")
        p.add_argument("--model")
        p.add_argument("--year")
        p.add_argument("--miles", type=int)

    p_create = sub.add_parser("create", help="Create a vehicle")
    add_vehicle_fields(p_create)

    p_update = sub.add_parser("update", help="Update a vehicle by id")
    p_update.add_argument("vehicle_id", help="The vehicle id")
    add_vehicle_fields(p_update)

    p_delete = sub.add_parser("delete", help="Delete a vehicle by id")
    p_delete.add_argument("vehicle_id", help="The vehicle id")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    app = VehicleServiceApp(AppConfig.from_env())

    try:
        if args.command == "list":
            _print(app.list_vehicles())
        elif args.command == "get":
            _print(app.get_vehicle(args.vehicle_id))
        elif args.command == "create":
            _print(
                app.create_vehicle(
                    nick_name=args.nick_name,
                    vin=args.vin,
                    make=args.make,
                    model=args.model,
                    year=args.year,
                    miles=args.miles,
                )
            )
        elif args.command == "update":
            _print(
                app.update_vehicle(
                    args.vehicle_id,
                    nick_name=args.nick_name,
                    vin=args.vin,
                    make=args.make,
                    model=args.model,
                    year=args.year,
                    miles=args.miles,
                )
            )
        elif args.command == "delete":
            _print(app.delete_vehicle(args.vehicle_id))
    except Exception as exc:  # noqa: BLE001 - surface SDK/transport errors cleanly
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
