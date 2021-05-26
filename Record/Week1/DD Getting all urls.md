# Python爬虫如何提取当前页面的所有url链接

在Python中可以使用urllib对网页进行爬取，然后利用Beautiful Soup对爬取的页面进行解析，提取出所有的URL。



## Beautiful Soup

-----

Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。

BeautifulSoup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快。



## 一些待看懂的代码

------

![image-20210526225707743](C:\Users\DingHan\AppData\Roaming\Typora\typora-user-images\image-20210526225707743.png)



## 备注

-----

有用到最后一节课ppt里的内容，应该还是需要看看的