#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hash Cracker - Herramienta educativa
Intenta descifrar un hash SHA-256 usando un diccionario de palabras.
"""

import hashlib
import sys

def main():
    print("=" * 50)
    print("   HASH CRACKER (SHA-256) - Herramienta Educativa")
    print("=" * 50)

    # 1. Pedir el hash que queremos romper
    hash_objetivo = input("\n[?] Ingresa el hash SHA-256 a descifrar: ").strip()
    if not hash_objetivo:
        print("[-] No ingresaste ningún hash. Saliendo...")
        sys.exit(1)

    # 2. Pedir la ruta del archivo diccionario
    dic_file = input("[?] Ruta del archivo diccionario (ej: diccionario.txt): ").strip()
    if not dic_file:
        print("[-] No ingresaste una ruta. Saliendo...")
        sys.exit(1)

    # 3. Intentar abrir el diccionario
    try:
        with open(dic_file, 'r', encoding='utf-8') as archivo:
            # Leer todas las líneas, eliminar espacios y saltos de línea
            diccionario = [linea.strip() for linea in archivo]
    except FileNotFoundError:
        print(f"[-] No se encontró el archivo '{dic_file}'. Verifica la ruta.")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error al leer el archivo: {e}")
        sys.exit(1)

    print(f"[+] Diccionario cargado: {len(diccionario)} palabras.")

    # 4. Probar cada palabra del diccionario
    encontrado = False
    for password in diccionario:
        # Calcular el hash SHA-256 de la palabra actual
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        # Comparar con el hash objetivo
        if hash_calculado == hash_objetivo:
            print(f"\n[+] ¡ÉXITO! La contraseña original es: {password}")
            encontrado = True
            break

    # 5. Si terminó el bucle y no encontró nada
    if not encontrado:
        print("\n[-] No se encontró la contraseña en el diccionario.")

if __name__ == "__main__":
    main()
