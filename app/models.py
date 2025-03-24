from django.db import models


# Create your models here.
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Person(SingletonModel):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, null=True)
    com_projects = models.IntegerField(null=True)
    awards = models.IntegerField(null=True)
    happy_customer = models.IntegerField(null=True)
    coffee_cup = models.IntegerField(null=True)
    website = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    image1 = models.ImageField(upload_to='portfolio/images/')
    image2 = models.ImageField(upload_to='portfolio/images/')
    document = models.FileField(upload_to='portfolio/documents/')

    def __str__(self):
        return self.name


class Background(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    duration = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    position = models.PositiveIntegerField(default=0)
    short_description = models.TextField(blank=True, null=True)  # Added short description
    technologies = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated list of technologies used.") # Added technologies
    github_url = models.URLField(blank=True, null=True) # Added github_url

    class Meta:
        ordering = ['position']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        else:
            return [] #returns empty list if technologies are null.



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
