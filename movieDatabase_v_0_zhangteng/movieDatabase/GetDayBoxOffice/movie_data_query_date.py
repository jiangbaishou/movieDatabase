import pandas
import datetime
import pymysql
import json

def data_deal(dateFrame):
	date_data = pandas.DataFrame(dateFrame)
	#单片数据
	movie_data = date_data[["movieName", 'releaseDate','boxoffice','personNum']].sort_index(by = 'boxoffice', ascending=False)[0:10]
	movie_data['releaseDate'] = movie_data['releaseDate'].astype("str")
	movie_Final = list(movie_data.to_dict('records'))
	#汇总数据
	all_data = date_data.groupby(['showDate']).agg({'boxoffice':'sum','personNum':'sum'})
	all_data.reset_index(level = [0],inplace = True)
	all_data['showDate'] = all_data['showDate'].astype("str")
	all_data_Final = list(all_data.to_dict('records'))
	#生成字典
	test1 = dict({'data1':movie_Final,'boxoffice':str(all_data['boxoffice'][0]),'personNum':str(all_data['personNum'][0])})
	#转成json格式
	json_Final = json.dumps(test1,ensure_ascii=False)
	return(json_Final)

def movie_data_query(data1):
	conn = pymysql.Connect(host = '',port = ,user = '',passwd = '',db = '',charset = 'utf8')
	#cur = conn.cursor()
	date_data = pandas.read_sql('select * from zzb_movieboxoffice where showDate = "' + data1 + '"',con = conn)
	conn.close()
	#处理数据
	request_data = data_deal(dateFrame = date_data)
	return(request_data)

def data_if_effective(data1):
	into_data = datetime.datetime.strptime(data1,'%Y-%m-%d')
	locol_data = datetime.datetime.today()
	if into_data > locol_data:
		message = "Sorry ,The date entered is greater than the local time."
		return(message)
	else :
		request_data = movie_data_query(data1 = data1)
		return(request_data)
