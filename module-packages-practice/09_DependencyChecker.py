# Question:
# Problem 9: Dependency Version Checker
# Check installed package version.

from importlib.metadata import version, PackageNotFoundError

def check_version(pkg):
    try:
        v = version(pkg)
        print(pkg, "version", v, "is installed.")
    except PackageNotFoundError:
        print(pkg, "is not installed.")

# input
pkg = input("Enter package name: ")
check_version(pkg)