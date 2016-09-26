from django.db import models

# Create your models here.
class MatchAll(models.Model):
	movieid = models.AutoField(db_column='movieId', primary_key=True)  # Field name made lowercase.
	moviename = models.CharField(db_column='movieName', max_length=255, blank=True, null=True)  # Field name made low																														ercase.
	moviename_en = models.CharField(db_column='movieName_en', max_length=255, blank=True, null=True)  # Field name ma																														de lowercase.
	releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
	id = models.IntegerField(blank=True, null=True)
	maoyanid = models.IntegerField(db_column='maoyanId', blank=True, null=True)  # Field name made lowercase.
	cboooid = models.IntegerField(db_column='cboooId', blank=True, null=True)  # Field name made lowercase.
	doubanmovieid = models.IntegerField(db_column='doubanMovieId', blank=True, null=True)  # Field name made lowercas																														e.
	mtimeid = models.IntegerField(db_column='mtimeId', blank=True, null=True)  # Field name made lowercase.
	taobaoid = models.IntegerField(db_column='taobaoId', blank=True, null=True)  # Field name made lowercase.
	wepiaoid = models.IntegerField(db_column='wepiaoId', blank=True, null=True)  # Field name made lowercase.
	weiboid = models.BigIntegerField(db_column='weiboId', blank=True, null=True)  # Field name made lowercase.
	franchiseid = models.IntegerField(db_column='franchiseId', blank=True, null=True)  # Field name made lowercase.
	imdbid = models.CharField(db_column='imdbId', max_length=500, blank=True, null=True)  # Field name made lowercase																														.
	boxofficemojoid = models.CharField(db_column='boxofficemojoId', max_length=500, blank=True, null=True)  # Field n																														ame made lowercase.
	thenumbersid = models.CharField(db_column='theNumbersId', max_length=500, blank=True, null=True)  # Field name ma																														de lowercase.
	notes = models.TextField(blank=True, null=True)
	timestamp = models.BigIntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'match_all'


#movie detail
class MovieDetail(models.Model):
	movieid = models.IntegerField(db_column='movieId', primary_key = True)  # Field name made lowercase.
	moviename = models.CharField(db_column='movieName', max_length=255, blank=True, null=True)  # Field name made lowercase.
	releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
	maoyanid = models.IntegerField(db_column='maoyanId', blank=True, null=True)  # Field name made lowercase.
	cboooid = models.IntegerField(db_column='cboooId', blank=True, null=True)  # Field name made lowercase.
	doubanmovieid = models.IntegerField(db_column='doubanMovieId', blank=True, null=True)  # Field name made lowercase.
	language = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)
	genre = models.CharField(max_length=255, blank=True, null=True)
	alias = models.CharField(max_length=255, blank=True, null=True)
	tag = models.CharField(max_length=255, blank=True, null=True)
	synopsis = models.TextField(blank=True, null=True)
	maoyanratingscore = models.FloatField(db_column='maoyanRatingScore', blank=True, null=True)  # Field name made lowercase.
	maoyanratingnum = models.FloatField(db_column='maoyanRatingNum', blank=True, null=True)  # Field name made lowercase.
	wishnum_maoyan = models.FloatField(db_column='wishNum_maoyan', blank=True, null=True)  # Field name made lowercase.
	duration = models.FloatField(blank=True, null=True)
	format = models.CharField(max_length=255, blank=True, null=True)
	gross = models.FloatField(blank=True, null=True)
	male = models.FloatField(blank=True, null=True)
	female = models.FloatField(blank=True, null=True)
	age_11_15 = models.FloatField(blank=True, null=True)
	age_16_20 = models.FloatField(blank=True, null=True)
	age_21_25 = models.FloatField(blank=True, null=True)
	age_26_30 = models.FloatField(blank=True, null=True)
	age_31_35 = models.FloatField(blank=True, null=True)
	age_36_40 = models.FloatField(blank=True, null=True)
	age_40_50 = models.FloatField(blank=True, null=True)
	timestamp = models.BigIntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'movie_detail'
#end of movie detail


#movie people
class MoviePeople(models.Model):
	movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
	cboooid = models.IntegerField(db_column='cboooId', blank=True, null=True)  # Field name made lowercase.
	name = models.TextField(blank=True, null=True)
	peopleid = models.IntegerField(db_column='peopleId', blank=True, null=True)  # Field name made lowercase.
	role = models.CharField(max_length=255, blank=True, null=True)
	timestamp = models.BigIntegerField(blank=True, null=True)
	id = models.IntegerField(db_column = 'id', primary_key = True)

	class Meta:
		managed = False
		db_table = 'movie_people'
#end of movie people



#movie company
class MovieCompany(models.Model):
	movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
	cboooid = models.IntegerField(db_column='cboooId', blank=True, null=True)  # Field name made lowercase.
	company = models.TextField(blank=True, null=True)
	companyid = models.IntegerField(db_column='companyId', blank=True, null=True)  # Field name made lowercase.
	role = models.CharField(max_length=255, blank=True, null=True)
	timestamp = models.BigIntegerField(blank=True, null=True)
	id = models.IntegerField(db_column = 'id', primary_key = True)

	class Meta:
		managed = False
		db_table = 'movie_company'
#end of movie company


#movie daily
class MovieDaily(models.Model):
    movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    maoyanid = models.IntegerField(db_column='maoyanId', blank=True, null=True)  # Field name made lowercase.
    showdate = models.DateField(db_column='showDate', blank=True, null=True)  # Field name made lowercase.
    sumboxoffice = models.FloatField(db_column='sumBoxoffice', blank=True, null=True)  # Field name made lowercase.
    dailyboxoffice = models.FloatField(db_column='dailyBoxoffice', blank=True, null=True)  # Field name made lowercase.
    totalshow = models.FloatField(db_column='totalShow', blank=True, null=True)  # Field name made lowercase.
    totalviewer = models.FloatField(db_column='totalViewer', blank=True, null=True)  # Field name made lowercase.
    attendrate = models.FloatField(db_column='attendRate', blank=True, null=True)  # Field name made lowercase.
    avgpeople = models.FloatField(db_column='avgPeople', blank=True, null=True)  # Field name made lowercase.
    avgprice = models.FloatField(db_column='avgPrice', blank=True, null=True)  # Field name made lowercase.
    boxrate = models.FloatField(db_column='boxRate', blank=True, null=True)  # Field name made lowercase.
    seatrate = models.FloatField(db_column='seatRate', blank=True, null=True)  # Field name made lowercase.
    showrate = models.FloatField(db_column='showRate', blank=True, null=True)  # Field name made lowercase.
    totalbox = models.FloatField(db_column='totalBox', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.BigIntegerField(blank=True, null=True)
    id = models.IntegerField(db_column = 'id', primary_key = True)

    class Meta:
        managed = False
        db_table = 'movie_daily'
#end of movie daily
