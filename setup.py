import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()


setuptools.setup(
	name='genny',
	version='1.1',
	scripts=['genny'],
	author='Ian Moncrieffe',
	author_email="dev.bitone@outlook.com",
	description="A Unique Id Generator utility"
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/BitOneInc/genny",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Licence :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		],
)
		
