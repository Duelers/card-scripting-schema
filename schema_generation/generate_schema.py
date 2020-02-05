import effects

if __name__ == '__main__':
    schema_root = effects.TriggeredEffect  # In future change this as the scope increases.
    schema_json = schema_root.schema_json(indent=4)
    file_name = 'duelers_schema'
    version = '0_1'
    with open(f'../schema_exports/{file_name}_{version}.json', 'w+') as file:
        file.write(schema_json)
