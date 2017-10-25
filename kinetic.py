def kinetic_energy(get_mass, velocity):
   KE = (0.5*get_mass*velocity)**2
   return KE

def main():
    get_mass = float(input('Please enter the mass in kilograms: '))
    velocity = float(input('Please enter the velocity in meters per seconds: '))

    print(kinetic_energy(get_mass, velocity), "is the objects kinetic energy.")



main()
      
