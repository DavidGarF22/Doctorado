import logging
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import (
    ModbusServerContext,
    ModbusSlaveContext,
    ModbusSequentialDataBlock,
)

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

# 1. Bloques de datos de ejemplo (todos presentes y de lectura/escritura)
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 1000),   # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0] * 1000),   # Coils
    hr=ModbusSequentialDataBlock(0, [0] * 1000),   # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0] * 1000),   # Input Registers
    zero_mode=True,
)

# 2. Inicializar algunos valores
store.setValues(3, 100, [1234, 5, 6, 7, 8])  # FC3/FC6 → Holding
store.setValues(3, 200, [9])

context = ModbusServerContext(slaves=store, single=True)

# 3. Identificación del servidor
identity = ModbusDeviceIdentification()
identity.VendorName = "ICS-LAB"
identity.ProductCode = "PLCVIRT"
identity.VendorUrl = "https://pymodbus.readthedocs.io"
identity.ProductName = "Virtual PLC Modbus/TCP"
identity.ModelName = "pymodbus-server"
identity.MajorMinorRevision = "3.6.4"

logging.info("Starting Modbus/TCP synchronous server on port 1502 (full context, RW)...")

# 4. Arranque
StartTcpServer(
    context=context,
    identity=identity,
    address=("0.0.0.0", 1502),
)
