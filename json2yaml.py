import json
import os
import sys

import yaml

def json2yaml(json_file, yaml_file, save):

    # Read json
    file = open(json_file, 'r')
    json_data = json.load(file)
    # print(json_data)

    # convert to yaml
    yaml_string = yaml.dump(json_data)
    # print('The YAML file is:')
    # print(yaml_string)
    file.close()

    if save:
        # Write yaml
        fileOut = open(yaml_file, 'w')
        fileOut.write(yaml_string)
        fileOut.close()

    return yaml_string


def main():
    args = sys.argv[1:] # -s to save the output as a file, -a to use in GitHub actions

    if '-a' in args:
        input_path = 'thamer-experiments/json2yaml_data/input/'
        output_path = 'thamer-experiments/json2yaml_data/output/'
    else:
        input_path = 'json2yaml_data/input/'
        output_path = 'json2yaml_data/output/'

    # get a list of all files in the input dir 'json2yaml_data/input'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        output_file = output_path + file[:file.find('.')] + '.yaml'

        # Convert JSON to YAML
        yaml_string = json2yaml(input_file, output_file, '-s' in args)
        print('The input file: ', input_file, ' converted to:\n', yaml_string, '\n------------------------------')


if __name__ == '__main__':
    main()