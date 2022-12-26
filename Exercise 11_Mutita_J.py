height = int(input("Please Enter Height Of Pyramid : "))
for x in range(height):
    text = ""
    for y in range((x * 2) +1):
        text += "*"
    print((height-(x+1))*" ",text)

