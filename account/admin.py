from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from .forms import UserAdminCreationForm, UserAdminChangeForm


class AccountAdmin(UserAdmin):
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm



	fieldsets = ((None, {'fields': ('email', 'username' 'password')}),
	('Personal info', {'fields': ()}),
	('Permissions', {'fields': ()}),
    )

	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()

	add_fieldsets = (
	(None, {
	'classes': ('wide',),
	'fields': ('email', 'password1', 'password2', 'username', )}
        ), )





admin.site.register(Account, AccountAdmin)