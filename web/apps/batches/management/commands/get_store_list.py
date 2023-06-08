import requests
import csv
import json
import pandas as pd

url = "https://map.seoul.go.kr/smgis/apps/theme.do"
headers = {"User-Agent": "Mozilla/5.0"}


res = requests.get(
    url,
    headers=headers,
    data={
        "cmd": "getContentsList",
        "key": "5a9e3f209e3047b484a2600fe048a8b8",
        "page_size": "300",
        "page_no": "1",
        "coord_x": "126.974695",
        "coord_y": "37.564150",
        "distance": "20000",
        "search_type": "1",
        "search_name": "",
        "theme_id": "11103395",
        "content_id": "",
        "subcate_id": "",
    },
)

result = res.json()
data = result["body"]


coord_x = []
coord_y = []
conts_name = []
dist = []
nation_point_number = []
nation_base_area = []
tel_no = []
conts_stat = []
value_01 = []
dong_name = []
reg_date = []
extra_name = []
coord_data = []
mbr_min_x = []
theme_name = []
mbr_min_y = []
conts_id = []
conts_lan_type = []
san_name = []
line_pattern = []
theme_type = []
line_color = []
thm_coord_type = []
update_date = []
mbr_max_x = []
theme_id = []
mbr_max_y = []
extra_data_01 = []
img_main_url = []
gu_name = []
line_weight = []
theme_sub_id = []
slave_id = []
rnum = []
addr_full_new = []
kw = []
coord_type = []
addr_full_old = []
master_no = []


for i in data:
    COT_COORD_X = i["COT_COORD_X"]
    coord_x.append(COT_COORD_X)
    COT_COORD_Y = i["COT_COORD_Y"]
    coord_y.append(COT_COORD_Y)
    COT_CONTS_NAME = i["COT_CONTS_NAME"]
    conts_name.append(COT_CONTS_NAME)
    DIST = i["DIST"]
    dist.append(DIST)
    COT_NATION_POINT_NUMBER = i["COT_NATION_POINT_NUMBER"]
    nation_point_number.append(COT_NATION_POINT_NUMBER)
    COT_NATION_BASE_AREA = i["COT_NATION_BASE_AREA"]
    nation_base_area.append(COT_NATION_BASE_AREA)
    COT_TEL_NO = i["COT_TEL_NO"]
    tel_no.append(COT_TEL_NO)
    COT_CONTS_STAT = i["COT_CONTS_STAT"]
    conts_stat.append(COT_CONTS_STAT)
    COT_VALUE_01 = i["COT_VALUE_01"]
    value_01.append(COT_VALUE_01)
    COT_DONG_NAME = i["COT_DONG_NAME"]
    dong_name.append(COT_DONG_NAME)
    COT_REG_DATE = i["COT_REG_DATE"]
    reg_date.append(COT_REG_DATE)
    COT_EXTRA_NAME = i["COT_EXTRA_NAME"]
    extra_name.append(COT_EXTRA_NAME)
    COT_COORD_DATA = i["COT_COORD_DATA"]
    coord_data.append(COT_COORD_DATA)
    COT_MBR_MIN_X = i["COT_MBR_MIN_X"]
    mbr_min_x.append(COT_MBR_MIN_X)
    THM_THEME_NAME = i["THM_THEME_NAME"]
    theme_name.append(THM_THEME_NAME)
    COT_MBR_MIN_Y = i["COT_MBR_MIN_Y"]
    mbr_min_y.append(COT_MBR_MIN_Y)
    COT_CONTS_ID = i["COT_CONTS_ID"]
    conts_id.append(COT_CONTS_ID)
    COT_CONTS_LAN_TYPE = i["COT_CONTS_LAN_TYPE"]
    conts_lan_type.append(COT_CONTS_LAN_TYPE)
    COT_SAN_NAME = i["COT_SAN_NAME"]
    san_name.append(COT_SAN_NAME)
    COT_LINE_PATTERN = i["COT_LINE_PATTERN"]
    THM_THEME_TYPE = i["THM_THEME_TYPE"]
    theme_type.append(THM_THEME_TYPE)
    COT_LINE_COLOR = i["COT_LINE_COLOR"]
    line_color.append(COT_LINE_COLOR)
    THM_COORD_TYPE = i["THM_COORD_TYPE"]
    thm_coord_type.append(THM_COORD_TYPE)
    COT_UPDATE_DATE = i["COT_UPDATE_DATE"]
    update_date.append(COT_UPDATE_DATE)
    COT_MBR_MAX_X = i["COT_MBR_MAX_X"]
    mbr_max_x.append(COT_MBR_MAX_X)
    COT_THEME_ID = i["COT_THEME_ID"]
    theme_id.append(COT_THEME_ID)
    COT_MBR_MAX_Y = i["COT_MBR_MAX_Y"]
    mbr_max_y.append(COT_MBR_MAX_Y)
    COT_EXTRA_DATA_01 = i["COT_EXTRA_DATA_01"]
    extra_data_01.append(COT_EXTRA_DATA_01)
    COT_IMG_MAIN_URL = i["COT_IMG_MAIN_URL"]
    img_main_url.append(COT_IMG_MAIN_URL)
    COT_GU_NAME = i["COT_GU_NAME"]
    gu_name.append(COT_GU_NAME)
    COT_LINE_WEIGHT = i["COT_LINE_WEIGHT"]
    line_weight.append(COT_LINE_WEIGHT)
    COT_THEME_SUB_ID = i["COT_THEME_SUB_ID"]
    theme_sub_id.append(COT_THEME_SUB_ID)
    COT_SLAVE_NO = i["COT_SLAVE_NO"]
    slave_id.append(COT_SLAVE_NO)
    RNUM = i["RNUM"]
    rnum.append(RNUM)
    COT_ADDR_FULL_NEW = i["COT_ADDR_FULL_NEW"]
    addr_full_new.append(COT_ADDR_FULL_NEW)
    COT_KW = i["COT_KW"]
    kw.append(COT_KW)
    COT_COORD_TYPE = i["COT_COORD_TYPE"]
    coord_type.append(COT_COORD_TYPE)
    COT_ADDR_FULL_OLD = i["COT_ADDR_FULL_OLD"]
    addr_full_old.append(COT_ADDR_FULL_OLD)
    COT_MASTER_NO = i["COT_MASTER_NO"]
    master_no.append(COT_MASTER_NO)

