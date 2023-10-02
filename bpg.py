#!/usr/bin/python3
import base58
import hashlib
import sys

def showHelp():
  print("HELP")
  print("====")
  print("ca     Clear all")
  print("sc     Clear Secret")
  print("s XYZ  Change secret to XYZ")
  print("dc     Data Clear")
  print("d XYZ  Change data to XYZ")
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

while True:
  print("Secret:       " + secret_string)
  print("Data:         " + data_string)
  print("Encoding:     " + encoding_string)
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
    case "d ":
      data_string = command[2:]
      print("Data set to  : " + data_string)
    case "s ":
      secret_string = command[2:]
      data_string = "*"
      print("Secret set to: " + secret_string)
      print("Data set to  : " + data_string)
    case "sc":
      secret_string = ""
      print("Secret cleared")
    case "dc":
      data_string = ""
      print("Data cleared")
    case "sd":
      secret_string = decimal_string
      data_string = "*"
    case "sh":
      secret_string = hash_string
      data_string = "*"
    case "sl":
      secret_string = base58_string[0:17]
      data_string = "*"
    case "sr":
      secret_string = base58_string[19:]
      data_string = "*"
    case "q":
      del secret_string
      del data_string
      del encoding_string
      del hash_string
      del decimal_string
      del base58_string
      del hash
      print("Sensitive data erased.")
      break
    case "?":
      showHelp()
      continue
      
  encoding_string = secret_string + "-" + data_string

  hash = hashlib.new('sha256')
  hash.update(encoding_string.encode('utf-8'))
  hash_string = hash.hexdigest()

  decimal_string = hash_string
  decimal_string = decimal_string.replace("a", "0")
  decimal_string = decimal_string.replace("b", "1")
  decimal_string = decimal_string.replace("c", "2")
  decimal_string = decimal_string.replace("d", "3")
  decimal_string = decimal_string.replace("e", "4")
  decimal_string = decimal_string.replace("f", "5")
  decimal_string = decimal_string[0:4] + "-" + decimal_string[4:8] + "-" + decimal_string[8:12] + "-" + decimal_string[12:16] + "-" + decimal_string[16:20] + "-" + decimal_string[20:24] + "-" + decimal_string[24:28] + "-" + decimal_string[28:32] + "-" + decimal_string[32:36] + "-" + decimal_string[36:40]
  
  base58_string = str(base58.b58encode(bytes.fromhex(hash_string)), encoding='utf-8')
  base58_string = base58_string[0:5] + "-" + base58_string[5:10] + "-" + base58_string[10:15] + "  " + base58_string[15:20] + "-" + base58_string[20:25] + "-" + base58_string[25:30]
  
  continue

