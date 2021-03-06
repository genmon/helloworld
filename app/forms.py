
from flask import current_app
from flask_wtf import Form
from wtforms import TextField, SelectField, validators

validators = {
	'twitter_display_name': [
		validators.Required(),
		validators.Length(min=2, max=16),
		validators.Regexp(r'^@[a-zA-Z0-9_]{1,15}$', message='Twitter handles start with @ and then have only letters, numbers and underscores')
	],
	'twitter_id': [
		validators.Required(),
		validators.Length(min=1, max=16),
		validators.Regexp(r'^[0-9]{1,16}$', message='Twitter IDs are numbers')
	],
	'device_address': [
		validators.Required(),
		validators.Length(min=16, max=16, message="A device address must be 16 characters"),
		validators.Regexp(r'^[a-f0-9]{1,16}$', message='A device address contains only the numbers 0-9 and the lowercase letters a-f')
	]
}

class AddGroupMemberForm(Form):
	twitter_display_name = TextField('twitter_display_name', validators['twitter_display_name'], default='@twitter_name')

# @todo this needs to be validated against the actual list of mutual friends
class AddGroupMemberFromTwitterNameForm(Form):
	twitter_id = SelectField('twitter_id', validators['twitter_id'], choices=[])

class RemoveGroupMemberForm(Form):
	pass

class DoGlanceForm(Form):
	pass

class DeviceAddressForm(Form):
	device_address = TextField('device_address', validators['device_address'])