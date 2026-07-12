# Plan: Add udocker Fallback Support to MT5Linux_RakiFella

## Overview
Create a Python helper module that programmatically detects and uses Docker or udocker to run the MT5Linux_RakiFella container.

## Status
Saved for later - NOT YET IMPLEMENTED

## Implementation Plan

### 1. Create `MT5Linux_RakiFella/_docker_helper.py`

Functions to implement:

```python
def _check_docker_available() -> bool:
    """Check if Docker is available by running 'docker info'."""

def _check_udocker_available() -> bool:
    """Check if udocker is available by running 'udocker --version'."""

def get_container_runtime() -> Literal['docker', 'udocker', None]:
    """Returns the available container runtime ('docker', 'udocker', or None)."""

def pull_image(image: str, runtime: str) -> bool:
    """Pull the Docker image using the specified runtime."""

def run_container(
    image: str,
    runtime: str,
    mt5_host: str = "0.0.0.0",
    vnc_password: str = "password",
    mt5_login: Optional[str] = None,
    mt5_password: Optional[str] = None,
    mt5_server: Optional[str] = None,
    novnc_port: int = 6081,
    mt5_port: int = 18812,
    name: str = "MT5Linux_RakiFella"
) -> bool:
    """Run the MT5Linux_RakiFella container with the specified runtime and configuration."""

def stop_container(runtime: str, name: str = "MT5Linux_RakiFella") -> bool:
    """Stop the MT5Linux_RakiFella container."""

def remove_container(runtime: str, name: str = "MT5Linux_RakiFella") -> bool:
    """Remove the MT5Linux_RakiFella container."""

def get_container_status(runtime: str, name: str = "MT5Linux_RakiFella") -> str:
    """Get the current status of the MT5Linux_RakiFella container."""
```

### 2. Environment Variables Supported
Same as docker-compose.yml:
- `MT5_HOST` (default: "0.0.0.0")
- `VNC_PASSWORD` (default: "password")
- `MT5_LOGIN` (optional)
- `MT5_PASSWORD` (optional)
- `MT5_SERVER` (optional)

### 3. Ports
- `6081` - VNC/noVNC web interface
- `18812` - MT5/RPyC server

### 4. Runtime Differences to Handle
- **Docker**: Uses `docker run -d` (detach mode supported)
- **udocker**: Uses `udocker run` (no `-d` flag, runs in foreground)
- **udocker** may need `--user=root` or `--exec-mode=PROOT` for some containers

### 5. Modify `MT5Linux_RakiFella/__init__.py`
Export helper functions for public use:
```python
from MT5Linux_RakiFella._docker_helper import (
    get_container_runtime,
    run_container,
    stop_container,
    remove_container,
    get_container_status,
)
```

## Files to Create/Modify
- **Create**: `MT5Linux_RakiFella/_docker_helper.py` (~150 lines)
- **Modify**: `MT5Linux_RakiFella/__init__.py` - add exports

## Example Usage After Implementation
```python
from MT5Linux_RakiFella import get_container_runtime, run_mt5_container

runtime = get_container_runtime()  # Returns 'docker', 'udocker', or None
if runtime:
    run_mt5_container(
        image='lprett/MT5Linux_RakiFella:latest',
        mt5_login='12345678',
        mt5_password='password',
        mt5_server='Broker-Server'
    )
```

## Reference: Current Docker Usage
See `docker/docker-compose.yml` and `docker/README.md` for current configuration format.
