# 今天刚刚白天刚刚接到一个需求:就是做一个类似支付宝首页-》更多，对里面的元素进行添加、删除、拖拽、点击, 我内心其实是拒绝的，没怎么去用过这个功能，就无从下手，网上找了下相关的示例后，发现支付宝添加、删除、拖拽、点击对元素的操作，其实很简单的操作啦

### gif截屏软件[:]([屏幕托吉夫 - 记录您的屏幕，编辑和保存作为一个 GIF，视频或其他格式 (screentogif.com)](https://www.screentogif.com/))
### [Snipaste - 截图 + 贴图]([Snipaste - 截图 + 贴图](https://zh.snipaste.com/))

### [ vue3文档]([Vue3中文文档 - vuejs (vue3js.cn)](https://vue3js.cn/docs/zh/))
### [uniapp文档](https://uniapp.dcloud.io/)
### 起步

首先:请先安装2个依赖:

| 依赖名称         | 安装命令和链接地址                                                                                      | 说明                                                                                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sortable     | yarn add sortable npm i -S sortable<http://www.sortablejs.com/>                                | 功能强大的JavaScript 拖拽库                                                                                                                                        |
| vuedraggable | yarn add vuedraggable npm i -S vuedraggable<https://www.itxst.com/vue-draggable/tutorial.html> | 是一款基于Sortable.js实现的vue拖拽插件。支持移动设备、拖拽和选择文本、智能滚动，可以在不同列表间拖拽、不依赖jQuery为基础、vue 2过渡动画兼容、支持撤销操作，总之是一款非常优秀的vue拖拽组件。本篇将介绍如何搭建环境及简单的例子，使用起来特别简单对被拖拽元素也没有CSS样式的特殊要求。 |

注意:（如果没有package.json的话）,请先在项目下使用命令行:npm init -y 创建出package.json相关内容,若存在，则省略此步骤操作

### 接着

效果如下(静态界面演示)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e89bdfc2ef94b018b9f6b7e04e070af~tplv-k3u1fbpfcp-zoom-1.image)

\


\


添加/删除等相关效果演示

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/367a308eac90474aafe3f03fcbff086c~tplv-k3u1fbpfcp-zoom-1.image)

\


设置标签

\


操作思路：

准备2个不同的数组，如list1和list2,list1用于存我的应用这部分列表数据,而list2用于存最近使用，热门推荐，所有应用相关列表，

其中当我的应用存在常用的8个时，如果进行删除操作会将删除的元素进入到所有应用这个栏目中去展示，所以在我的应用会存在一个独一无二的字段作为是否为常用的标识体（此标识体，也可以由后端提供）

list1中的结构如下

```
 //我的应用中一开始的
				navList: [{
						id: 1,
						title: '我要捐款',
						icon: '/static/server/my1.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
          ....
				],
```

list2中的结构如下

```
list1: [{
						leftName: '最近使用',
						rightName: '全部',

						navList: [{
								title: '会员活动',
								icon: '/static/server/recently1.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							...
						]
					},
					{
						leftName: '热门推荐',
						rightName: '全部',
						navList: [{
								title: '器官（遗体、组织）',
								icon: '/static/server/recommend1.png', //控制定位的icon
								url: 'http://app22.hzgsredcross.org.cn/addqgjx.aspx?quId=1', //所要跳转的url地址
							},
								...
						]
					},
					{
						leftName: '所有应用',
						rightName: '全部',
						navList: [{
								title: '我要发表文章',
								icon: '/static/server/icon1.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
								...
						]
					}
				]
```

相关的结构体如下上面

html模板结构部分如下 我的常用列表模板

```
	<block v-for="(item,index) in navList" :key="index">
							<view class="data" :class="index>=4?'datas':''" @click="onDel(item,index)">
								<view class="icon">
									<view class="dd">
										<image :src="item.icon" class="images"></image>
										<image v-if="edit" src="/static/server/delete.png" class="images1"></image>
									</view>

								</view>
								<view class="text">
									{{item.title}}
								</view>
							</view>
						</block>
```

html模板结构部分如下 其他列表模板

