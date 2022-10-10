## vite是什么?

###### 是一种新型的前端构建工具,能够显著提升前端开发体验。它主要由两部分组成：一个开发服务器，它基于 原生 ES 模块 提供了 丰富的内建功能，如速度快到惊人的 模块热更新（HMR）。一套构建指令，它使用 Rollup 打包你的代码，并且它是预配置的，可输出用于生产环境的高度优化过的静态资源。

## 对比

###### 与webpack相比

**Vite 是基于原生 ES6 Modules，在生产环境下打包使用的是 Rollup。vue-cli 基于 webpack 封装，生产环境和开发环境都是基于 Webpack 打包。所以两者在生产环境下都是基于源代码文件打包。但在开发环境中，两者有所不同。Vite 在开发环境下，基于原生 ES6 ，无需对代码进行打包，浏览器可以直接调用。所以 Vite 因为基于浏览器的原生功能，省掉了打包过程，在开发环境中体验及其愉快。**

## vite官网和vue cli官网

vite官网:[vite国服](https://cn.vitejs.dev/),[vite英语](https://vitejs.dev/)

vue cli官网:[vue cli国服](https://cli.vuejs.org/zh/),[vue cli英文](https://cli.vuejs.org/index.html)

## vite插件

[vite插件](https://cn.vitejs.dev/plugins/),[vite其他插件](https://github.com/vitejs/awesome-vite#plugins)

## vue cli插件

[vue cli插件](https://github.com/vuejs/vue-docs-zh-cn)

## 为什么选 Vite？

**在浏览器支持 ES 模块之前，JavaScript 并没有提供原生机制让开发者以模块化的方式进行开发。这也正是我们对 “打包” 这个概念熟悉的原因：使用工具抓取、处理并将我们的源码模块串联成可以在浏览器中运行的文件。**

## vite开始项目

**开始搭建第一个 Vite 项目**

```
$ npm create vite@latest
```

```
$ yarn create vite
```

```
$ pnpm create vite
```

### 创建项目请看<https://cn.vitejs.dev/guide/#index-html-and-project-root>

\


在项目创建完之后，需要创建如下几个文件（画红色线部分的）

.env.development和.env.production 用于存放比如接口服务器地址，一些类型等

vite.config.js用于存放比如处理跨域操作，打包操作等所需要的一些配置行为

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e39638b093eb406dbb77f8ef73d78d37~tplv-k3u1fbpfcp-zoom-1.image)

```
import { defineConfig, loadEnv } from 'vite' //导入vite相关的方法
import path from 'path'// node方法，用于查找路径
import vue from '@vitejs/plugin-vue';//导入vite相关的vue
import Components from 'unplugin-vue-components/vite';//unplugin-vue-components 是由 Vue官方人员开发的一款自动引入插件，可以省去比如 UI 库的大量 import 语句。
import { VantResolver } from 'unplugin-vue-components/resolvers';//插件可以在Vue文件中自动引入组件（包括项目自身的组件和各种组件库中的组件）
import { createHtmlPlugin } from "vite-plugin-html";//一个针对 index.html，提供压缩和基于 ejs 模板功能的 vite 插件。 通过搭配.env 文件，可以在开发或构建项目时，对 index.html 注入动态数据，例如替换网站标题。
import globalStyle from '@originjs/vite-plugin-global-style'//开头的文件会自动添加到 Vite 全局样式中。SASSLESSStylusglobal

// https://vitejs.dev/config/
export default ({mode})=>{
  process.env = { ...process.env, ...loadEnv(mode, process.cwd()) };
  const env = loadEnv(mode, process.cwd());
  return defineConfig({
    // optimizeDeps:{
    //   exclude:[],
    //   entries:''
    // },
    build:{//打包输出
      outDir: 'dist',//Specify the output directory (relative to project root).
    },
    resolve: {
      alias: {//配置别名操作
        '@':path.resolve(__dirname,'src'),
      }
    },
    base:loadEnv(mode, process.cwd()).VITE_APP_ENV,//开发或生产环境服务的公共基础路径
    publicDir:'public',//作为静态资源服务的文件夹。该目录中的文件在开发期间在 / 处提供，并在构建期间复制到 outDir 的根目录，并且始终按原样提供或复制而无需进行转换。该值可以是文件系统的绝对路径，也可以是相对于项目的根目录的相对路径。
    plugins: [
        vue({
          babel:{
            plugins: [//配置相关插件 
              //此处这2个插件，进行?. ??方式的操作，具体可以 查看如下连接地址
              //复制到浏览器:https://zh.javascript.info/
              "@babel/plugin-proposal-optional-chaining",
              "@babel/plugin-proposal-nullish-coalescing-operator",
            ]
          }
        }),
      Components({
        //全局可以 不用导入，直接 使用
        resolvers: [VantResolver()]
      }),
      createHtmlPlugin({
        minify: true,
        enter:'src/main.js',
        template: 'public/index.html',
        inject: {
          data:{
            title:'vite app',
            injectScripts: `<script src="./inject.js"></script>`
          }
        }
      }),
    ],
    css:{
      preprocessorOptions: {
        scss: {//全局配置文件
          // 此处修改为要被预处理的scss文件地址
          additionalData: `@import "css文件路径";`
        },
      }
    },
    define:{//定义全局常量替换方式。其中每项在开发环境下会被定义在全局，而在构建时被静态替换。
      'process.env':{}
    },
    server:{//配置本地服务相关
      hmr:true,
      host:'localhost',
      port:3001,
      open:true,
      strictPort: false,
      https: false,
      proxy:{
        '/api':{
          target:env.VITE_APP_URL,
          changeOrigin: true,
          rewrite: path => path.replace(/^/api/, '')
        }
      }
    }
  })
}
```

##### 相关库连接地址

unplugin-vue-components:[unplugin-vue-components](https://github.com/antfu/unplugin-vue-components)

unplugin-vue-components:[unplugin-vue-components](https://github.com/antfu/unplugin-vue-components)

vite-plugin-html:[vite-plugin-html](https://github.com/vbenjs/vite-plugin-html)

vite-plugin-global-style:[vite-plugin-global-style](https://originjs.org/en/guide/plugins/vite-plugin-global-style/)

###### 相关说明

vite配置跨域相关问题（第三方提供）

1.[vite 中配置 proxy 代理 https](http://www.alvinhtml.com/article/web/vite-proxy-https.html)

##### 若对您有所帮助，麻烦点个赞或者分享给其他朋友哦，谢谢
