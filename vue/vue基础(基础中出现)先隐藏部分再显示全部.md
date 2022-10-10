### **前言**
<font color=#000 size=2     face="黑体">总结下以前项目中经常使用到的一些vue基础方面的小技术，分享给自己和网上的朋友</font>
###### 如下项目中的截图<点击某个时间，比如 织造一车间的白班6点到18点，能够查看全部的截图>
![](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/6/1/16b10b0074229cea~tplv-t2oaga2asx-image.image)
```
当页面加载时，会将部分隐藏起来，只显示前5条数据

代码如下（用的框架是vue的vux）
1  <group v-for="(item,index) in newResult":key="index" :title="item.workshop_name">
2            <cell value-align="left"v-for="(n,j) in item.data":title="n.index_key"is-link class="islink1">
3                <span v-if="n.product"v-html="n.showAll ? n.product.split(',').join('<br>') :
4                n.product.split(',').slice(0,5).join('<br>')"
5                      @click="$router.push('/output/machine/'+item.workshop_id+'/'+n.shift_key)" class="islink2"></span>
6              <a class="voida" href="javascript:void(0)" @click="switchShow(index,j,n)" v-if="n.product">{{n.showAll ? '关闭显示' : '显示全部'}}</a>
7            </cell>
8 
9       </group>
复制代码
```
当页面加载完之后，会点击显示全部按钮的时候，显示所有

![](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/6/1/16b10b063da44479~tplv-t2oaga2asx-image.image)
```js
computed:{
    newResult(){
      var data = this.result;
      if(data.length){
        data.forEach((n,i)=>{
           // n是对象 i是数字
          if(n.data.length){
            n.data.forEach((m,j)=>{
              // m是对象 j是数字
              if(!('showAll' in data[i].data[j])){
                data[i].data[j].showAll = false;
              };
            });
          };
        });
      };
      return this.result
    }
  },
  点击 操作
  methods:{
    switchShow(index,secIndex,item){
      this.$set(this.newResult[index].data[secIndex],'showAll',!item.showAll);
      var temp = [].slice.call(this.newResult);
      for(let i = 0; i < temp.length;i++){
        this.$set(this.newResult ,i, temp[i]);
      }
    },
```
### <font color=#000 size=4 face="黑体">小结</font>
###### 1.针对vue基础方面的知识点进行回顾
###### 2.针对vue中计算属性，$set方面所使用的知识点进行巩固，
###### 3.针对js中[【优雅代码】深入浅出 妙用Javascript中apply、call、bind](https://www.cnblogs.com/coco1s/p/4833199.html)一个简单的应用
### <font color=#000 size=4 face="黑体">最后</font>
###### 下次见!!!!