```
<view class="content" v-for="(k,v) in list1" :key="v">
			<view class="main">
				<view class="title">
					<view class="left">
						<text>{{k.leftName}}</text>
					</view>
					<view class="right">
						<text>{{k.rightName}}</text>
						<u-icon name="arrow-right"></u-icon>
					</view>
				</view>
				<view class="iconList">
					<block v-for="(item,index) in k.navList" :key="index">
						<view class="data list-group-item" :class="index>=4?'datas':''" @click="onAdd(v,index)">
							<view class="icon">
								<image :src="item.icon" class="images"></image>
								<image v-if="edit" src="/static/server/add.png" class="images1"></image>
							</view>
							<view class="text">
								{{item.title}}
							</view>
						</view>
					</block>
				</view>
			</view>
		</view>
```

上面部分只参与了添加,删除的模板操作

```
data() {
			return {
				edit: false, //定义一个标识，用于判断是否为修改还是编辑状态
      }
},
  //onEdit方法操作
  methods: {
			//编辑状态
			onEdit() {
				this.edit = !this.edit
			},
        //添加
        //判断当修改状态时，才可以进行添加（除我的应用外的列表元素，将相应的列表元素值添加一个数组中，将删除原数组中的一项，其实可以使用filter这个方法进行删除操作的）
			onAdd(a, b) {
				if (this.edit) {
					this.navList.push({
						id: this.list1[a].navList[b].id,
						title: this.list1[a].navList[b].title,
						icon: this.list1[a].navList[b].icon, //控制定位的icon
						url: this.list1[a].navList[b].url, //所要跳转的url地址
						name: this.list1[a].leftName,
						pageIndex: a,
						childIndex: b,
					})
					this.list1[a].navList.splice(b, 1)
				}
			},
        //删除状态的逻辑和添加类似
        //并判断list1中是否存在isCommonly这个字段，如果有，说明是常用列表元素，删除到所有应用列表中去，将原数组中的项进行删除掉
			onDel(item,index) {
				if (this.edit) {
          //如果有有isCommonly,则为常用的
          if(item.isCommonly){
            const {icon, id, isCommonly, title, url} = item
            this.navList.splice(index, 1)
            this.list1[this.list1.length-1].navList.push({
              id,
              title,
              icon,
              url,
              isCommonly
            })

          } else {
            const pt = this.navList[index]
            const {
              pageIndex,
              childIndex,
              id,
              title,
              icon,
              url
            } = pt
            if (this.list1[pageIndex]) {
              this.navList.splice(index, 1)
              this.list1[pageIndex].navList.splice(childIndex, pageIndex,

                  {
                    id,
                    title,
                    icon,
                    url
                  })
            }

          }
				}
			},
  }
```

html修改或者编辑模板

```
<view class="title">
					<view class="left">
						<text>我的应用</text>
					</view>
					<view class="right edit" @click="onEdit">
						<text style="color: #4F73FE;margin-right: 10rpx;">{{edit?'修改':'编辑'}}</text>
					</view>
				</view>
```

拖拽演示操作

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/def65f3c3a8849f4a032c6dc6c273e9e~tplv-k3u1fbpfcp-zoom-1.image)

拖拽的思路和添加,删除类似，主要是判断是否在修改状态下进行操作的，若是，就可以进行拖拽操作，否则 不能进行拖拽操作

js部分

```
//如果未安装依赖，请先安装相关依赖才进行操作
import draggable from "vuedraggable"
components: {
			draggable//注册组件
		},
//然后就可以使用了
//更多的操作请看上面表格中所有的链接地址
```

拖拽html模板代码如下

```
<draggable :disabled="!edit" class="ul-draggable" element="ul" v-model="navList">
						<block v-for="(item,index) in navList" :key="index">
							<view class="data" :class="index>=4?'datas':''" @click="onDel(item,index)">
								<view class="icon">
									<view class="dd">
										<image :src="item.icon" class="images"></image>
										<image v-if="edit" src="/static/server/delete.png" class="images1"></image>
									</view>

								</view>
								<view class="text">
									{{item.title}}
								</view>
							</view>
						</block>
					</draggable>
```

完整代码如下

html模板部分

