# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1: Greet template
def greeting(name):
    return f'Hola {name} , How are you!'

print(greeting('Clara'))

# Part 2: Force
def force(mass, body='earth'):
    # Dictionary of gravity factors for each celestial body
    gravity_factors = {
        'mercury': 3.7,
        'venus': 8.87,
        'earth': 9.8,
        'mars': 3.711,
        'jupiter': 24.79,
        'saturn': 10.44,
        'uranus': 8.69,
        'neptune': 11.15,
        'pluto': 0.62,
        'moon': 1.62,
        'sun': 274
    }
    gravity_factor = round(gravity_factors[body], 1)
    return mass * gravity_factor

mass = 5.9722 * (10^24)
gravity_factor = 9.8
print(force(mass))

#Part 3:Gravity
def pull(m1, m2, d):
    G = 6.67408 * 10**-11
    return (G * m1 * m2) / d**2;
print(pull(3.5, 68.6, 6))