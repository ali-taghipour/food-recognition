import yaml


labels_file_path = 'category.txt'
output_yaml_path = 'config.yaml'


with open(labels_file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

label_names = []
for line in lines:
    if line.strip():  # Skip empty lines
        parts = line.strip().split('\t')
        if len(parts) == 2:
            label_names.append(parts[1])

yaml_dict = {
    'names': str(label_names)
}

def represent_list(dumper, data):
    return dumper.represent_sequence(u'tag:yaml.org,2002:seq', data, flow_style=True)

yaml.add_representer(list, represent_list)

with open(output_yaml_path, 'w', encoding='utf-8') as f:
    yaml.dump(yaml_dict, f, default_flow_style=None, allow_unicode=True)

print(f"YAML configuration file created at: {output_yaml_path}")