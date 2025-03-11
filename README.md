# yaml-jsonld-turtle_pipeline
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [yaml-jsonld-turtle_pipeline](#yaml-jsonld-turtle_pipeline)
    - [Intro](#intro)
    - [Requirements for Local Use](#requirements-for-local-use)
    - [Setup Github Pipeline Actions](#setup-github-pipeline-actions)
    - [Use Github Pipeline Actions](#use-github-pipeline-actions)

<!-- markdown-toc end -->

## Intro

This directory contains the following coverters:
- json2yaml
- jsonld2turtle
- turtle2jsonld
- yaml2json
- yaml2turtle

And the following validators:
- jsonvalidator
- yamlvalidator

## Requirements for Local Use

- Python 3.7+
- Run `pip install -r requirements.txt` to install the requirements (`pyyaml` and `rdflib`)

## Setup Github Pipeline Actions

1. Begin by forking the repository.
2. Activate the Actions feature for the repository under the 'Action' tab
3. Locally clone the project.

## Use Github Pipeline Actions
1. Place the files that need conversion or validation into their respective directories, such as `json2yaml_data/input` to convert json to yaml, `jsonld2turtle_data/input` to convert jsonld to turtle, and so on.
2. Commit and push the changes to directory `thamer-experiments` for example `git add thamer-experiments/`.  (Please note that the defined GitHub actions will only be triggered if you push to this directory or any of its sub-directories.)
3. The transformed file content or the validation output will be accessible in the action's log, for example:

```
Run jsonld2turtle to convert all files in 'jsonld2turtle_data/input'

Run python3 json2yaml.py

The input file:  json2yaml_data/input/test1.jsonld  converted to:
 '@context':
  '@vocab': http://schema.org/
  countries: http://publication.europa.eu/resource/authority/country/
'@graph':
- '@id': countries:ITA
- '@id': http://people.example/Homer
  country:
    '@id': countries:ITA
  full_name: Homer Simpson
- '@id': http://people.example/Lisa
  country:
    '@id': countries:ITA
  full_name: Lisa Simpson
```
