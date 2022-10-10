####

遇到了一个场景，当在浏览器(pc)上面按f5之类刷新 页面时，如果底部的tarbbar是自定义的话，会回到默认的第1个，解决方案如下:

[beforeRouteEnter文档说明](https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#%E8%B7%AF%E7%94%B1%E7%8B%AC%E4%BA%AB%E7%9A%84%E5%AE%88%E5%8D%AB)

```
  //利用vuerouter中的api方法监听页面是否在刷新操作
  beforeRouteEnter(to, from, next) {
    next(vm=>{
      vm.tabbarList.filter((item,index)=>{
        if(item.path===to.fullPath){
          vm.currentItem = index
          vm.currentPath = to.fullPath
        }
      })
    })
  },
```

注意:在beforeRouteEnter中，无法直接使用this方法，如果使用，则报错，请在next()方法中传入一个参数，去处理vue实例中的变量，方法等，解决方案就在上面的代码中。

记录下，以方便未来的检阅
