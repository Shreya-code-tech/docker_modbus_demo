# Modbus Docker Demo

This project demonstrates a Dockerized setup for a Modbus server and client.

## Prerequisites

- Docker installed on your machine.
- Python and `pymodbus` installed (for testing the client locally).

---

## Running the Modbus Server

Start the Modbus server using the Docker Hub image:

```bash
docker run -d --name modbus-server -p 502:502 oitc/modbus-server
