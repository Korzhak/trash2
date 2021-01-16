from django.db import models


class Flow(models.Model):
    name = models.CharField("Name of flow", max_length=200)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField("Name of spec.", max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField("Name of spec.", max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    key = models.IntegerField("Last 4 number of phone", primary_key=True)
    full_name = models.CharField("Full name", max_length=120)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    attendance = models.IntegerField("Attendance", default=90)
    academic_performance = models.FloatField("Academic performance", default=8)
    date_of_birth = models.DateField("Date of birth.")
    photo = models.ImageField("Avatar")

    crystals = models.IntegerField("crystals", default=400)
    coins = models.IntegerField("Coins", default=700)

    score = models.IntegerField("User Score", default=0)

    level_1 = models.BooleanField("L1 Done", default=False)
    level_2 = models.BooleanField("L2 Done", default=False)
    level_3 = models.BooleanField("L3 Done", default=False)
    level_4 = models.BooleanField("L4 Done", default=False)

    hint_1_level = models.TextField("Hint in 1 level", default="",
                                    max_length=500)
    hint_2_level = models.TextField("Hint in 2 level", default="",
                                    max_length=500)
    hint_3_level = models.TextField("Hint in 3 level", default="",
                                    max_length=500)
    hint_4_level = models.TextField("Hint in 4 level", default="",
                                    max_length=500)

    joke = models.TextField("Joke", blank=True)

    def __str__(self):
        return self.full_name


class Task(models.Model):
    description = models.TextField("Description task")

