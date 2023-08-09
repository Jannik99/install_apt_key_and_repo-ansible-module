# Ansible Module: install_apt_key_and_repo

The Ansible module `install_apt_key_and_repo` allows for easy installation of an APT key and addition of an APT repository on a target host.
This was tested and created on Ubuntu 22 with and for the repository of PostgreSQL. If it works on other repositories thats nice, if not it may or may not be added in future.
You are welcome to extend the module and make pull requests.

## Prerequisites

- A supported operating system using APT (Advanced Package Tool).

## Parameters

- `key_url`: URL of the APT key to be imported. Required.
- `repo_url`: URL of the APT repository to be added. Required.
- `distribution_codename`: The distribution's codename (e.g., `jammy`, `buster`). Required.

## Example

```yaml
- name: Install Custom Repository and Key
  hosts: your_target_hosts
  tasks:
    - name: Add apt key and repository for postgres
      install_apt_key_and_repo:
        key_url: "https://www.postgresql.org/media/keys/ACCC4CF8.asc"
        repo_url: "http://apt.postgresql.org/pub/repos/apt"
        distribution_codename: "jammy-pgdg" # Replace with your distribution's codename
```

## Notes

- Ensure the provided key_url and repo_url are valid and reachable.
- Verify the distribution_codename against your operating system version.
- Run the Ansible playbook under a user with sufficient permissions

## Supported Operating Systems

The module has been tested on the following operating systems:

- Ubuntu 22.04 (Jammy Jellyfish)

## License

This Ansible module is licensed under the [MIT License](https://opensource.org/license/mit/).
