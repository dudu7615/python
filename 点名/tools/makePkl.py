from pathlib import Path
import pickle
import yaml

file = Path("点名/data/yaml/2.yml")
names:list = yaml.load(file.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
print((len(names)))
with open(file.parent.parent/"pkl"/f"{file.name}.pkl", "wb") as f:
    pickle.dump(names, f)