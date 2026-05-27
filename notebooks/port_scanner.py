#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escáner de Puertos Simple
Uso educativo: escanea puertos abiertos en una IP o dominio.
"""

import socket
import sys
from datetime import datetime

def escanear_puerto(ip, puerto):
    """Intenta conectar a un puerto específico."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            return True
        else:
            return False
    except Exception:
        return False
    finally:
        sock.close()

def escanear_puertos(ip, rango_inicio, rango_fin):
    """Escanea un rango de puertos y muestra los abiertos."""
    print(f"\n[+] Iniciando escaneo en {ip} desde puerto {rango_inicio} hasta {rango_fin}")
    print(f"[+] Hora de inicio: {datetime.now()}\n")
    
    abiertos = []
    for puerto in range(rango_inicio, rango_fin + 1):
        if escanear_puerto(ip, puerto):
            print(f"[+] Puerto {puerto} → ABIERTO")
            abiertos.append(puerto)
        # Pequeño indicador de progreso (cada 100 puertos)
        if puerto % 100 == 0:
            print(f"   ... escaneados {puerto} puertos", end="\r")
    
    print(f"\n\n[+] Escaneo completado. Hora final: {datetime.now()}")
    if abiertos:
        print(f"\n[+] Puertos abiertos encontrados: {', '.join(map(str, abiertos))}")
    else:
        print("\n[-] No se encontraron puertos abiertos en el rango especificado.")

def main():
    print("=" * 50)
    print("   ESCÁNER DE PUERTOS - Herramienta Educativa")
    print("=" * 50)
    
    # Entrada de datos
    objetivo = input("\n[?] Ingresa la IP o dominio a escanear (ej: 127.0.0.1 o scanme.nmap.org): ").strip()
    if not objetivo:
        print("[-] No ingresaste ningún objetivo. Saliendo...")
        sys.exit(1)
    
    try:
        # Resolver dominio a IP
        ip_objetivo = socket.gethostbyname(objetivo)
        print(f"[+] Resolviendo {objetivo} → {ip_objetivo}")
    except socket.gaierror:
        print(f"[-] No se pudo resolver el dominio {objetivo}. Verifica la dirección.")
        sys.exit(1)
    
    try:
        puerto_inicio = int(input("[?] Puerto inicial (por defecto 1): ") or "1")
        puerto_fin = int(input("[?] Puerto final (por defecto 1024): ") or "1024")
        if puerto_inicio < 1 or puerto_fin > 65535 or puerto_inicio > puerto_fin:
            raise ValueError
    except ValueError:
        print("[-] Rango de puertos inválido. Debe ser entre 1 y 65535, y el inicio <= final.")
        sys.exit(1)
    
    # Advertencia ética
    print("\n⚠️  ADVERTENCIA: Escanear puertos sin autorización puede ser ilegal.")
    confirmar = input("¿Tenés permiso para escanear este objetivo? (s/N): ").strip().lower()
    if confirmar != 's':
        print("[-] Escaneo cancelado.")
        sys.exit(0)
    
    # Ejecutar escaneo
    escanear_puertos(ip_objetivo, puerto_inicio, puerto_fin)

if __name__ == "__main__":
    main()
