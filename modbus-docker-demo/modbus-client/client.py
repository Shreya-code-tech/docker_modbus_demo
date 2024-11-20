from pymodbus.client.sync import ModbusTcpClient  # Import for pymodbus 2.5.3

def main():
    # Modbus server configuration
    server_ip = "localhost"  # Use "localhost" if both server and client are on the same machine
    server_port = 5020

    # Create Modbus TCP client
    client = ModbusTcpClient(server_ip, port=server_port)

    # Attempt to connect to the Modbus server
    if not client.connect():
        print("Failed to connect to the Modbus server.")
        return

    print("Connected to the Modbus server!")

    # Example: Read 10 coils starting at address 0
    response = client.read_coils(0, 10)
    if response.isError():
        print(f"Error reading coils: {response}")
    else:
        print(f"Coil values: {response.bits}")

    # Close the client connection
    client.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()

