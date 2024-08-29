import platform

packages=[
    # for checking my shell scripts
    "shellcheck",
    # for checking spelling
    "aspell",
    # ruby stuff
    "ruby-bundler",
    "rbenv",
]

desktop = platform.freedesktop_os_release()
VERSION_ID = desktop["VERSION_ID"]

if VERSION_ID == "24.04":
    # the right package for docker compose
    packages.append("docker-compose-v2")

packages_remove = []

if VERSION_ID == "22.04":
    # because of conflict with containerd which is needed by "docker.io" below
    packages_remove.append("containerd.io")
if VERSION_ID == "24.04":
    # because of conflict with containerd which is needed by "docker.io" below
    packages_remove.append("containerd.io")
