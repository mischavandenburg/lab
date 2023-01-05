from applications_dict_file import applications
import yaml

# opens a file containing a large dictionary and converts it to a yaml file

data = applications

# Open a file for writing
with open("data.yaml", "w") as file:
    # Convert the dictionary to YAML and write it to the file
    yaml.dump(data, file)
