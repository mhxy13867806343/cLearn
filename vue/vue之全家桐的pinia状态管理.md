## 官网

1.[英文官网](https://pinia.vuejs.org/)

2.[中文官网](https://pinia.web3doc.top/)

## pinia基本代码

```
import { defineStore } from 'pinia'
import {saveSearch,getSearch,delAllSearch,saveUser,getUser,clearAll} from '@/utils/data-cache'
export const useTestStore  = defineStore('main',{
    state:()=> {
        return {
            token: getUser('token')||'',//用户token
            cookie:getUser('cookie')||'',//用户cookie
            user: getUser('user'),//用户信息
            searchList: getSearch()||[],//搜索历史列表
            countrycode:getUser('countrycode')||[],//国家码
        }
    },
    getters: {
        getToken: state => state.token,
        getCookie: state => state.cookie,
        getUser: state => state.user,
        getSearchList: state => state.searchList,
        getCountrycode: state => state.countrycode,
    },
    actions:{
        //保存国家码列表
        saveCountrycode(list){
            this.countrycode.push()
            saveUser('countrycode',list)
        },
        //保存基本信息
        async onLogin({token,user,cookie}={token:'',user:{},cookie:''}) {
            this.user = user;
            this.token = token;
            this.cookie = cookie;
            saveUser('token',token)
            saveUser('user',user)
            saveUser('cookie',cookie)
        },
        //清空搜索记录
        clearSearchList(){
            this.searchList = [];
            delAllSearch()
        },
        //保存搜索记录
        saveSearchList(data){
            this.searchList.push(data);
            saveSearch( this.searchList)
        },
        //退出后清空
        clearLogin(){
            clearAll()
        }
    }
})
```

## 调用

```
import { useTestStore } from "@/store";
import { storeToRefs } from "pinia";
const testStore = useTestStore();
const {getCountrycode}=storeToRefs(testStore)
```
