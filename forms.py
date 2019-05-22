from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

# reddit_search form.
class SearchForm(FlaskForm):
    search = StringField('Search Term', validators=[DataRequired()])
    time_select = SelectField('Time Filter', choices= [('all', 'All Time'), ('hour','Past Hour'), ('day', 'Past 24 Hours'), ('week', 'Past Week'), ('month', 'Past Month'), ('year', 'Past Year')])
    submit = SubmitField('Search')

# techmeme search form.
class TechmemeForm(FlaskForm):
    search = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search')