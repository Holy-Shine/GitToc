<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg"></a> <a href='https://pytorch.org/'><img src='https://img.shields.io/badge/python-3.5-green.svg'></a>

# GitToc

Generate a Readme toc for your Github repository.

[中文版](README_CN.md)

## Glimpse

This simple script can parse your markdown file and generate a Toc like this:

<img src='effect.png' width=70%>

This generated toc supports inner page jumping.

## Usage

Assuming that your target file's name is `targetFile.md`. Just type this command in shell:

 ```shell
> python gitToc.py targetFile.md
 ```

You will get a new markdown file named `targetFile_with_toc.md` in current directory.  



