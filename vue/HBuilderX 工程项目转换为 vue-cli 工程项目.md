# 步骤1、安装vue-cli

```
npm install -g @vue/cli
```

# 步骤2、新建通过vue-cli搭建的项目

```
vue create -p dcloudio/uni-preset-vue vue-cli-project
```

选择默认版本

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47d2d1fd61e44abf82ff9c6adda01715~tplv-k3u1fbpfcp-zoom-1.image)

# 步骤3、新建存放旧项目的文件夹

```
mkdir newProject
```

# 步骤4、项目迁移

## 第一步

在newProject文件夹的根目录下新建src文件夹，将HBuilderX创建的工程项目里面所有的文件copy进src文件夹。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e3be6177dfc458b847f8fda60503a6a~tplv-k3u1fbpfcp-zoom-1.image)

## 第二步

将vue-cli-project项目这些文件copy进newProject文件夹的根目录下。

\
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/256ea9e2f78448e68d8c3bad06b77ae2~tplv-k3u1fbpfcp-zoom-1.image)

## 第三步

修改newProject文件夹根目录下的package.json文件，将src文件夹下的package.json文件的相关配置copy到根目录下的package.json文件。然后删除src文件夹下的package.json文件与package-lock.json文件。

## 第四步

安装相关依赖，注意：\
需安装less-loader与sass-loader，因为HBuilderX 工程自带插件帮我们安装了less-loader或者sass-loader，所以迁移到vue-cli工程项目的时候，我们要安装一次。

```
例如我用的是sass
package.json
{
...
    "devDependencies": {
        ...
        "sass": "^1.42.1",
        "sass-loader": "10.1.1"
    
    },
      "devDependencies":{
          "@vue/composition-api": "^1.4.6",
    "uni-composition-api": "^0.6.1",
      
      }
...
}

yarn 
```

我这边的package.json文件

