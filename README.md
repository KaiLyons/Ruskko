# Ruskko
HTML for lazy people.

## What is Ruskko?
Ruskko is an HTML Framework that translate a Ruskko file (`.rsko`) to a usable HTML file. \
The goal of Ruskko is to make it easier to create websites of all forms.

## Ruskko dependancies:
- Python 3.7.5 or higher

Otherwise you don't need anything else, Ruskko does not use external dependancies, only what is inside of Python 3 itself.

## How Ruskko Works: 
It is a non-installed program, and this is only because the Linux and BSD installers will be set up for the 1.0 release. The only way to run it, on all platforms, is to use Python 3.7.5 or higher.

Here is the command usage for Ruskko: \
`python3 ruskko.py [filename] [option] [command]`

Here are all the allowed command form examples: \
- `python3 ruskko.py index.rsko` - Create a normal index.html file
- `python3 ruskko.py index.rsko -o mypage` - Turns index.rsko into mypage.html
- `python3 ruskko.py index.rsko -of textfile.txt` - Turns index.rsko into any form of file wanted keeping html syntax
- `python3 ruskko.py -help` - Displays the help information

## Planned Features
- Custom Ruskko tags (will have many by 1.0 release)
- Different ID / Class syntax
- Easy <meta> tags

## Desired Features
These might be scrapped as ideas but they will be documented.
- CSS support based on Sass
- Bulma support
