from setuptools import setup

package_name = 'icksu_homework1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='icksu',
    maintainer_email='icksu@todo.todo',
    description='ROS2 package for homework, includes publisher and subscriber nodes.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'icksu_publisher = icksu_homework1_pkg.icksu_publisher:main',
            'icksu_subscriber = icksu_homework1_pkg.icksu_subscriber:main',
        ],
    },
)

