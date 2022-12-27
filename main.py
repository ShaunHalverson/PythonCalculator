def calculator():
  ### Initialize variables
  firstNumber = 0
  secondNumber = 0
  function = ""

  ### Gather first number from user
  while True:
    try:
      firstNumber = float(input("Please provide a number: "))
      break
    except:
      print("Invalid input. Please try again.")

  ### Gather operation from user
  while True:
    try:
      function = input("Please choose an operator (+, -, /, *): ")
      if(function in ['+','-','/','*']):
        break
    except:
        print("Invalid input. Please try again.")

  ### Gather third number from user
  while True:
    try:
      secondNumber = float(input("Please provide a number: "))
      break
    except:
      print("Invalid input. Please try again.")

  ### Perform calculations
  if(function == "+"):
    result = firstNumber + secondNumber
  elif(function == "-"):
    result = firstNumber - secondNumber
  elif(function == "/"):
    result = firstNumber / secondNumber
  elif(function == "*"):
    result = firstNumber * secondNumber
  else:
    result = "Invalid operator"

  ### Print result to user
  print("Your result is: ", result)
  print("\n")

if __name__ == "__main__":
  while True:
    calculator()
