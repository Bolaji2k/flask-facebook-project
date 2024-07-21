from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from ..models.models import User, Group, db

admin = Admin(name='Facebook', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Group, db.session))