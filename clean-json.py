import json
import re

ORIGINAL_FILE_PATH = 'results.json'
OUTPUT_FILE_PATH = 'sanitised_gitleaks_output.json'

ignore_these = [
    'Enumerating objects',
    '] cloning ',
    'pack-reused',
    'leaks detected',
    'recovering from panic on commit',
    'cloning:',
    'error occurred during audit of repo:'
]
#find junk lines to remove
with open(ORIGINAL_FILE_PATH, 'r') as original_output:
    content_as_lines = original_output.readlines()
    removing = []
    for line in content_as_lines:
        for i in ignore_these:
            if i in line:
                removing.append(line)
                break

    for r in removing:
        content_as_lines.remove(r)
#transform to actual json
    with open(OUTPUT_FILE_PATH, 'w') as output_cleaned:
        output_cleaned.write('[')
        for line in content_as_lines:
            if line.startswith('}') and line is not content_as_lines[-1]:
                output_cleaned.write(line.replace('}', '},'))
            else:
                output_cleaned.write(line)
        output_cleaned.write(']')

with open(OUTPUT_FILE_PATH, 'r') as json_file:
    json_content = json.load(json_file)