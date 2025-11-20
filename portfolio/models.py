from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Percentage (0-100)")
    icon_class = models.CharField(max_length=50, help_text="FontAwesome or similar icon class", blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=200, help_text="Comma separated technologies")
    live_link = models.URLField(blank=True)
    repo_link = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fas fa-briefcase", help_text="FontAwesome icon class")
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    use_logo = models.BooleanField(default=False, help_text="Check to use the uploaded logo instead of the icon")

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.CharField(max_length=20) # e.g., "2018 - 2022"
    icon_class = models.CharField(max_length=50, default="fas fa-graduation-cap", help_text="FontAwesome icon class")
    institution_logo = models.ImageField(upload_to='institution_logos/', blank=True, null=True)
    use_logo = models.BooleanField(default=False, help_text="Check to use the uploaded logo instead of the icon")

    def __str__(self):
        return self.degree

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(blank=True)
    icon_class = models.CharField(max_length=50, default="fas fa-certificate", help_text="FontAwesome icon class")
    certification_logo = models.ImageField(upload_to='certification_logos/', blank=True, null=True)
    use_logo = models.BooleanField(default=False, help_text="Check to use the uploaded logo instead of the icon")

    def __str__(self):
        return self.name
