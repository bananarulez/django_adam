# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cvut(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    fond2 = models.TextField(db_column='Fond2', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse('data_detail', kwargs={'pk': self.pk})
	
    class Meta:
        managed = False
        db_table = 'cvut'

    class ReadonlyMeta:
        readonly = ["fond"]

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['fond']
        return []


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Eu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    fond2 = models.TextField(db_column='Fond2', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eu'


class Fondy(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_fondu = models.TextField(db_column='ID_fondu')  # Field name made lowercase.
    cesta = models.TextField()
    fond = models.TextField()
    popis_fondu = models.TextField()
    pouzito = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fondy'


class Hk(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hk'


class Kiliankovi(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kiliankovi'


class Menclovi(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menclovi'


class NabDum(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tdum = models.CharField(db_column='Tdum', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_dum'


class NabFond(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tfond = models.CharField(db_column='Tfond', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_fond'


class NabJednotka(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tjednotka = models.CharField(db_column='Tjednotka', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_jednotka'


class NabKlasif(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tklasif = models.CharField(db_column='Tklasif', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_klasif'


class NabKraj(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tkraj = models.CharField(db_column='Tkraj', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_kraj'


class NabMaterial(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tmaterial = models.CharField(db_column='Tmaterial', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_material'


class NabOkres(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tokres = models.CharField(db_column='Tokres', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_okres'


class NabStat(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tstat = models.CharField(db_column='Tstat', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_stat'


class NabUcel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tucel = models.CharField(db_column='Tucel', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nab_ucel'


class Nm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    fond2 = models.TextField(db_column='Fond2', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nm'


class Oae(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.DateField(db_column='Datum_zprac', blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oae'


class Obrfond(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'obrfond'


class Pekar(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pekar'


class Plany(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plany'


class SiteUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=41)
    admin_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'site_user'


class SiteUserInfo(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    mobil = models.CharField(max_length=20)
    eu_fond1 = models.IntegerField()
    eu_fond2 = models.IntegerField()
    eu_fond3 = models.IntegerField()
    eu_fond4 = models.IntegerField()
    eu_fond5 = models.IntegerField()
    eu_fond6 = models.IntegerField()
    eu_fond7 = models.IntegerField()
    eu_fond8 = models.IntegerField()
    eu_fond9 = models.IntegerField()
    eu_fond10 = models.IntegerField()
    nm_fond1 = models.IntegerField()
    nm_fond2 = models.IntegerField()
    nm_fond3 = models.IntegerField()
    nm_fond4 = models.IntegerField()
    nm_fond5 = models.IntegerField()
    nm_fond6 = models.IntegerField()
    nm_fond7 = models.IntegerField()
    nm_fond8 = models.IntegerField()
    nm_fond9 = models.IntegerField()
    nm_fond10 = models.IntegerField()
    nm_fond11 = models.IntegerField()
    nm_fond12 = models.IntegerField()
    nm_fond13 = models.IntegerField()
    nm_fond14 = models.IntegerField()
    nm_fond15 = models.IntegerField()
    log_err = models.IntegerField()
    ad_level = models.IntegerField()
    blocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'site_user_info'


class Stranska(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stranska'


class Studna(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studna'


class Uluv(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    instituce = models.CharField(db_column='Instituce', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fond = models.CharField(db_column='Fond', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inventarni_cislo = models.CharField(db_column='Inventarni_cislo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signatura = models.CharField(db_column='Signatura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inkrement = models.CharField(db_column='Inkrement', max_length=20, blank=True, null=True)  # Field name made lowercase.
    karton_ulozeni = models.CharField(db_column='Karton_ulozeni', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lokalita = models.CharField(db_column='Lokalita', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puv_nazev = models.CharField(db_column='Puv_nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obec = models.CharField(db_column='Obec', max_length=50, blank=True, null=True)  # Field name made lowercase.
    okres = models.CharField(db_column='Okres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='Stat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gps = models.CharField(db_column='GPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zakladni_klasifikace = models.CharField(db_column='Zakladni_klasifikace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_ucel = models.CharField(db_column='Objekt_ucel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    objekt_material = models.CharField(db_column='Objekt_material', max_length=50, blank=True, null=True)  # Field name made lowercase.
    narodopisna_oblast = models.CharField(db_column='Narodopisna_oblast', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_domu = models.CharField(db_column='Typ_domu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    popis_objektu = models.TextField(db_column='Popis_objektu', blank=True, null=True)  # Field name made lowercase.
    poznamka_doplnek = models.TextField(db_column='Poznamka_doplnek', blank=True, null=True)  # Field name made lowercase.
    evid_jednotka = models.CharField(db_column='Evid_jednotka', max_length=100, blank=True, null=True)  # Field name made lowercase.
    negativ = models.IntegerField(db_column='Negativ', blank=True, null=True)  # Field name made lowercase.
    rozmer = models.CharField(db_column='Rozmer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zobrazeni = models.TextField(db_column='Zobrazeni', blank=True, null=True)  # Field name made lowercase.
    barva = models.CharField(db_column='Barva', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stav = models.CharField(db_column='Stav', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_vzniku = models.CharField(db_column='Datum_vzniku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autor = models.TextField(db_column='Autor', blank=True, null=True)  # Field name made lowercase.
    poznamka_autor = models.TextField(db_column='Poznamka_autor', blank=True, null=True)  # Field name made lowercase.
    publikace = models.TextField(db_column='Publikace', blank=True, null=True)  # Field name made lowercase.
    rozsah_souboru = models.TextField(db_column='Rozsah_souboru', blank=True, null=True)  # Field name made lowercase.
    zpracovatel_zaznamu = models.CharField(db_column='Zpracovatel_zaznamu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datum_zprac = models.CharField(db_column='Datum_zprac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snimek = models.TextField(db_column='Snimek', blank=True, null=True)  # Field name made lowercase.
    poznamka = models.TextField(db_column='Poznamka', blank=True, null=True)  # Field name made lowercase.
    negativ_rozmer_mat = models.CharField(db_column='Negativ_rozmer_mat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poznamka_dokument = models.TextField(db_column='Poznamka_dokument', blank=True, null=True)  # Field name made lowercase.
    snimek_cesta = models.TextField(db_column='Snimek_cesta', blank=True, null=True)  # Field name made lowercase.
    tmp4 = models.TextField(db_column='TMP4', blank=True, null=True)  # Field name made lowercase.
    tmp5 = models.TextField(db_column='TMP5', blank=True, null=True)  # Field name made lowercase.
    gps_sirka = models.FloatField(db_column='GPS_sirka', blank=True, null=True)  # Field name made lowercase.
    gps_delka = models.FloatField(db_column='GPS_delka', blank=True, null=True)  # Field name made lowercase.
    gps_presne = models.IntegerField(db_column='GPS_presne', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uluv'