```
<template>
	<view class="server">
		<Header></Header>
		<view class="content">
			<view class="main">
				<view class="title">
					<view class="left">
						<text>我的应用</text>
					</view>
					<view class="right edit" @click="onEdit">
						<text style="color: #4F73FE;margin-right: 10rpx;">{{edit?'修改':'编辑'}}</text>
					</view>
				</view>
				<view class="iconList">
					<draggable :disabled="!edit" class="ul-draggable" element="ul" v-model="navList">
						<block v-for="(item,index) in navList" :key="index">
							<view class="data" :class="index>=4?'datas':''" @click="onDel(item,index)">
								<view class="icon">
									<view class="dd">
										<image :src="item.icon" class="images"></image>
										<image v-if="edit" src="/static/server/delete.png" class="images1"></image>
									</view>

								</view>
								<view class="text">
									{{item.title}}
								</view>
							</view>
						</block>
					</draggable>
				</view>
			</view>
		</view>
		<view class="content" v-for="(k,v) in list1" :key="v">
			<view class="main">
				<view class="title">
					<view class="left">
						<text>{{k.leftName}}</text>
					</view>
					<view class="right">
						<text>{{k.rightName}}</text>
						<u-icon name="arrow-right"></u-icon>
					</view>
				</view>
				<view class="iconList">
					<block v-for="(item,index) in k.navList" :key="index">
						<view class="data list-group-item" :class="index>=4?'datas':''" @click="onAdd(v,index)">
							<view class="icon">
								<image :src="item.icon" class="images"></image>
								<image v-if="edit" src="/static/server/add.png" class="images1"></image>
							</view>
							<view class="text">
								{{item.title}}
							</view>
						</view>
					</block>
				</view>
			</view>
		</view>
	</view>
</template>
```

css样式部分

```
<style lang="scss" scoped>
	.server {
		background: #F6F6F6;
		padding-bottom: 150rpx;
	}
	.content {
		margin: 0 25rpx 20rpx 25rpx;
		background: #FFFFFF;
		border-radius: 15rpx;
		.main {
			.title {
				padding: 21rpx 25rpx 0 25rpx;
				display: flex;
				justify-content: space-between;
				align-items: center;
				.left {
					font-size: 30rpx;
					font-family: PingFang;
					font-weight: bold;
					color: #222222;
				}
				.right {
					font-size: 26rpx;
					font-family: PingFang;
					font-weight: 500;
					color: #666666;
					.u-icon{
						margin-left: 10rpx;
						font-size: 26rpx;
						color: #666666;
					}
				}
				.edit {
					color: #222222;
				}
			}

			.iconList {
				margin-top: 30rpx;
				width: auto;
				border-radius: 5rpx;
				display: flex;
				justify-content: flex-start;
				white-space: nowrap;
				flex-wrap: wrap;
				.data {
					margin-bottom: 30rpx;
					flex-basis: 25%;
					box-sizing: border-box;
					text-align: center;
					.icon {
						flex-grow: 1;
						position: relative;
						.images {
							width: 45rpx;
							height: 43rpx;
						}
						.images1 {
							width: 27rpx;
							height: 27rpx;
							border-radius: 50%;
							position: absolute;
							right: 30%;
							top: -10rpx;
							transform: translate(60%, 0);
						}
					}
					.text {
						width: 167rpx;
						padding: 7rpx 20rpx;
						overflow: hidden;
						text-overflow:ellipsis;
						white-space: nowrap;
						font-size: 24rpx;
						font-family: PingFang;
						font-weight: 500;
						color: #222222;
					}
				}
			}
		}
	}
	.list-group {
		width: 100%;
		height: auto;
	}
	.list-group-item_img {
		position: absolute;
		width: 16px;
		right: 0;
		margin-right: 4px;
	}
	.list-group-item_img2 {
		position: absolute;
		width: 18px;
		right: 0;
		margin-right: 4px;
	}
	.list-group-item {
		cursor: move;
		float: left;
		width: 20%;
	}
	.list-group-item-div {
		padding: 10px 0px;
	}
	.ul-draggable {
		display: flex;
		flex-wrap: wrap;
		padding: 0;
	}
</style>
```

js逻辑部分

