from setuptools import setup, find_packages
 
setup(
    name='docker-port-introspect',
    version='0.1.0',
    description="""Docker API (socket) wrapper to get ports inside of a container.
        Plus serf -tags to expose mapped 49XXX ports""",
    author='Vladimir Shulyak',
    author_email='vladimir@shulyak.net',
    url='http://shulyak.net/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts = [
        'docker_port_introspect/docker-port-introspect'
    ],
    install_requires=['docker-py>=0.3.2']
)