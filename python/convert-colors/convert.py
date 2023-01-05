import yaml

# Load the YAML file
with open('old_colors.yaml', 'r') as f:
    colors = yaml.safe_load(f)

# Loop through the colors and convert them to hexadecimal
for color_group, color_values in colors['gruvbox_material'].items():
    for color_name, color_code in color_values.items():
        # Convert the color code to an integer
        color_int = int(color_code, 16)
        # Convert the integer to hexadecimal and add the '#' symbol
        color_hex = '#{:06x}'.format(color_int)
        # Update the color code in the YAML file
        color_values[color_name] = color_hex

# Save the updated YAML file
with open('new_colors.yaml', 'w') as f:
    yaml.dump(colors, f)
