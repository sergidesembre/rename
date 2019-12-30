<h3 align="center">
    sergidesembre/rename
</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/23048749/71590293-2f45a100-2b28-11ea-9ca5-78bb4575852f.gif" alt="sergidesembre/rename" width="80%">
  <br>
  <sub>Rename and copy of files from defined path</sub>
</p>

## Usage
```bash
python main.py ~/photo ~/photo/rename/all
```
You must define the origin path where get files and rename path like destination where store renamed files

#### Optional arguments
```bash
python main.py ~/photo ~/photo/rename/all --filter=jpg,arw
```
With argument **--filter** or **-f** you select by file extension (multiple extensions separated by coma character)
```bash
python main.py ~/photo ~/photo/rename/all --rename-type=default
```
With **--rename-type--** or **-rt** you can define what kind of rename do you prefer (default, numeric, updated_at)

## External Libs
* [plac](https://pypi.org/project/plac/)
* [colored](https://pypi.org/project/colored/)

## License
The GNU General Public License v3.0. Please see [License](LICENSE) for more information.