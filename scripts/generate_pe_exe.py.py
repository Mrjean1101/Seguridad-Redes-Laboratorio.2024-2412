#!/usr/bin/env python3
import struct

# Generar cabecera válida PE/MZ de Windows (512 bytes)
b = bytearray(512)
b[0:2] = b'MZ'
struct.pack_into('<I', b, 60, 64)
b[64:68] = b'PE\0\0'
struct.pack_into('<HHIIIHH', b, 68, 0x14C, 1, 0, 0, 0, 224, 0x102)
struct.pack_into('<H', b, 88, 0x10B)

with open('actualizacion.exe', 'wb') as f:
  f.write(b)

print('Ejecutable PE de 512 bytes generado con éxito.')