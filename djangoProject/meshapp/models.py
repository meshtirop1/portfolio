from django.db import models


class Project(models.Model):

    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('incomplete', 'Incomplete'),
        ('school', 'School'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10,
                              choices=(('completed', 'Completed'), ('incomplete', 'Incomplete'), ('school', 'School')))
    github_url = models.URLField(max_length=200, blank=True, null=True)
    start_date = models.DateField(verbose_name="Start Date", null=True, blank=True)
    end_date = models.DateField(verbose_name="End Date", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.description
