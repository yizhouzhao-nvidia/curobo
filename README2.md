# Problems [Until April 17th 2024]:

1. [Curobo] Fix Curobo to support Isaac Sim 4.5.0 
    - Status: ![](https://img.shields.io/badge/Fixing%20in%20progress-1A2BE2) 
    - Solution: ![](https://img.shields.io/badge/Can%20walk%20around-8A2BE2) [see this](#solution-to-isaac-sim).

2. [Ur5e example](https://forums.developer.nvidia.com/t/curobo-ur5e-example/308613) joint velocities pretty noisy
    - Status: ![](https://img.shields.io/badge/Under%20examination-9A9B12)
    - Solution: ![]

3. [Robotiq Gripper Issue](https://github.com/isaac-sim/IsaacLab/issues/1600)
    - Status: ![](https://img.shields.io/badge/Closed-112233)  

# Solution to Isaac-Sim

## References:
- [A commit from JonathanKuelz: 447ae7b](https://github.com/NVlabs/curobo/commit/447ae7b777cb156f1c63c731cdb9d604884b2754)

![test](https://img.shields.io/badge/any_text-you_like-blue)

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