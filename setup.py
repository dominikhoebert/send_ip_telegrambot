from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.read().splitlines()

setup(
    name='sendipbot',
    version='0.1',
    py_modules=['sendipbot'],
    #packages=find_packages(),
    install_requires=requirements,
    entry_points={  # Optional: If you want to make your script executable via command line
        'console_scripts': [
            'sendipbot=sendipbot:send_ip_address',  # Replace with 'command-name=module:function' if you have a main() function
        ],
    },
)
