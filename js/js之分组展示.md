```
export function getGroupsCategoryList(arrList) {
  const data = arrList
  const map = {}
  const list = []
  if (data.length) {
    data.map(item => {
      if (!map[item.subScene]) {
        if (item.sceneSort !== '1000') {
          list.push({
            Group: item.subScene,
            id: item.sceneId,
            category: item.subScene,
            leftName: item.subScene_dictText,
            logo: item.sceneLogo,
            navList: data
          })
          map[item.subScene] = item
        }
      } else {
        list.map(j => {
          const dj = j
          if (dj.subScene == item.subScene) {
            dj.navList.push(item)
          }
        })
      }
    })
    return list
  }
}
```

截图

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37fa506758f84a1eb9f7a6dc1a510e58~tplv-k3u1fbpfcp-zoom-1.image)
