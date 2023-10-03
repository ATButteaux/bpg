#!/usr/bin/python3

from ast import literal_eval
import base58
import hashlib
import sys

def showHelp():
  print("bpg.py ver 20231002")
  print()
  print("HELP")
  print("====")
  print("ca     Clear all")
  print("sc     Clear Secret")
  print("s XYZ  Change secret to XYZ")
  print("dc     Data Clear")
  print("d XYZ  Change data to XYZ")
  print("q      Quit and wipe working data")
  print("sd     Change secret to decimal string")
  print("sh     Change secret to sha256 hash")
  print("sl     Change secret to left side Base58")
  print("sr     Change secret to right side Base58")
  print("?      Show help")
  print()


showHelp()

secret_string = ""
data_string = ""
encoding_string = ""
hash_string = ""
decimal_string = ""
base58_string = ""
hash = ""

while True:
  print("Secret:       " + secret_string)
  print("Data:         " + data_string)
  print("Hash:         " + hash_string)
  print("Decimal:      " + decimal_string)
  print("Base58:       " + base58_string)
  print()

  command = input("Command: ")
  print()

  match command[0:2].lower():
    case "ca":
      secret_string = ""
      data_string = ""
      encoding_string = ""
      hash_string = ""
      decimal_string = ""
      base58_string = ""
      print("All variables cleared")
      print()
    case "d ":
      data_string = command[2:]
      print("Data set to  : " + data_string)
      print()
    case "s ":
      secret_string = command[2:]
      data_string = "*"
      print("Secret set to: " + secret_string)
      print("Data set to  : " + data_string)
      print()
    case "sc":
      secret_string = ""
      print("Secret cleared")
      print()
    case "dc":
      data_string = ""
      print("Data cleared")
      print()
    case "sd":
      secret_string = decimal_string
      data_string = "*"
      print("Secret set to decimal string")
      print()
    case "sh":
      secret_string = hash_string
      data_string = "*"
      print("Secret set to hash")
      print()
    case "sl":
      secret_string = base58_string[0:17]
      data_string = "*"
      print("Secret set to left side of Base58")
      print()
    case "sr":
      secret_string = base58_string[19:]
      data_string = "*"
      print("Secret set to right side of Base 58")
      print()
    case "q":
      del secret_string
      del data_string
      del encoding_string
      del hash_string
      del decimal_string
      del base58_string
      del hash
      print("Sensitive data erased.")
      print()
      break
    case "?":
      showHelp()
      continue
      
  encoding_string = secret_string + "-" + data_string

  hash = hashlib.new('sha256')
  hash.update(encoding_string.encode('utf-8'))
  hash_string = hash.hexdigest()

  decimal_string = "0x" + hash_string
  decimal_string = literal_eval(decimal_string)
  decimal_string = str(decimal_string)
  decimal_string = decimal_string[0:5] + " " + decimal_string[5:10] + " " + decimal_string[10:15] + " " + decimal_string[15:20] + " " + decimal_string[20:25] + " " + decimal_string[25:30] + " " + decimal_string[30:35] + " " + decimal_string[35:40] + " " + decimal_string[40:45] + " " + decimal_string[45:50] + " " + decimal_string[50:55] + " " + decimal_string[55:60] + " " + decimal_string[60:65] + " " + decimal_string[65:70] + " " + decimal_string[70:75]
  
  base58_string = str(base58.b58encode(bytes.fromhex(hash_string)), encoding='utf-8')
  base58_string = base58_string[0:5] + "-" + base58_string[5:10] + "-" + base58_string[10:15] + "  " + base58_string[15:20] + "-" + base58_string[20:25] + "-" + base58_string[25:30]
  
  continue
