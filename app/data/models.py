from django.db import models

class Aktualnosc(models.Model):
	def __unicode__(self):
		return self.tytul
	def get_absolute_url(self):
		return "/nowosci/%i/" % self.id
	tytul = models.CharField(max_length=200)
	tekst = models.TextField()
	data_wydarzenia = models.DateTimeField(blank = True, null = True)
	pub_date = models.DateTimeField(auto_now = True)
	
class Strona(models.Model):
	def __unicode__(self):
		return self.tytul
	def get_absolute_url(self):
		return "/strony/%i/" % self.id
	tytul = models.CharField(max_length=200)
	tekst = models.TextField()
	pub_date = models.DateTimeField(auto_now = True)
	class Media:
		js = ("/admin/tiny_mce/tiny_mce.js", "/admin/js/textareas.js",)

class MenuPrawe(models.Model):
	def __unicode__(self):
		return self.nazwa
	nazwa = models.CharField(max_length=100)
	strona = models.ForeignKey(Strona, related_name='+', blank = True, null = True)

class PodMenuPrawe(models.Model):
	def __unicode__(self):
		return self.nazwa
	nazwa = models.CharField(max_length=100)
	parent = models.ForeignKey(MenuPrawe, related_name='pod_menu')
	strona = models.ForeignKey(Strona, related_name='+')

class MenuGorne(models.Model):
	def __unicode__(self):
		return str(self.numer) + ' : ' + self.nazwa
	nazwa = models.CharField(max_length=100)
	opis = models.CharField(max_length=200)
	strona = models.ForeignKey(Strona, related_name='+')
	numer = models.IntegerField()