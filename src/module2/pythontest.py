import json
from pathlib import Path
project_root=Path(__file__).resolve().parents[2]
config_file=project_root/'config'/'config1.json'
with open(config_file,'r') as f:
    config=json.load(f)
print('application:',config['application'])
print('environment:',config['environment'])
print('timeout:',config['timeout'])