# Generic Collection Contributing Guide

This is a collection of generic Icestudio components.

## Project Structure

* `blocks\`: contains the *Icestudio* blocks with the extension **.ice**
* `examples\`: contains the *Icestudio* examples with the extension **.ice**
* `locale\`: contains the translations files for the collection:
  * `translation.js`: contains all the texts to translate
  * `en\`: contains the **.po** files for the English translation
  * `es_ES\`: contains the **.po** files for the Spanish translation

## Development Setup

In order to simplify the collection development we recommend to use the [icm (icestudio collection manager)](https://github.com/FPGAwars/icm) tool:
* [icm update](https://github.com/FPGAwars/icm/wiki#icm-update): this command is used to update the **README.md** file and to **extract the texts** from the collection
* [icm validate](https://github.com/FPGAwars/icm/wiki#icm-validate): this command check if the **collection is valid**

## Contribute

### Add blocks

Add your blocks in the `blocks` directory. You can also add more directories in order to categorize the blocks.

NOTE: be sure that you blocks have proper *Project Information* (name, version, description, author and SVG image).

### Add examples

Add your examples in the `examples` directory. You can also add more directories in order to categorize the examples.

NOTE: examples do not require the SVG images in *Project Information*.

### Add translations

After adding or updating the blocks/examples run `icm update` to extract the texts to be translated.

Now you can update the existing translations by opening the **PO files** with [Poedit](https://poedit.net/) and loading the updated `locale/translations.js` file:
1. Open the PO file with Poedit
2. Press "Update" to update from sources

You can also add new languages creating new directories in `locale` with its correspondant PO files.

Before updating the translations execute again `icm update` to update the *Languages* section in the README.md file.

## Attributions

If you **add blocks or examples**, please add yourself to the **authors** section in the *package.json* file.

If you **add translations** or **update blocks or examples**, please add yourself to the **contributors** section if you are not already in the authors section.

Finally, execute `icm validate` and `icm update` to ensure that your changes are valid and the documentation is updated. Now you can create a **Pull Request** from a *feature branch* to *master*.
