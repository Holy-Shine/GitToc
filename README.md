<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg?style=flat-square"></a> <a href='https://pytorch.org/'><img src='https://img.shields.io/badge/python-3.5-green.svg?style=flat-square'></a> ![](https://img.shields.io/badge/platform-windows-lightgrey?style=flat-square) [![HitCount](http://hits.dwyl.io/Holy-Shine/GitToc.svg)](http://hits.dwyl.io/Holy-Shine/GitToc)

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



## Platform

- **Windows**

  This simple script has been packed into windows PE file(.exe) within [release version](https://github.com/Holy-Shine/GitToc/releases/tag/v1.0.0) by [pyinstaller](https://pypi.org/project/PyInstaller/). Now you can click `gitToc_GUI.exe` directly and do transformation job in your Windows PC.



## Online Usage

The author [@lzw5399](https://github.com/lzw5399) made an online conversion tool **TocGenerator** based on GitToc.

TocGenerator Github link: https://github.com/lzw5399/TocGenerator

Online conversion address: [https://toc.codepie.fun/](https://toc.codepie.fun/)

**Instructions:**

![](online.gif)