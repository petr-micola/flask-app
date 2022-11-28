from flask_appbuilder import ModelView
from flask_appbuilder.fields import QuerySelectField
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Employee


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ["id", "full_name", "year"]


    show_template = "appbuilder/general/model/show_cascade.html"

db.create_all()

appbuilder.add_view(
    EmployeeView, "Employees", icon="fa-folder-open-o", category="Company"
)
