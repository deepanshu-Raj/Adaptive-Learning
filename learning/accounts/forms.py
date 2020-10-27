from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

# for not a valid email-address.
class EmailValidationOnForgotPassword(PasswordResetForm):

	def clean_email(self):
		
		email = self.cleaned_data['email']
		if not User.objects.filter(email__iexact=email,is_active=True).exists():
			msg = ('There is no User registered with the specified E-mail address.')
			self.add_error('email',msg)
		return email