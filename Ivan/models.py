from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies used")
    date_created = models.DateField(auto_now_add=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order', '-date_created']
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    SKILL_LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=SKILL_LEVELS)
    proficiency_percentage = models.IntegerField(default=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order', 'category']
    
    def __str__(self):
        return f"{self.name} ({self.category})"


class About(models.Model):
    title = models.CharField(max_length=200, default="About Me")
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    resume_link = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "About"
    
    def __str__(self):
        return self.title
