def checkFailures(passcode, attempts):
  fails = 0
  for attempt in attempts:
    fails = fails+1 if attempt != passcode else 0
    if fails >= 10: return True
  return False

passcode1 = "1111"
attempts1 = ["1111", "4444","9999", "3333","8888", "2222","7777", "0000","6666", "7285","5555", "1111"]
print(checkFailures(passcode1, attempts1))

passcode2 = "1234"
attempts2 = ["9999", "9999","9999", "9999","9999", "9999","9999", "1234","9999", "9999","9999", "9999"]
print(checkFailures(passcode2, attempts2))