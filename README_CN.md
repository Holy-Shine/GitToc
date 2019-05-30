<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg?style=flat-square"></a> <a href='https://pytorch.org/'><img src='https://img.shields.io/badge/python-3.5-green.svg?style=flat-square'></a> [![HitCount](http://hits.dwyl.io/Holy-Shine/GitToc.svg)](http://hits.dwyl.io/Holy-Shine/GitToc)

# GitToc

为你的Github仓库的Readme自动生成一个目录

[English readme](README.md)

## 简介

如下是转换效果：

<img src='effect.png' width=70%>

转换后的目录支持页内跳转

## 使用教程

假设你的目标文件名为 `targetFile.md`. 在你的命令行下键入下面命令即可:

 ```shell
> python gitToc.py targetFile.md
 ```

你会在你的当前目录下获得一个名为 `targetFile_with_toc.md` 的文件