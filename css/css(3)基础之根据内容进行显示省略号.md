### **前言**
<font color=#000 size=2     face="黑体">总结下项目中经常使用到的一些css基础方面的小技术，分享给自己和网上的朋友</font>
需设置宽度才能溢出显示省略号。 
###  <font color=#000 size=3 face="黑体">单行文本：</font>
```css
selector {
    word-wrap: normal; /* for IE */
    text-overflow: ellipsis;    //当文本溢出显示省略符号来代表被修剪的文本。
    white-space: nowrap;  //规定段落中的文本不进行换行
    overflow: hidden;
}
　　

word-wrap: normal / break-word; 
normal 只在允许的断字点换行（浏览器保持默认处理）。 
break-word 在长单词或 URL 地址内部进行换行。

```

![省略号](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/7/12/16be1ddd1c243f57~tplv-t2oaga2asx-image.image)

 
###  <font color=#000 size=3 face="黑体">多行文本：</font>

```css
selector {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
}
要将height设置为line-height的整数倍，防止超出的文字露出。
```

![省略号](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/7/12/16be1de6bd2c756a~tplv-t2oaga2asx-image.image)
[来源:CSS实现单行，多行文本溢出显示省略号（...）](http://www.daqianduan.com/6179.html)
### <font color=#000 size=4 face="黑体">最后</font>
###### 下次见!!!!
