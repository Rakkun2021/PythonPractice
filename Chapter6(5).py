word = 'X-DSPAM-Confidence:0.8475'
data = word[19:]  # Finds the 'Colon' character and extracts portion after colon
s = float(data)  # Float function that converts string into a floating point number
print(s)
