注：今天遇到一个问题，在此记录下

需要在已有项目（如[uniapp](https://uniapp.dcloud.io/)和 [@vue/composition-api](https://github.com/vuejs/composition-api)结合使用中，添加如下功能）

```
<script setup>
import { defineProps, defineEmits } from '@vue/composition-api'

const props = defineProps({
  foo: String
})

const emit = defineEmits(['change', 'delete'])
// setup code
console.log(defineProps,defineEmits)//返回结果是undefined
</script>


//如截图 
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e30cb79b6cd44a6f9592d111b89bfa53~tplv-k3u1fbpfcp-zoom-1.image)

所遇到的问题，直接在

```
<script setup>
import {onShow} from 'uni-composition-api'
onShow(()=>{
//逻辑体，会报如下截图的错误
})
</script>
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cdb9b9c299c4d12a556e5d06826c1e7~tplv-k3u1fbpfcp-zoom-1.image)![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0824c7a035e746b5baa113e5bb6ec89b~tplv-k3u1fbpfcp-zoom-1.image)

去github上面询问了解决方案

```
<script setup>
import {onShow} from 'uni-composition-api'
onShow(()=>{
//这个在安装新插件，还没有测试过
})
</script>
```

[解决问题来源处===>](https://github.com/vuejs/composition-api/issues/915)安装对应的依赖（[unplugin-vue2-script-setup](https://github.com/antfu/unplugin-vue2-script-setup)）

我这边使用的是[Vue CLI](https://cli.vuejs.org/zh/index.html) 方式进行处理的

若未创建vue.config.js的话,请创建vue.config.js,得与src目录同级,

```
// vue.config.js
const ScriptSetup = require('unplugin-vue2-script-setup/webpack').default

module.exports = {
  parallel: false,  // disable thread-loader, which is not compactible with this plugin
  configureWebpack: {
    plugins: [
      ScriptSetup({ /* options */ }),
    ],
  },
}
```

复制完上面的代码进vue.config.js后，重启项目即可看到效果，使用unplugin-vue2-script-setup这个插件，请先安装

```
npm i -D unplugin-vue2-script-setup
```

文档说明：[unplugin-vue2-script-setup链接](https://github.com/antfu/unplugin-vue2-script-setup)

创建一个空白的.vue文件，使用如下操作

```
<script setup>
const props = defineProps({
  foo: String
})

const emit = defineEmits(['change', 'delete'])
// setup code
</script>
```

就可以看到效果，其他操作请看上面链接进行操作！
