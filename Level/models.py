from django.db import models

class Level(models.Model):
    ORIENTATION_CHOICES = [
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
    ]

    level_number = models.IntegerField(unique=True)
    math_question = models.CharField(max_length=255,blank=True, null=True)
    riddle_question = models.CharField(max_length=255,blank=True, null=True)
    answer = models.IntegerField()
    hint = models.TextField(blank=True, null=True)
    image_question = models.ImageField(upload_to='level_images/', blank=True, null=True)
    riddle_pattern = models.CharField(max_length=255, blank=True, null=True)
    question_orientation = models.CharField(max_length=10, choices=ORIENTATION_CHOICES, default='horizontal')

    def __str__(self):
        return f"Level {self.level_number}"
