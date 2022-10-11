### **前言**

\


总结下js的基础知识点，以帮助自己的及别人的回顾

\


let,count,var的区别

| 名称    | 变量是否提升 | 是否支持重复定义 | 是否支持修改操作                       | 是否暂时性死区 | 是否支持块级作用域 | 是否属于全局对象的属性 |
| ----- | ------ | -------- | ------------------------------ | ------- | --------- | ----------- |
| var   | 是      | 是        | 是                              | 否       | 否         | 是           |
| let   | 否      | 否        | 是                              | 是       | 是         | 否           |
| count | 否      | 否        | 否(不支持，当声明后，是不允许修改的，底层带有指针部分内容) | 是       | 是         | 否           |

\


### 变量是否提升

\


```
var a=1 // undefined
b //b is not defined
let b
c;// c is not defined
const c //Uncaught SyntaxError: Unexpected identifier
```

\


### 是否支持重复定义

\


```
x=1
var x=2
let x =3  //Identifier 'x' has already been declaredat <anonymous>
const x //Uncaught SyntaxError: Unexpected identifier
```

\


### 是否支持修改操作

\


```
let x=1
x=3 // 3
var x=1
x=3 // 3
const x5=45
x5=45676 // Assignment to constant variable.
```

\


### 是否暂时性死区

\


##### 当进入当前作用域中，所使用的变量就已存在了，是无法获取到的,只有在专题变量那一行代码出现后，才能正确的获取的使用当前该变量

\


```
  typeof a    // a is not defined
    let a = 'a'
    
    typeof b    // b is not defined
    const b = 'b'
    
    typeof c    // "undefined"
    var c = 'c'
```

\


##### 除了以上的情况外，还有以下情况也属性不能进行重复声明的

\


##### 函数中

\


```
function func(arg){
let arg //SyntaxError: Identifier 'arg' has already been declared
}
```

\


### 是否支持块级作用域

\


##### 除了以上的情况外，还有以下情况也属性不能进行块级作用域的

\


```
function func1(){
let a1;
let a1=2 // Identifier 'a1' has already been declared
}
```

\


##### 除了以上的情况外，只有在es5中存在全局作用域和函数作用域，但没有 块级作用域的情况

\


### 是否属于全局对象的属性

\


```
var a1=2
window.a1 //2

let a2=3
window.a2 // undefined

const  a3=4
window.a3 //undefined
```

\


##### 除了以上的情况外，除了var所声明的变量带有全局对象的属性外,let &count均没有全局对象的属性

\


### 参考

\


###### 来源

\


链接: [ECMAScript 6 入门的let 和 const 命令](http://es6.ruanyifeng.com/#docs/let).

\


### 小结

\


### 本文主要介绍了let、const与var定义变量的区别以及优点。感谢阅读，如有问题，欢迎指正。

\


\


\


### 最后

\


###### 下次见!!!!
