#Adventure Game JeremyBeam
import random
print("You are lost underground in a maze of tunnels")
dangerTunnel = (random.randint(1,5))
print("Wendigo in tunnel", dangerTunnel)
tunnelChoice = 0
while tunnelChoice < 1 or tunnelChoice > 5:
    tunnelChoice = int(input("Choose tunnel 1 to tunnel 5:"))    
if tunnelChoice == dangerTunnel:
    print("You entered a tunnel with a Wendigo. Watch out!")
elif tunnelChoice == dangerTunnel:
    print("You entered an empty tunnel. You are safe for now.")
if tunnelChoice == 3:
    print("You found an exit!")
elif tunnelChoice != 3:
    print("You entered an empty tunnel. You are safe for now.")
input("Press ENTER to exit")
