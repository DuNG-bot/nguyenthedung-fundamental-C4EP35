height = int(input('Enter your height (cm): '))
mass = int(input('Enter your weight (kg): '))
D = mass/((height/100)**2)

if D < 16:
    print("You're severely underweight!!!")
elif D < 18.5:
    print("You're underweight!")
elif D < 25:
    print("You're normal. Keep it up :D")
elif D < 30:
    print("You're overweight. Be mindful of your health!")
else:
    print('Obesity has joined the chat >.<')


    
