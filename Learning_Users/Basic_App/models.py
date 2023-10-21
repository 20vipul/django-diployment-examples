from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    """
    Model representing additional user profile information.

    This model is intended to extend the built-in User model from Django's
    authentication system. It creates a one-to-one relationship with the User
    model, allowing you to add additional fields specific to your application.

    Fields:
    - user: One-to-one relationship with the User model to associate the
      UserProfileInfo with a user account.
    - portfolio_site: An optional URLField where the user can provide a link
      to their portfolio or personal website. It allows for blank entries.
    - profile_pic: An ImageField to store the user's profile picture. The
      'upload_to' argument specifies the directory where the uploaded images
      will be stored, in this case, "Profile_Pics". It also allows for blank
      entries.

    Methods:
    - __str__: A string representation of the UserProfileInfo object, which is
      the username of the associated User. This makes it easier to display
      user information in the admin interface and other contexts.

    This model is often used to store additional user-specific information that
    is not covered by the basic User model, such as profile pictures and
    website links.

    Note: To use this model, you should have the Django User model configured
    properly. Make sure that 'AUTH_USER_MODEL' is set correctly in your
    project's settings to use a custom user model if needed.

    Example usage:
    user_profile = UserProfileInfo.objects.create(user=user_instance,
                                                 portfolio_site='https://example.com',
                                                 profile_pic='profile_image.jpg')
    """


    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #additional clases

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to="Profile_Pics",blank=True)

    def __str__(self):
        return self.user.username

