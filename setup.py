from setuptools import setup , find_packages 


HYPEN_DOT = "-e ."

def get_requirements(requirements_file):

    with open(requirements_file) as f:
        data = f.readlines()
        data = [i.replace("\n", "") for i in data]

        if HYPEN_DOT in data:
            data.remove(HYPEN_DOT)
        
    return data 


setup(
    name = "Random_Project",
    version = "0.0.1",
    author = "BOT",
    author_email = "phewpheww123@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)
