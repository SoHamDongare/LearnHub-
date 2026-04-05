from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
class Course(models.Model):
    course_CHOICES = [
        ('Development', 'Development'),
        ('Testing', 'Testing'),
        ('Data analytics', 'Data analytics'),
        ('Data science', 'Data science'),
        ('Devops', 'Devops'),
    ]
    name=models.CharField( max_length=200)
    description=models.TextField(max_length=1000)
    price=models.IntegerField()
    rating=models.FloatField(default=0)
    duration = models.IntegerField()    
    category=models.CharField(max_length=100,choices=course_CHOICES)
    image=models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.name
    
class CourseRating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:

        unique_together = ('user', 'course')


    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        avg_rating = CourseRating.objects.filter(
            course=self.course
        ).aggregate(Avg('rating'))['rating__avg']

        self.course.rating = round(avg_rating, 1)

        self.course.save()