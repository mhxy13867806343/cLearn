### if语句转&&方式

```
#遇到简单的当如下的修改
if (code === 200) {
this.joinList = result.slice(0, 99)
  this.getList()
}
#可以转换为
this.joinList=code===200&& result.slice(0, 99)
code===200&& this.getList()
```

### [] or {} => null (永远不要相信后端返回的数据)

```
const { data } = await getApiData()

// 如果data类型是一个数组
console.log(data[0]) // 如果data返回了个null，会报错

// 如果data类型是一个对象
console.log(data.a) // 如果data返回了个null，会报错

// 可以写成下面这样
console.log((data || [])[0])
console.log((data || {}).a)
console.log(data?.a)
console.log(data?.[0])
// 此时就算data返回了null，也只会提示undefined，并不会报错阻塞代码
```

### 生成指定长度的数字数组

```
const isArray100=(n=100)=>[...Array(n).keys()]
```

### 生成A-Z数组

```
[...Array(91).keys()].filter(i=>i>64).map(i=>String.fromCharCode(i))
 [...Array(26).keys()].map(i => String.fromCharCode(i+65))
```

### 取整

```
console.log(123.456||0)
```

### 万能reduce

#### 11.通过reduce方法去重

```
const arr = [
    {
        id:'1',
        msg:''
    },
    {
        id:'2',
        msg:''
    },
    {
        id:'1',
        msg:''
    }
]

const preduce=arr.reduce((p,n)=>{
    if(!p.find(i=>i.id ===n.id))p.push(n)
    return p

    
},[])
console.log(preduce)
```
