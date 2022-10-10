### 官网：[tailwindcss 中文文档（官网）](https://www.tailwindcss.cn/)

### 指点: [RemMai 感谢这个博主的文章](https://www.cnblogs.com/RemMai/p/13403750.html)

### 相关链接

-   [vue-cli4 全面配置(持续更新)](https://staven630.github.io/vue-cli4-config/)

### 说明

-   我的个人项目采用vue3.js+vatn ui方式进行的，昨天加入了tailwindcss这个css库，安装过程中，出现了很多情况，在此记录下，把相关的 库放到这边记录下

```
"dependencies": {
   "@tailwindcss/postcss7-compat": "^2.2.17",
   "tailwindcss": "npm:@tailwindcss/postcss7-compat@^2.2.10"


},
  "devDependencies": {
     "postcss": "^7.0.39",
    "postcss-cli": "^8.3.1",
    "postcss-pxtorem": "^5.1.1"
  }
```

-   安装完依赖之后，在命令行中输入，（要求与src目录同级即可）找到vue.configs.js文件添加如下代码

```
// vue.config.js
module.exports = {
  css: {
    loaderOptions: {
      postcss: {
        plugins: [
          require('tailwindcss'),
          require('autoprefixer')
        ]
      }
    }
  }
}
```

-   安装完依赖之后，在命令行中输入，（要求与src目录同级即可）

```
 npx tailwind init
```

会生成与src目录同级的一个文件：tailwind.config.js

-   最后在main.js文件中输入如下代码

```
import 'tailwindcss/tailwind.css'
```

-   当以上操作都处理好了之后，重启项目即可
