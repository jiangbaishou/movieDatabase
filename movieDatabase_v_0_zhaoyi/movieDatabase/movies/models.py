from django.db import models

# Create your models here.
class MatchAll(models.Model):
    movieid = models.AutoField(db_column='movieId', primary_key=True)  # Field name made lowercase.
    moviename = models.CharField(db_column='movieName', max_length=255, blank=True, null=True)  # Field name made low                                                                                                                        ercase.
    moviename_en = models.CharField(db_column='movieName_en', max_length=255, blank=True, null=True)  # Field name ma                                                                                                                        de lowercase.
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, null=True)
    maoyanid = models.IntegerField(db_column='maoyanId', blank=True, null=True)  # Field name made lowercase.
    cboooid = models.IntegerField(db_column='cboooId', blank=True, null=True)  # Field name made lowercase.
    doubanmovieid = models.IntegerField(db_column='doubanMovieId', blank=True, null=True)  # Field name made lowercas                                                                                                                        e.
    mtimeid = models.IntegerField(db_column='mtimeId', blank=True, null=True)  # Field name made lowercase.
    taobaoid = models.IntegerField(db_column='taobaoId', blank=True, null=True)  # Field name made lowercase.
    wepiaoid = models.IntegerField(db_column='wepiaoId', blank=True, null=True)  # Field name made lowercase.
    weiboid = models.BigIntegerField(db_column='weiboId', blank=True, null=True)  # Field name made lowercase.
    franchiseid = models.IntegerField(db_column='franchiseId', blank=True, null=True)  # Field name made lowercase.
    imdbid = models.CharField(db_column='imdbId', max_length=500, blank=True, null=True)  # Field name made lowercase                                                                                                                        .
    boxofficemojoid = models.CharField(db_column='boxofficemojoId', max_length=500, blank=True, null=True)  # Field n                                                                                                                        ame made lowercase.
    thenumbersid = models.CharField(db_column='theNumbersId', max_length=500, blank=True, null=True)  # Field name ma                                                                                                                        de lowercase.
    notes = models.TextField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_all'

