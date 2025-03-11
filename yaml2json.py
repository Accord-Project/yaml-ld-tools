import json
import os
import sys

import yaml

def yaml2json(yaml_file, json_file, save):

    with open(yaml_file, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        yaml_file.close()

    if save:
        with open(json_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            json_file.close()

    return json.dumps(data, indent=4)


def main():
    args = sys.argv[1:] # -s to save the output as a file, -a to use in GitHub actions

    if '-a' in args:
        input_path = 'thamer-experiments/yaml2json_data/input/'
        output_path = 'thamer-experiments/yaml2json_data/output/'
    else:
        input_path = 'yaml2json_data/input/'
        output_path = 'yaml2json_data/output/'

    # get a list of all files in the input dir 'yaml2json_data/input'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        output_file = output_path + file[:file.find('.')] + '.jsonld'

        # Convert JSON to YAML
        json_data = yaml2json(input_file, output_file, '-s' in args)
        print('The input file: ', input_file, ' converted to:\n', json_data, '\n------------------------------')



    # json_file = "yaml2json_data/output.jsonld"
    # yaml_file = "yaml2json_data/input.yaml"
    #
    # # Convert JSON to YAML
    # yaml2json(yaml_file, json_file)


if __name__ == '__main__':
    main()