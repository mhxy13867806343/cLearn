import requests
from pyquery import PyQuery as pq
import re  #正则表达式
host='https://www.douyin.com/share/video/'
headers={
'cookie': 'ttwid=1%7CwyqlQmTqpptjyoopQyeCsezR_fDquzcD_-7tqVAUk6g%7C1661825561%7Cfbc1389c308d71af070183f1a68f16474c7e7396655514300269dfad1956e9af; douyin.com; strategyABtestKey=1661825581.538; s_v_web_id=verify_l7fk1lco_4ngfHZeO_tLzF_4w1H_BSta_rV3LYbEyxky0; passport_csrf_token=bad6f050f7738d8bb655e99e02a93088; passport_csrf_token_default=bad6f050f7738d8bb655e99e02a93088; odin_tt=131ad3d1ecf03dc87d7959c8990779c94d176b9d3f4817daa4210f31d6f74245f2ee0a1e3c672ca3d6fad5cfc52ec23c22f203b0ca27b5c57ab9163bddb24895; SEARCH_RESULT_LIST_TYPE=%22multi%22; ttcid=8496e17ce99c48e198e031195ea913b936; _tea_utm_cache_1243=undefined; MONITOR_WEB_ID=d7bfdb15-b34d-4f90-b74f-b6ac37ea0618; THEME_STAY_TIME=%22299596%22; IS_HIDE_THEME_CHANGE=%221%22; _tea_utm_cache_2018=undefined; n_mh=KhhWMccGLN1ZCEWbsmulZ-_tEQ9oBty4fS3R6cEsOto; sid_guard=d94c1c6a49bb3e049b4b5c275fe1b474%7C1661826929%7C5184000%7CSat%2C+29-Oct-2022+02%3A35%3A29+GMT; uid_tt=fff9e1fd4eab023aaa70d37496f4aacd; uid_tt_ss=fff9e1fd4eab023aaa70d37496f4aacd; sid_tt=d94c1c6a49bb3e049b4b5c275fe1b474; sessionid=d94c1c6a49bb3e049b4b5c275fe1b474; sessionid_ss=d94c1c6a49bb3e049b4b5c275fe1b474; sid_ucp_v1=1.0.0-KDc4NDkzNmYyY2I0NzdiYmFlZjAyNzc4NWExNzQ4NzgxYmVhMzIzMWMKFQivuY36qAIQ8e61mAYY2wk4AkDxBxoCbGYiIGQ5NGMxYzZhNDliYjNlMDQ5YjRiNWMyNzVmZTFiNDc0; ssid_ucp_v1=1.0.0-KDc4NDkzNmYyY2I0NzdiYmFlZjAyNzc4NWExNzQ4NzgxYmVhMzIzMWMKFQivuY36qAIQ8e61mAYY2wk4AkDxBxoCbGYiIGQ5NGMxYzZhNDliYjNlMDQ5YjRiNWMyNzVmZTFiNDc0; __ac_signature=_02B4Z6wo00f01cqJ2CAAAIDAskczJ20bMdHKqdyAABGxzibI1WFMKwxqeYb6w0ub5278jnjYTlsi6Cu5wonikXOV.zCsBIQLUfviMTussUjsdv5JdCui-tW-QdL9WWlfUlh.vHjDxl9GZdGl88; download_guide=%223%2F20220830%22; __ac_nonce=0630d89b000fe6686376d; home_can_add_dy_2_desktop=%221%22; msToken=HX2J3eM2PV8vcYbOtEfK8RNEspWylg2DOmeYKrQrZk-crBiVSsBXpcOq-Ge5aUSnpyyGxXCxc3MdTghOIwmBrx7YqUIGFeDbxNpxlyFMd0OEytNZmcWFr5Pbkiagsr0=; msToken=e9IuHgChY_FvGxct5BLHyeeboG3VC_GynaqNWIsrTKQKPIleVr-44ukEcW0woHRhVEiv5gnlTc2x1Wsl94hdd5secYpQ81a22OA-P35AvZ9KuuG6yJ_WyNjEJdm11Bo=; tt_scid=SGCI5tdX3rdoHO7pVhuWIpNCQg2Be2KmepsLztSnJTg.tzn8C5loLErPjn7iljL01d22',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/104.0.5112.102'
}
def getDY(path):
    req=requests.get(path,headers=headers)
    title =pq(req.text).find('title').text()
    script=pq(req.text).val('#RENDER_DATA')
    reg1 = re.compile('Fplaywm%2F%3Fvideo_id%3D(\w+.)%26')
    id1=reg1.findall(req.text)[0]
    reg2 = re.compile('26ratio%3D(\w+.)p%26')
    id2=reg2.findall(req.text)[0]
    reg3 = re.compile('%26line%3D(\w+.)')
    id3=str(reg3.findall(req.text)[0]).replace('%','')
    url=f'{host}aweme/v1/playwm?video_id={id1}&ratio=${id2}&line={id3}'
    const=requests.get(url,headers=headers)
    with open(f'./{title}.mp4','wb') as f:
        f.write(const.content)
getDY(f'{host}6978322368745852171')
