import os
import sys

import yaml
from rdflib import Graph, Literal, Namespace, RDF, URIRef

def yaml2turtle(yaml_file, turtle_file, save):
    # Load YAML data
    with open(yaml_file, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    # Create an RDF graph
    graph = Graph()

    # Parse the JSON-LD data into the graph
    graph.parse(data=data, format='json-ld')

    # Serialize the graph to Turtle format
    turtle_data = graph.serialize(format='turtle')
    if save:
        graph.serialize(destination=turtle_file, format='turtle')

    graph.close()

    return turtle_data

def main():
    args = sys.argv[1:] # -s to save the output as a file, -a to use in GitHub actions

    if '-a' in args:
        input_path = 'thamer-experiments/yaml2turtle_data/input/'
        output_path = 'thamer-experiments/yaml2turtle_data/output/'
    else:
        input_path = 'yaml2turtle_data/input/'
        output_path = 'yaml2turtle_data/output/'

    # get a list of all files in the input dir 'yaml2turtle_data/input'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        output_file = output_path + file[:file.find('.')] + '.ttl'

        # Convert YAML to Turtle
        yaml_string = yaml2turtle(input_file, output_file, '-s' in args)
        print('The input file: ', input_file, ' converted to:\n', yaml_string, '\n------------------------------')


if __name__ == '__main__':
    main()