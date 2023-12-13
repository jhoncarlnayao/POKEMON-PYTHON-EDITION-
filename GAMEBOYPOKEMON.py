import random
import os


skills = False


def clear():
    os.system('cls' if os.name == 'nt'else 'clear')


def Bulbasaur(userhealth, enemyhealth, pokemonchar):
    print("╔════════════════════════╗")
    print("║   Bulbasaur Skill      ║")
    print("╠════════════════════════╣")
    print("║  [1] TEST SKILL        ║")
    print("║  [2] Skills            ║")
    print("║  [3] Exit              ║")
    print("╚════════════════════════╝")
    skills = input("Input your choice here: ")
    print("───────────────────────────────────────────────────── ")

    if skills == "1":
        print("")
        userdamage = random.randint(15, 20)
        enemydamage = random.randint(5, 15)

        enemyhealth -= userdamage
        userhealth -= enemydamage
        print("\n")
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                      BATTLE INFORMATION!                      ║")
        print("╠═══════════════════════════════════════════════════════════════╣")
        print(
            f"║      {pokemonchar} dealt {userdamage} damage to the Wild Pokemon!            ║")
        print("║     ─────────────────────────────────────────────────────     ║")
        print(
            f"║        Wild Pokemon dealt {enemydamage} damge to your Pokemon            ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print("\n\n")
        if userhealth <= 0:
            print("\nYour Pokemon fainted. Game over!")
        elif enemyhealth <= 0:
            print("You Defeated a Wild Pokemon. Congratulations!!!!\n")
        else:
            print("\nThe Battle continues..\n")


def Charmander(enemyhealth, userhealth, pokemonchar):
    print("╔════════════════════════╗")
    print("║   Charmander Skill     ║")
    print("╠════════════════════════╣")
    print("║  [1] TEST SKILL        ║")
    print("║  [2] Skills            ║")
    print("║  [3] Exit              ║")
    print("╚════════════════════════╝")
    skills = input("Input your choice here: ")
    print("─────────────────────────────────────────────────────")

    if skills == "1":
        print("")
        userdamage = random.randint(15, 20)
        enemydamage = random.randint(5, 15)

        enemyhealth -= userdamage
        userhealth -= enemydamage
        print("\n")
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                      BATTLE INFORMATION!                      ║")
        print("╠═══════════════════════════════════════════════════════════════╣")
        print(
            f"║      {pokemonchar} dealt {userdamage} damage to the Wild Pokemon!            ║")
        print("║     ─────────────────────────────────────────────────────     ║")
        print(
            f"║        Wild Pokemon dealt {enemydamage} damge to your Pokemon            ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print("\n\n")

        if userhealth <= 0:
            print("\nYour Pokemon fainted. Game over!")
        elif enemyhealth <= 0:
            print("You Defeated a Wild Pokemon. Congratulations!!!!\n")
        else:
            print("\nThe Battle continues..\n")


def Squirtle(enemyhealth, userhealth, pokemonchar):
    print("╔════════════════════════╗")
    print("║     Squirtle Skill     ║")
    print("╠════════════════════════╣")
    print("║  [1] TEST SKILL        ║")
    print("║  [2] Skills            ║")
    print("║  [3] Exit              ║")
    print("╚════════════════════════╝")
    skills = input("Input your choice here: ")
    print("─────────────────────────────────────────────────────")

    if skills == "1":
        print("")
        userdamage = random.randint(15, 20)
        enemydamage = random.randint(5, 15)

        enemyhealth -= userdamage
        userhealth -= enemydamage
        print("\n")
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                      BATTLE INFORMATION!                      ║")
        print("╠═══════════════════════════════════════════════════════════════╣")
        print(
            f"║      {pokemonchar} dealt {userdamage} damage to the Wild Pokemon!            ║")
        print("║     ─────────────────────────────────────────────────────     ║")
        print(
            f"║        Wild Pokemon dealt {enemydamage} damge to your Pokemon            ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print("\n\n")
        if userhealth <= 0:
            print("\nYour Pokemon fainted. Game over!")
        elif enemyhealth <= 0:
            print("You Defeated a Wild Pokemon. Congratulations!!!!\n")
        else:
            print("\nThe Battle continues..\n")


def battleplay(userhealth, enemyhealth, pokemonchar):
    clear()
    print("╔════════════════════════╗")
    print("║         WARNING!!      ║")
    print("╠════════════════════════╣")
    print("║A wild Pokemon appeard!!║")
    print("╚════════════════════════╝")
    print("───────────────────────────────────────────────────── ")
    print("\n")

    while userhealth > 0 and enemyhealth > 0:
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                      Pokemon HealthBar                        ║")
        print("╠═══════════════════════════════════════════════════════════════╣")
        print(
            f"║                      {pokemonchar} | HP: {userhealth}                       ║")
        print("║     ─────────────────────────────────────────────────────     ║")
        print(
            f"║                     Wild Pokemon | HP: {enemyhealth}                     ║")
        print("╚═══════════════════════════════════════════════════════════════╝")

        print("\n")

        print("╔════════════════════════╗")
        print("║     Choose Action      ║")
        print("╠════════════════════════╣")
        print("║  [1] Tackle            ║")
        print("║  [2] Skills            ║")
        print("║  [3] Run away          ║")
        print("╚════════════════════════╝")
        action = input("Input your choice here: ")
        print("───────────────────────────────────────────────────── ")
        print("\n")

        if action == "1":
            userdamage = random.randint(1, 15)
            enemydamage = random.randint(1, 15)

            enemyhealth -= userdamage
            userhealth -= enemydamage
            print("\n")
            print("╔═══════════════════════════════════════════════════════════════╗")
            print("║                      BATTLE INFORMATION!                      ║")
            print("╠═══════════════════════════════════════════════════════════════╣")
            print(
                f"║      {pokemonchar} dealt {userdamage} damage to the Wild Pokemon!            ║")
            print("║     ─────────────────────────────────────────────────────     ║")
            print(
                f"║        Wild Pokemon dealt {enemydamage} damge to your Pokemon            ║")
            print("╚═══════════════════════════════════════════════════════════════╝")
            print("\n\n")

            if userhealth <= 0:
                print("\nYour Pokemon fainted. Game over!")
            elif enemyhealth <= 0:
                print("You Defeated a Wild Pokemon. Congratulations!!!!\n")
            else:
                print("\nThe Battle continues..\n")
        elif action == "2":
            if pokemonchar == "Bulbasaur":
                Bulbasaur(userhealth, enemyhealth, pokemonchar)
            elif pokemonchar == "Charmander":
                Charmander(userhealth, enemyhealth, pokemonchar)
            elif pokemonchar == "Squirtle":
                Squirtle(userhealth, enemyhealth, pokemonchar)

        elif action == "3":
            print(f"{pokemonchar} Runs away! Do better next time")
            input("Press enter to continue")
            mainpokemon()

            if userhealth <= 0:
                print("\nYour Pokemon fainted. Game over!")
            elif enemyhealth <= 0:
                print("You Defeated a Wild Pokemon. Congratulations!!!!\n")
            else:
                print("\nThe Battle continues..\n")
        else:
            print("Invalid Actions!")


def mainpokemon():
    global pokemonchar
    clear()
    while True:
        print("╔════════════════════════╗")
        print("║Pokemon Console Edition ║")
        print("╠════════════════════════╣")
        print("║  [1] Play              ║")
        print("║  [2] Info              ║")
        print("║  [3] Exit              ║")
        print("╚════════════════════════╝")
        choice = input("Input your choice here: ")
        print("─────────────────────────────────────────────────────")

        if choice == "1":
            # userhealth=int(input("Enter your Pokemon health: "))
            print("╔════════════════════════╗")
            print("║     Choose a Pokemon   ║")
            print("╠════════════════════════╣")
            print("║  [1] Bulbasaur         ║")
            print("║  [2] Charmander        ║")
            print("║  [3] Squirtle          ║")
            print("╚════════════════════════╝")
            pokemonchar = input("Input your choice here: ")
            print("─────────────────────────────────────────────────────")
            if pokemonchar == "1":
                pokemonchar = "Bulbasaur"
            elif pokemonchar == "2":
                pokemonchar = "Charmander"
            elif pokemonchar == "3":
                pokemonchar = "Squirtle"
            userhealth = 35
            enemyhealth = random.randint(15, 55)
            battleplay(userhealth, enemyhealth, pokemonchar)
        elif choice=="2":
            print("Game Information: ")
            print("'a bored BSIT student made a copy writed game,\nwith a great mind comes with a great coding responsibility '")
            print("\nGame : Pokemon console Edition")
            print("Dev  : Fuujin")
            input("\n Press enter to go back in main menu.")
            mainpokemon()
        elif choice=="3":
            print(" ' Comback stronger little stranger ' ")
            break
        
if __name__ == "__main__":
    mainpokemon()
