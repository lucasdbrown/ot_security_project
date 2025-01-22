from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Define MODBUS Registers
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0]*100),  # Coils
    hr=ModbusSequentialDataBlock(0, [10]*100),  # Holding Registers (Preset value of 10)
    ir=ModbusSequentialDataBlock(0, [0]*100)   # Input Registers
)

context = ModbusServerContext(slaves=store, single=True)

# Start the MODBUS TCP Server
print("[PLC] Starting MODBUS TCP Server on port 5020...")
StartTcpServer(context, address=("0.0.0.0", 5020))
