```
export  function getTypeCodeList(){
    let [newList,oldList,indexList] = [[],[],[]] //newList保存除了其他的数组  oldList保存其他的数组
    // indexList 保存0-index的索引值
    const typeCodeList=[
        {name:'入驻歌手',cat:5001},
        {name:'华语男歌手',cat:1001},
        {name:'华语女歌手',cat:1002},
        {name:'华语组合/乐队',cat:1003},
        {name:'欧美男歌手',cat:2001},
        {name:'欧美女歌手',cat:2002},
        {name:'欧美组合/乐队',cat:2003},
        {name:'日本男歌手',cat:6001},
        {name:'日本女歌手',cat:6002},
        {name:'日本组合/乐队',cat:6003},
        {name:'韩国男歌手',cat:7001},
        {name:'韩国女歌手',cat:7002},
        {name:'其他男歌手',cat:4001},
        {name:'其他女歌手',cat:4002},
        {name:'其他组合/乐队',cat:4003},
    ] //歌手列表
    typeCodeList.reduce((olds,news,index)=>{
        const {name,cat} =news
        indexList.push(index)
        const startsWith = name.startsWith('其他')
        if(startsWith){
            oldList.push(news)
        } else {
            newList.push(news)
        }
    }, [])
    newList.sort((n,c)=>{
        return n.cat-c.cat
    })
    newList = [...newList,...oldList]
    return {
        newList,
        indexList
    }
}
```
