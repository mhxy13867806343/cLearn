链接地址

[tailwindcss中文](https://www.tailwindcss.cn/)

无需离开您的HTML，即可快速建立现代网站。

Tailwind CSS 是一个功能类优先的 CSS 框架，它集成了诸如 flex, pt-4, text-center 和 rotate-90 这样的的类，它们能直接在脚本标记语言中组合起来，构建出任何设计。

通过如下命令生成如下的截图

```
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
//如果在webstorm里面使用如上命令，会出现无法提示的问题，需要使用如下的方式才可以在webstorm中提示 
//在package.json中的 
  "dependencies": {
   "tailwindcss": "npm:@tailwindcss/postcss7-compat",  
  }
//若有node_modules先删除掉，若无，再直接进行安装依赖即可,安装完成之后就可以有提示操作了
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18c20a4e839c4a1bbc0218a110fecd64~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a7dac94a5e448f98dba629003a87e8e~tplv-k3u1fbpfcp-zoom-1.image)

\


在src/assets/tailwind.css中复制如下代码

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

如上3行代码请查看=><https://www.tailwindcss.cn/docs/functions-and-directives>

tailwind.config.js配置 如果需要自己配置，可以参考如下代码，

```
module.exports = {
    purge: ['./public/index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {},
        fontSize:{//字体自定义配置
            'xs': '10px',
            'sm': '12px',
            'tiny': '14px',
            'base': '16px',
            'lg': '18px',
            'xl': '20px',
            '2xl': '22px',
            '3xl': '24px',
            '4xl': '26px',
            '5xl': '28px',
            '6xl': '30px',
            '7xl': '32px',
            '8xl': '34px',
            '9xl': '36px',
            '10xl': '38px',
            '11xl': '40px',
            '12xl': '42px',
            '13xl': '44px',
            '14xl': '46px',
            '15xl': '48px',
            '16xl': '50px',
            '17xl': '52px'
        }
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
```

也可以 按文档进行配置=><https://www.tailwindcss.cn/docs/configuration>
