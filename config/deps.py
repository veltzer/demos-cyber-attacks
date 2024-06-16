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
