from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp

class ContactForm(FlaskForm):
    name = StringField(
        'Name', 
        validators=[
            DataRequired(message="Name is required."),
            Length(min=2, max=50, message="Name must be between 2 and 50 characters."),
            Regexp(r'^[A-Za-z\s]+$', message="Name must contain only letters and spaces.")
        ]
    )

    phone = StringField(
        'Phone',
        validators=[
            DataRequired(message="Phone number is required."),
            Length(min=7, max=15, message="Phone number must be between 7 and 15 digits."),
            Regexp(r'^\d+$', message="Phone number must contain only digits.")
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email format.")
        ]
    )

    type = SelectField(
        'Type', 
        choices=[('Personal', 'Personal'), ('Business', 'Business')],
        validators=[DataRequired(message="Contact type is required.")]
    )

    submit = SubmitField('Save')
