from pyscript import display, document

def converter(e):
    document.getElementById("output").innerHTML = ""
    input = int(document.getElementById("input").value)
    
    celsius = (input - 32) * 5 / 9
    answer = float(celsius)
    
    display(f"The temperature in Celsius is: {answer:.2f}°C", target="output")
    
    if answer >= 37.8:
        display("Warning: The temperature indicates a fever.", target="output")
    else:
        display("The temperature is within the normal range.", target="output")
    