```
{
  "name": "vue-cli-project",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "npm run dev:h5",
    "build": "npm run build:h5",
    "build:app-plus": "cross-env NODE_ENV=production UNI_PLATFORM=app-plus vue-cli-service uni-build",
    "build:custom": "cross-env NODE_ENV=production uniapp-cli custom",
    "build:h5": "cross-env NODE_ENV=production UNI_PLATFORM=h5 vue-cli-service uni-build",
    "build:mp-360": "cross-env NODE_ENV=production UNI_PLATFORM=mp-360 vue-cli-service uni-build",
    "build:mp-alipay": "cross-env NODE_ENV=production UNI_PLATFORM=mp-alipay vue-cli-service uni-build",
    "build:mp-baidu": "cross-env NODE_ENV=production UNI_PLATFORM=mp-baidu vue-cli-service uni-build",
    "build:mp-jd": "cross-env NODE_ENV=production UNI_PLATFORM=mp-jd vue-cli-service uni-build",
    "build:mp-kuaishou": "cross-env NODE_ENV=production UNI_PLATFORM=mp-kuaishou vue-cli-service uni-build",
    "build:mp-lark": "cross-env NODE_ENV=production UNI_PLATFORM=mp-lark vue-cli-service uni-build",
    "build:mp-qq": "cross-env NODE_ENV=production UNI_PLATFORM=mp-qq vue-cli-service uni-build",
    "build:mp-toutiao": "cross-env NODE_ENV=production UNI_PLATFORM=mp-toutiao vue-cli-service uni-build",
    "build:mp-weixin": "cross-env NODE_ENV=production UNI_PLATFORM=mp-weixin vue-cli-service uni-build",
    "build:quickapp-native": "cross-env NODE_ENV=production UNI_PLATFORM=quickapp-native vue-cli-service uni-build",
    "build:quickapp-webview": "cross-env NODE_ENV=production UNI_PLATFORM=quickapp-webview vue-cli-service uni-build",
    "build:quickapp-webview-huawei": "cross-env NODE_ENV=production UNI_PLATFORM=quickapp-webview-huawei vue-cli-service uni-build",
    "build:quickapp-webview-union": "cross-env NODE_ENV=production UNI_PLATFORM=quickapp-webview-union vue-cli-service uni-build",
    "dev:app-plus": "cross-env NODE_ENV=development UNI_PLATFORM=app-plus vue-cli-service uni-build --watch",
    "dev:custom": "cross-env NODE_ENV=development uniapp-cli custom",
    "dev:h5": "cross-env NODE_ENV=development UNI_PLATFORM=h5 vue-cli-service uni-serve",
    "dev:mp-360": "cross-env NODE_ENV=development UNI_PLATFORM=mp-360 vue-cli-service uni-build --watch",
    "dev:mp-alipay": "cross-env NODE_ENV=development UNI_PLATFORM=mp-alipay vue-cli-service uni-build --watch",
    "dev:mp-baidu": "cross-env NODE_ENV=development UNI_PLATFORM=mp-baidu vue-cli-service uni-build --watch",
    "dev:mp-jd": "cross-env NODE_ENV=development UNI_PLATFORM=mp-jd vue-cli-service uni-build --watch",
    "dev:mp-kuaishou": "cross-env NODE_ENV=development UNI_PLATFORM=mp-kuaishou vue-cli-service uni-build --watch",
    "dev:mp-lark": "cross-env NODE_ENV=development UNI_PLATFORM=mp-lark vue-cli-service uni-build --watch",
    "dev:mp-qq": "cross-env NODE_ENV=development UNI_PLATFORM=mp-qq vue-cli-service uni-build --watch",
    "dev:mp-toutiao": "cross-env NODE_ENV=development UNI_PLATFORM=mp-toutiao vue-cli-service uni-build --watch",
    "dev:mp-weixin": "cross-env NODE_ENV=development UNI_PLATFORM=mp-weixin vue-cli-service uni-build --watch",
    "dev:quickapp-native": "cross-env NODE_ENV=development UNI_PLATFORM=quickapp-native vue-cli-service uni-build --watch",
    "dev:quickapp-webview": "cross-env NODE_ENV=development UNI_PLATFORM=quickapp-webview vue-cli-service uni-build --watch",
    "dev:quickapp-webview-huawei": "cross-env NODE_ENV=development UNI_PLATFORM=quickapp-webview-huawei vue-cli-service uni-build --watch",
    "dev:quickapp-webview-union": "cross-env NODE_ENV=development UNI_PLATFORM=quickapp-webview-union vue-cli-service uni-build --watch",
    "info": "node node_modules/@dcloudio/vue-cli-plugin-uni/commands/info.js",
    "serve:quickapp-native": "node node_modules/@dcloudio/uni-quickapp-native/bin/serve.js",
    "test:android": "cross-env UNI_PLATFORM=app-plus UNI_OS_NAME=android jest -i",
    "test:h5": "cross-env UNI_PLATFORM=h5 jest -i",
    "test:ios": "cross-env UNI_PLATFORM=app-plus UNI_OS_NAME=ios jest -i",
    "test:mp-baidu": "cross-env UNI_PLATFORM=mp-baidu jest -i",
    "test:mp-weixin": "cross-env UNI_PLATFORM=mp-weixin jest -i"
  },
  "dependencies": {
    "@dcloudio/uni-app-plus": "^2.0.1-33920220208001",
    "@dcloudio/uni-h5": "^2.0.1-33920220208001",
    "@dcloudio/uni-helper-json": "*",
    "@dcloudio/uni-i18n": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-360": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-alipay": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-baidu": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-jd": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-kuaishou": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-lark": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-qq": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-toutiao": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-vue": "^2.0.1-33920220208001",
    "@dcloudio/uni-mp-weixin": "^2.0.1-33920220208001",
    "@dcloudio/uni-quickapp-native": "^2.0.1-33920220208001",
    "@dcloudio/uni-quickapp-webview": "^2.0.1-33920220208001",
    "@dcloudio/uni-stat": "^2.0.1-33920220208001",
    "@vue/shared": "^3.0.0",
    "core-js": "^3.6.5",
    "flyio": "^0.6.2",
    "regenerator-runtime": "^0.12.1",
    "vue": "^2.6.11",
    "vuex": "^3.2.0",
    "lodash": "^4.17.21",
    "moment": "^2.29.1",
    "vant": "^2.12.44",
    "node-sass": "^4.14.0",
    "sass-loader": "^8.0.2"
  },
  "devDependencies": {
    "@babel/runtime": "~7.12.0",
    "@dcloudio/types": "*",
    "@dcloudio/uni-automator": "^2.0.1-33920220208001",
    "@dcloudio/uni-cli-i18n": "^2.0.1-33920220208001",
    "@dcloudio/uni-cli-shared": "^2.0.1-33920220208001",
    "@dcloudio/uni-migration": "^2.0.1-33920220208001",
    "@dcloudio/uni-template-compiler": "^2.0.1-33920220208001",
    "@dcloudio/vue-cli-plugin-hbuilderx": "^2.0.1-33920220208001",
    "@dcloudio/vue-cli-plugin-uni": "^2.0.1-33920220208001",
    "@dcloudio/vue-cli-plugin-uni-optimize": "^2.0.1-33920220208001",
    "@dcloudio/webpack-uni-mp-loader": "^2.0.1-33920220208001",
    "@dcloudio/webpack-uni-pages-loader": "^2.0.1-33920220208001",
    "@vue/cli-plugin-babel": "~4.5.15",
    "@vue/cli-service": "~4.5.15",
    "babel-plugin-import": "^1.11.0",
    "cross-env": "^7.0.2",
    "jest": "^25.4.0",
    "mini-types": "*",
    "miniprogram-api-typings": "*",
    "postcss-comment": "^2.0.0",
    "@vue/composition-api": "^1.4.6",
    "uni-composition-api": "^0.6.1",
    "vue-template-compiler": "^2.6.11"
  },
  "browserslist": [
    "Android >= 4.4",
    "ios >= 9"
  ],
  "uni-app": {
    "scripts": {}
  }
}
```

\


# 步骤5、运行与发布项目（小程序举例）

具体项目类型可以根据 [官方文档](https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fquickstart-cli%3Fid%3D%25e8%25bf%2590%25e8%25a1%258c%25e3%2580%2581%25e5%258f%2591%25e5%25b8%2583uni-app) 进行运行与发布,或者查看package.json的script字段。

# 步骤6：来源=>([HBuilderX 工程项目转换为 vue-cli 工程项目](https://juejin.cn/post/7018764210221875231))
