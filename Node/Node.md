# Setup

nvm is a tool for managing Node.js versions on your operating system. It allows for easy switching between different Node.js versions and managing packages for each version.

To install nvm on a Linux or macOS system, you can use the following command:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

## Menaging 

After installing nvm, you can install a specific version of Node.js using the command:

nvm install <version>

where <version> is the Node.js version number, e.g. 14.17.6. You can also set a default Node.js version for your system using the command:

```nvm alias default <version>``  


To check which Node.js versions are installed using nvm, you can use the command:

```nvm ls```

This will return a list of installed Node.js versions, with the currently active version highlighted.
