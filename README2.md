# Refer to:

[447ae7b](https://github.com/NVlabs/curobo/commit/447ae7b777cb156f1c63c731cdb9d604884b2754)


# link isaac sim to this repo:

```bash
./link_app.sh --path <path to your isaac sim 4.5>

## e.g.
# ./link_app.sh --path /home/yizhou/Desktop/isaac-sim
```

# reinstall torch
```bash
./app/python.sh -m pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

# install curobo
```bash
./app/python.sh -m pip install -e ".[isaacsim]" --no-build-isolation
```

# (Optional) Pytest
```bash
./app/python.sh -m pip install pytest
./app/python.sh -m pytest ./tests/
```
# Edit the version function 

(line 52): `src/curobo/__init__.py`

# install lxml in isaac-sim script editor
omni.kit.pipapi.install(
    "lxml"
)