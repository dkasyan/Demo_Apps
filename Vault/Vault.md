# Setup

nvm is a tool for managing Node.js versions on your operating system. It allows for easy switching between different Node.js versions and managing packages for each version.

To install nvm on a Linux or macOS system, you can use the following command:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

## Enginess

- KV : this is storage key-value
- PKI : certificates - sign certs as CA authority
- SSH : ssh
- Transit : Cryptography
- TOTOP : time-based one time password. When we want add permisions for houers

## How connect

Vault need two local vaules like `export VAULT_ADD="http://serwer.com:80"` and `export VAULT_TOKEN="hvs.dfhni3fsjnbfdk"`  
If we want need check serwer status or parms we must use `vault status` then we shoud get info like:
```Key                    Value
---                    -----
Seal Type              shamir
Initialized            true
Sealed                 false
Total Shares           3  <-------this is info about users
Threshold              2
Version                1.1.2
Build Date             2023-03-02T18:32:37Z
Storage Type           consul
Cluster Name           vault-cluster_name
Cluster ID             2ced33ae-a8d2-fbvy834bhf2b16-c236d3dsad
HA Enabled             true
HA Cluster             https://192.168.1.4:8301
HA Mode                standby
Active Node Address    https://192.168.1.5:8300
```

## How download list of secrets
