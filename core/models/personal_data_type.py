import reversion
from .utils import CoreModel, TextFieldWithInputWidget

@reversion.register()
class PersonalDataType(CoreModel):
    """
    Represents categories of personal data.

    """

    class Meta:
        app_label = 'core'
        get_latest_by = "added"
        ordering = ['name']

    code = TextFieldWithInputWidget(max_length=20,
                                    blank=False,
                                    verbose_name='Code', unique=True)

    name = TextFieldWithInputWidget(max_length=120,
                                    blank=False,
                                    verbose_name='Name', unique=True)

    def __str__(self):
        return self.name
