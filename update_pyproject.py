import os
import toml
import argparse
import subprocess

# Make sure to use absolute path when calling the script from different places
ABS_PATH = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = "pyproject.toml"

# Create the parser to use the script with ou without a flag
parser = argparse.ArgumentParser(description="Update pyproject.toml")
parser.add_argument(
    "-c",
    "--config",
    help="pyproject.toml config file",
    required=False,
    default=os.path.join(ABS_PATH, CONFIG_FILE),
)
args = parser.parse_args()


def update_pyproject_dependencies(path: str) -> None:
    """
    Reads the dependencies from a `pyproject.toml` file, updates them
    with the output of `pip freeze`, and writes the updated data back to the file.

    :param path: Path to the `pyproject.toml` file.
    :return: None
    """

    with open(path, "r") as file:
        pyproject_data = toml.load(file)

    dependencies = pyproject_data["project"]["dependencies"]

    # Get updated dependencies from `pip freeze`
    frozen_dependencies = subprocess.check_output(["pip", "freeze"]).decode("utf-8")

    # Update dependencies in pyproject.toml
    dependencies.clear()
    for line in frozen_dependencies.splitlines():
        package, version = line.split("==")
        print(f"{package}=={version}")
        dependencies.append(f"{package}=={version}")

    # Write updated data back to the file
    with open(path, "w") as file:
        toml.dump(pyproject_data, file)


def __init__():
    update_pyproject_dependencies(args.config)
