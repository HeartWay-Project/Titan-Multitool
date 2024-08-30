import os
from Config.Config import *
from Config.Util import *

color_var_mapping = {
    'primary': 'primary',
    'secondary': 'secondary',
    'valid': 'valid',
    'invalid': 'invalid'
}

def update_util_file(role, new_color_name):
    util_file_path = "Settings/Config/Util.py"
    
    with open(util_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    with open(util_file_path, "w", encoding="utf-8") as file:
        for line in lines:
            if line.startswith(f"{color_var_mapping[role]} = color."):
                file.write(f"{color_var_mapping[role]} = color.{new_color_name}\n")
            else:
                file.write(line)

def parameters_menu():
    while True:
        print(f"\n{primary}--- Parameters ---\n")
        print(f"{secondary}[{primary}1{secondary}] {primary}Themes")
        print(f"{secondary}[{primary}0{secondary}] {primary}Exit\n")
        choice = input(f"Select an option -> {reset}")

        if choice == '1':
            themes_menu()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def themes_menu():
    while True:
        display_current_colors()
        print(f"\n{primary}--- Themes ---\n")
        print(f"Select a color role to change:\n")
        print(f"{secondary}[{primary}1{secondary}] {primary}Primary (primary)")
        print(f"{secondary}[{primary}2{secondary}] {primary}Secondary ({secondary}White{primary})")
        print(f"{secondary}[{primary}3{secondary}] {primary}Valid ({valid}Green{primary})")
        print(f"{secondary}[{primary}4{secondary}] {primary}Invalid ({invalid}Red{primary})")
        print(f"{secondary}[{primary}0{secondary}] {primary}Back to MultiTool\n")

        choice = input(f"{primary}Select an option -> {reset}")

        if choice == '0':
            Continue()
            Reset()

        if choice in ['1', '2', '3', '4']:
            role_name = ['primary', 'secondary', 'valid', 'invalid'][int(choice) - 1]
            print(f"\n{primary}Available colors:\n")
            for idx, (color_name, _) in enumerate(available_colors):
                print(f"{primary}[{secondary}{idx + 1}{primary}] {color_name}")
            
            color_choice = input(f"\n{primary}Enter the number for the new color of {role_name}-> {reset}")
            
            if color_choice.isdigit() and 1 <= int(color_choice) <= len(available_colors):
                new_color_name, new_color = available_colors[int(color_choice) - 1]
                change_color(role_name, new_color)
                update_util_file(role_name, new_color_name)
                print(f"{role_name.capitalize()} color has been changed to {new_color_name}.")
            else:
                Continue()
                Reset()
        else:
            Continue()
            Reset()

if __name__ == "__main__":
    parameters_menu()
