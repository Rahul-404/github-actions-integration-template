import streamlit as st
from calculator.addition import add
from calculator.subtraction import subtract
from calculator.multiplication import multiply
from calculator.division import divide

st.title("🧮 Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Operation selection
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    st.success(f"Result: {result}")
