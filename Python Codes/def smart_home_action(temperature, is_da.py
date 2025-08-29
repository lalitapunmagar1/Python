def smart_home_action(temperature, is_dark, at_home, security_armed, door_open):
    """Determine the action based on temperature, lighting, and security system status."""
    actions = []
    
    if temperature < 18:
        actions.append("Turn on the heater.")
    
    if temperature > 25:
        actions.append("Turn on the air conditioner.")

    if is_dark == "yes" and at_home == "yes":
        actions.append("Turn on the lights.")

    if security_armed == "yes" and door_open == "yes":
        actions.append("Sound the alarm.")
    
    if not actions:
        actions.append("No specific action required.")
    
    return actions
def main():
    try:
        
        temperature = float(input("Enter the current temperature in °C: "))
        is_dark = input("Is it dark outside? (yes/no): ")
        at_home = input("Is someone at home? (yes/no): ")
        security_armed = input("Is the security system armed? (yes/no): ")
        door_open = input("Is a door opened? (yes/no): ")
        
        if is_dark != 'yes' and is_dark != 'no':
            print("Error: 'Is it dark outside?' input must be 'yes' or 'no'.")
            return
        if at_home != 'yes' and at_home != 'no':
            print("Error: 'Is someone at home?' input must be 'yes' or 'no'.")
            return
        if security_armed != 'yes' and security_armed != 'no':
            print("Error: 'Is the security system armed?' input must be 'yes' or 'no'.")
            return
        if door_open != 'yes' and door_open != 'no':
            print("Error: 'Is a door opened?' input must be 'yes' or 'no'.")
            return
       
        actions = smart_home_action(temperature, is_dark, at_home, security_armed, door_open)
        for action in actions:
            print(action)
    except ValueError as e:
        print(f"Error: {e}")
main()
