# Vehicle Service App

A small Python application that implements the **Vehicle Service API** by consuming the
generated `vehicle_service_collection_sdk` (Postman SDK, generated from the
*Vehicle Service Collection*).

It wraps the SDK in a thin, convenient client (`VehicleServiceApp`) and ships a
command-line interface (`vehicle-cli`) for the full CRUD surface:

| Operation            | SDK method              | HTTP               |
| -------------------- | ----------------------- | ------------------ |
| List all vehicles    | `get_all_vehicles`      | `GET /vehicles`    |
| Get one vehicle      | `retrieve_a_vehicle`    | `GET /vehicles/:id`|
| Create a vehicle     | `create_a_vehicle`      | `POST /vehicles`   |
| Update a vehicle     | `update_a_collection`   | `PATCH /vehicles/:id`|
| Delete a vehicle     | `delete_a_vehicle`      | `DELETE /vehicles/:id`|

## Setup

```bash
cd app
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

`requirements.txt` installs the locally-generated SDK (editable) plus its
dependencies, so you do not need to publish the SDK to PyPI.

## Configuration

Configuration is read from environment variables (see `.env.example`):

| Variable               | Default                   | Description                      |
| ---------------------- | ------------------------- | -------------------------------- |
| `VEHICLE_API_BASE_URL` | `http://localhost:4500`   | Base URL of the Vehicle Service  |
| `VEHICLE_API_KEY`      | _(empty)_                 | Value for the `X-API-Key` header |
| `VEHICLE_API_TIMEOUT`  | `30`                      | Request timeout in seconds       |

You can export them directly or copy `.env.example` to `.env` and source it.

## Usage

```bash
# List all vehicles
python -m vehicle_app list

# Retrieve one vehicle
python -m vehicle_app get <vehicle-id>

# Create a vehicle
python -m vehicle_app create \
  --nick-name "The Lisa Marie" \
  --vin 4M2DV11W4RDJ53329 \
  --make Mercury --model Villager --year 1994 --miles 10000

# Update a vehicle
python -m vehicle_app update <vehicle-id> --miles 20000

# Delete a vehicle
python -m vehicle_app delete <vehicle-id>
```

After `pip install`, the `vehicle-cli` console script is also available:

```bash
vehicle-cli list
```

## Using the client in your own code

```python
from vehicle_app import VehicleServiceApp

app = VehicleServiceApp()  # reads config from environment
vehicles = app.list_vehicles()
created = app.create_vehicle(nick_name="Daily", vin="1HG....", make="Honda")
```