```
<script>
	import draggable from "vuedraggable"
	export default {
		components: {

			draggable
		},

		data() {
			return {
				enabled: true,
				dragging: false,
				edit: false,
        //我的应用中一开始的
				navList: [{
						id: 1,
						title: '我要捐款',
						icon: '/static/server/my1.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 2,
						title: '我要捐物',
						icon: '/static/server/my2.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 3,
						title: '个人入会',
						icon: '/static/server/my3.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 4,
						title: '团体入会',
						icon: '/static/server/my4.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 5,
						title: '我要求助',
						icon: '/static/server/my5.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 6,
						title: '捐物记录',
						icon: '/static/server/my6.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 7,
						title: '捐款记录',
						icon: '/static/server/my7.png', //控制定位的icon
						url: '', //所要跳转的url地址
					},
					{
						id: 8,
						title: '更多应用',
						icon: '/static/server/my8.png', //控制定位的icon
						url: '', //所要跳转的url地址
					}
				],
				list1: [{
						leftName: '最近使用',
						rightName: '全部',

						navList: [{
								title: '会员活动',
								icon: '/static/server/recently1.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '成为志愿者',
								icon: '/static/server/recently2.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '志愿者活动',
								icon: '/static/server/recently3.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '集锦秀',
								icon: '/static/server/recently4.png', //控制定位的icon
								url: '', //所要跳转的url地址
							}
						]
					},
					{
						leftName: '热门推荐',
						rightName: '全部',
						navList: [{
								title: '器官（遗体、组织）',
								icon: '/static/server/recommend1.png', //控制定位的icon
								url: 'http://app22.hzgsredcross.org.cn/addqgjx.aspx?quId=1', //所要跳转的url地址
							},
							{
								title: '一键呼救',
								icon: '/static/server/recommend2.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '救援记录',
								icon: '/static/server/recommend3.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '呼救记录',
								icon: '/static/server/recommend4.png', //控制定位的icon
								url: '', //所要跳转的url地址
							}
						]
					},
					{
						leftName: '所有应用',
						rightName: '全部',
						navList: [{
								title: '我要发表文章',
								icon: '/static/server/icon1.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '我要建议',
								icon: '/static/server/icon2.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '在线学习',
								icon: '/static/server/icon3.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '申领急救物资',
								icon: '/static/server/icon4.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '救护E站',
								icon: '/static/server/icon5.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '联系红会',
								icon: '/static/server/icon6.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '博爱家园',
								icon: '/static/server/icon7.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '积分商城',
								icon: '/static/server/icon8.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '加入志愿者队伍',
								icon: '/static/server/icon9.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '救护员培训报名',
								icon: '/static/server/icon10.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '培训记录',
								icon: '/static/server/icon11.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '我要开票',
								icon: '/static/server/icon12.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '我要咨询',
								icon: '/static/server/icon13.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '捐赠证书',
								icon: '/static/server/icon14.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '积分记录',
								icon: '/static/server/icon15.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '查找AED',
								icon: '/static/server/icon16.png', //控制定位的icon
								url: '', //所要跳转的url地址
							},
							{
								title: '造血干细胞捐献意向登记',
								icon: '/static/server/icon17.png', //控制定位的icon
								url: 'http://app22.hzgsredcross.org.cn/addzxgxb.aspx?quId=1', //所要跳转的url地址
							}
						]
					}
				]
			};
		},
		mounted() {
      this.navList.map(item=>{
        this.$set(item,'isCommonly',true)
      })
      this.list1.map((item, index1) => {
				this.$set(item, 'id', (index1 + 1))
				return item.navList.map((c, index) => {
					this.$set(c, 'id', (index + 1))
				})
			})
		},
		methods: {
			//编辑状态
			onEdit() {
				this.edit = !this.edit
			},
			//删除状态
			onDel(item,index) {
				if (this.edit) {
          //如果有有isCommonly,则为常用的
          if(item.isCommonly){
            const {icon, id, isCommonly, title, url} = item
            this.navList.splice(index, 1)
            this.list1[this.list1.length-1].navList.push({
              id,
              title,
              icon,
              url,
              isCommonly
            })

          } else {
            const pt = this.navList[index]
            const {
              pageIndex,
              childIndex,
              id,
              title,
              icon,
              url
            } = pt
            if (this.list1[pageIndex]) {
              this.navList.splice(index, 1)
              this.list1[pageIndex].navList.splice(childIndex, pageIndex,

                  {
                    id,
                    title,
                    icon,
                    url
                  })
            }

          }
				}
			},
			//添加
			onAdd(a, b) {
				if (this.edit) {
					this.navList.push({
						id: this.list1[a].navList[b].id,
						title: this.list1[a].navList[b].title,
						icon: this.list1[a].navList[b].icon, //控制定位的icon
						url: this.list1[a].navList[b].url, //所要跳转的url地址
						name: this.list1[a].leftName,
						pageIndex: a,
						childIndex: b,
					})
					this.list1[a].navList.splice(b, 1)
				}
			}
		}
	}
</script>
```
