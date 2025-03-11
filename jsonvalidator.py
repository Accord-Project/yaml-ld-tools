import json
import os
import sys
import jsonschema

def validator(input_file, schema_file):
    # Read schema
    file = open(schema_file, 'r')
    schema = json.load(file)

    # Read data
    data_file = open(input_file, 'r')
    data = json.load(data_file)

    try:
        jsonschema.validate(data, schema=schema)
        print("JSON-LD data is valid.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print("JSON-LD data is invalid.")
        print(e)
        return False

def main():
    args = sys.argv[1:] # -a to use in GitHub actions

    if '-a' in args:
        input_path = 'thamer-experiments/jsonvalidator_data/'
        schema_path = 'thamer-experiments/schema_files/'
    else:
        input_path = 'jsonvalidator_data/'
        schema_path = 'schema_files/'

    # get a list of all files in the input dir 'jsonvalidator_data'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        schema_file = schema_path + 'schema'

        # Convert JSON to YAML
        print('The input file: ', input_file, '\n')
        valid = validator(input_file, schema_file)
        print('\n------------------------------')


if __name__ == '__main__':
    main()