# Home

*imcon* is an application used to control scientific imaging systems. It is based on the *azcam* image acquisition and analysis package.

## Installation

### imcon

`pip install imcon`

The latest version of the imcon package is located on GitHub at <https://github.com/mplesser/imcon.git>

## AzCam

See the [azcam documentation](https://azcam.readthedocs.io) for all things azcam related.

## Usage

A configuration file is required to configure imcon at start up. It is specified with a full pathname and does not need to be in an installed python package. Startup examples are:

```python
imcon <full_path_to_config_file> -- <options>
or
python -m <full_path_to_config_file> -- <options>
```

Example:
```python
imcon /data/90prime/code/pf_config.py -- -normal
```

After initiialization imcon provides an embedded IPython shell which is used for all local operations. The *tools* object is exposed to provide access to all azcam tools.

## Examples

```python
instrument = tools["instrument"]
exposure = tools["exposure"]
instrument.set_wavelength(450)
wavelength = instrument.get_wavelength()
print(f"Current wavelength is {wavelength}")
exposure.expose(2., 'flat', "a 450 nm flat field image")
```

## Help
Help is available by typing `?xxx`, `xxx?`, `xxx??` or `help(xxx)` where `xxx` is an class, command, or object instance.

## External Links

Useful external links include:
  
 * IPython <https://ipython.org>
 * Python programming language <https://www.python.org>
