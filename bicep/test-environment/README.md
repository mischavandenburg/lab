# Quick AKS Test Environment

This script and templates deploy a cheap AKS cluster in a newly created resource group.

## Requirements

* bash shell
* [ripgrep](https://github.com/BurntSushi/ripgrep)

## Usage

1. az login
2. az account set -s mysubscriptionid
3. `./setup`
4. Do your thing on your newly created cluster
5. To clean up your mess, run `./setup --delete`
