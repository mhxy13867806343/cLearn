```
export const clikPhone = value=>/^(?:(?:+|00)86)?1\d{10}$/.test(value)
```

```
export const clickEmail=value=>/^(([^<>()[]\.,;:\s@"]+(.[^<>()[]\.,;:\s@"]+)*)|(".+"))@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}])|(([a-zA-Z-0-9]+.)+[a-zA-Z]{2,}))$/.test(value)
```

```
export const clickId=value=>/^\d{6}((((((19|20)\d{2})(0[13-9]|1[012])(0[1-9]|[12]\d|30))|(((19|20)\d{2})(0[13578]|1[02])31)|((19|20)\d{2})02(0[1-9]|1\d|2[0-8])|((((19|20)([13579][26]|[2468][048]|0[48]))|(2000))0229))\d{3})|((((\d{2})(0[13-9]|1[012])(0[1-9]|[12]\d|30))|((\d{2})(0[13578]|1[02])31)|((\d{2})02(0[1-9]|1\d|2[0-8]))|(([13579][26]|[2468][048]|0[048])0229))\d{2}))(\d|X|x)$/.test(value)
```

###### 更多js正式表达式示例

[链接===〈〉](https://raw.githubusercontent.com/any86/any-rule/v0.3.7/packages/www/src/RULES.js)

##### 若对您有所帮助，麻烦点个赞或者分享给其他朋友哦，谢谢
