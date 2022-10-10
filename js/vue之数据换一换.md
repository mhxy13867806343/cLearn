```
//换一换
import {reactive} from "vue";
export default function (){
  const sceneReactive=reactive({
    newList:[], //处理后的list
    timeStart:0, //截取第几组的开始参数
    timeEnd:1, //截取第几组的结束参数
    group:0, //默认为0组
    num:4, //一页展示list数量
    clickNum:0,//点击换一批次数
  })
  //换一批数据
  const onRouterClickScene=(list,num=4)=>{
    if(list.length>=num&&list.length>=sceneReactive.num) {
      onRouterToggle(list)
    }
  }
  const onRouterToggle=(list)=>{
    onRouterClickListLen(list.length)
    onRouterClickAutoIncre()
    onRouterClickListClear(sceneReactive.clickNum,sceneReactive.group)
    onRouterClickRenderR(list)
  }
//点击的时候获取分为几组
  const onRouterClickListLen=(len)=>{
    sceneReactive.group=len/sceneReactive.num
    if(len%sceneReactive.num!==0){
      sceneReactive.group=parseInt(sceneReactive.group)+1
    }
  }
//每点击一次记录点击次数
  const onRouterClickAutoIncre=()=>{
    sceneReactive.clickNum++
    sceneReactive.timeStart++
    sceneReactive.timeEnd++
  }
//计算将点击次数和开始截取的参数清空, 如果点击此时大于当前数据的组数，则重新开始计数。
  const onRouterClickListClear=(num,group)=>{
    if(num>group-1){
      sceneReactive.timeStart=0
      sceneReactive.timeEnd=1
      sceneReactive.clickNum=0
    }
  }
//截取当前每组的数据
  const onRouterClickRenderR=(arr)=>{
    sceneReactive.newList=arr.slice(
      sceneReactive.timeStart*sceneReactive.num,
      sceneReactive.timeEnd*sceneReactive.num)
  }
  return {
    sceneReactive,
    onRouterClickScene
  }
}
```
