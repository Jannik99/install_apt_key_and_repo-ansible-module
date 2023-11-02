#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import subprocess


def run(command):
    result = {}
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        result['stdout'] = output
        result['changed'] = True
    except subprocess.CalledProcessError as e:
        result['stderr'] = str(e)
        result['failed'] = True

    return result


def main():
    module = AnsibleModule(
        argument_spec=dict(
            key_url=dict(required=True, type='str'),
            repo_url=dict(required=True, type='str'),
            distribution_codename=dict(required=True, type='str'),
            repo_name = dict(required=True, type='str')
        )
    )

    key_url = module.params['key_url']
    repo_url = module.params['repo_url']
    codename = module.params['distribution_codename']
    repo_name = module.params['repo_name']

    commands = [
        f"curl {key_url} | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/apt.custom_key.gpg >/dev/null",
        f"sudo sh -c 'echo \"deb {repo_url} {codename}-{repo_name} main\" > /etc/apt/sources.list.d/{repo_name}.list'",
        "sudo apt update"
    ]

    results = []
    for command in commands:
        result = run(command)
        results.append(result)

    module.exit_json(results=results)


if __name__ == '__main__':
    main()