lists = {
    "COT_COORD_X": coord_x,
    "COT_COORD_Y": coord_y,
    "COT_CONTS_NAME": conts_name,
    "DIST": dist,
    "COT_NATION_POINT_NUMBER": nation_point_number,
    "COT_NATION_BASE_AREA": nation_base_area,
    "COT_TEL_NO": tel_no,
    "COT_CONTS_STAT": conts_stat,
    "COT_VALUE_01": value_01,
    "COT_DONG_NAME": dong_name,
    "COT_REG_DATE": reg_date,
    "COT_EXTRA_NAME": extra_name,
    "COT_COORD_DATA": coord_data,
    "COT_MBR_MIN_X": mbr_min_x,
    "THM_THEME_NAME": theme_name,
    "COT_MBR_MIN_Y": mbr_min_y,
    "COT_CONTS_ID": conts_id,
    "COT_CONTS_LAN_TYPE": conts_lan_type,
    "COT_SAN_NAME": san_name,
    "THM_THEME_TYPE": theme_type,
    "COT_LINE_COLOR": line_color,
    "THM_COORD_TYPE": thm_coord_type,
    "COT_UPDATE_DATE": update_date,
    "COT_MBR_MAX_X": mbr_max_x,
    "COT_THEME_ID": theme_id,
    "COT_MBR_MAX_Y": mbr_max_y,
    "COT_EXTRA_DATA_01": extra_data_01,
    "COT_IMG_MAIN_URL": img_main_url,
    "COT_GU_NAME": gu_name,
    "COT_LINE_WEIGHT": line_weight,
    "COT_THEME_SUB_ID": theme_sub_id,
    "COT_SLAVE_NO": slave_id,
    "RNUM": rnum,
    "COT_ADDR_FULL_NEW": addr_full_new,
    "COT_KW": kw,
    "COT_COORD_TYPE": coord_type,
    "COT_ADDR_FULL_OLD": addr_full_old,
    "COT_MASTER_NO": master_no,
}

df = pd.DataFrame(lists)
df.to_csv("seeder_stores.csv", encoding="utf-8-sig")
