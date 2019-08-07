<h3 align="center">Arcli</h3>

<div align="center">

  [![GitHub Issues](https://img.shields.io/github/issues/guiscaranse/arcli.svg)](https://github.com/guiscaranse/arcli/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/guiscaranse/arcli.svg)](https://github.com/guiscaranse/arcli/pulls)
  [![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Arcli is a lightweight cross-platform builder inspired by TravisCI. It can automate deploying aplications with a single command line, and is highly extensive.
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage and definitions](#usage)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)

## 🧐 About <a name = "about"></a>
Arcli started as a hobby and quickly evolved into something incredibly useful that I implement in my daily life. With Arcli you can write code routines to be executed at the time of a deployment, as well as optional steps that can be triggered by certain conditions.

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing
You can install Arcli using pip 

```sh
pip install arcli
```

or by downloading one of our pre-compiled binaries.

```sh
# Download
wget https://github.com/guiscaranse/arcli/releases/latest/download/arcli-linux_arm64.tar.gz
# Extract
tar arcli-linux_arm64.tar.gz
# Make executable
chmod u+x arcli
```

Start using it or add it to your `PATH` 

```sh
arcli run
```

## 🎈 Usage and Definitions <a name="usage"></a>
Arcli will try to find and read an Arcli File (`arcli.yml`) where it will parse and run it.

### Arcli File
An Arcli file is an instruction file written in YAML. Arcli will interpret it, perform validations, and thus run the codes described.

Here it is a sample Arcli file (more samples on `samples`).

```yaml
arcli: 0.1
os: linux
dependencies:
  - git
env:
  - TEST=sampleenv
runtime:
  - 'echo Hello World'
  - $step checkgit
  - 'echo Arcli End'
step @checkgit:
  trigger:
    name: GitDiff
    args: ["arcli/*.py"]
  script:
    - 'echo Python Files Modified'
```

#### Arcli file definitions

| Key          | Type  | Optional | Description                                                                                                      |
|--------------|-------|----------|------------------------------------------------------------------------------------------------------------------|
| arcli        | float | No       | Refers to the version of Arcli that that file was made, it is possible to use Semantic Versioning for this field |
| os           | str   | Yes      | Which operating system this file was made to run [`linux`, `osx`, `windows`, `any` (default)]                    |
| dependencies | list  | Yes      | Which executables this file will need to use                                                                     |
| env          | list  | Yes      | List of environment variables that will be injected at runtime.                                                  |
| runtime      | list  | No       | List of main commands to be executed by Arcli. You can reference steps using `$step [step name]`                 |

#### Step and Triggers definitions
Steps are separate blocks of code that can be executed under certain circumstances when triggered by Triggers.

This is how a step look like:

```yaml
step @checkgit:
  trigger:
    name: GitDiff
    args: ["arcli/*.py"]
  script:
    - 'echo Python Files Modified'
```

| Key     | Type | Optional | Description                                                                                                                                           |
|---------|------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| step    | str  | No       | It will be used to refer to the step in the runtime, you must name it after the @. Example: `step @mystep`                                            |
| trigger | obj  | Yes      | Not all steps need to have a trigger, in the absence of a trigger it will always be executed. You can see the triggers available in `arcli/triggers`. |
| script  | list | Yes      | Code to be executed if the step is valid (trigger is triggered or trigger is missing)                                                                 |

This is how a trigger looks like:

```yaml
trigger:
  name: GitDiff
  args: ["arcli/*.py"]
  options:
    autopull: true
```

| Key     | Type | Optional | Description                                                                    |
|---------|------|----------|--------------------------------------------------------------------------------|
| name    | str  | No       | It will be used to identify the trigger, it must be the same as the class name |
| args    | list | Yes      | Arguments that can be passed at the time of executing the trigger              |
| options | obj  | Yes      | Advanced options that can contain keys and values to be passed to the trigger  |

Triggers documentation can be found in each respective trigger file.


## ⛏️ Built Using <a name = "built_using"></a>
- [Python](https://www.python.org/) - Python
- [Click](https://click.palletsprojects.com/en/master/) - CLI Framework
- [Nuitka](http://nuitka.net) - Binaries generator