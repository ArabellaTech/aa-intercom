from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from aa_intercom.exceptions import UnsupportedIntercomEventType
from aa_intercom.mixins import IntercomUserMixin
from aa_intercom.models import AbstractIntercomEvent
from aa_intercom.signals import account_post_save, intercom_event_push_to_intercom_post_save


class UserModel(AbstractUser, IntercomUserMixin):
    pass


class IntercomEvent(AbstractIntercomEvent):
    TYPE_EXAMPLE_EVENT = "example_event"
    TYPE_GENERIC = "generic"

    LABEL_EXAMPLE_EVENT = _("example event")
    LABEL_GENERIC = _("generic event")

    EVENT_TYPES = (
        (TYPE_EXAMPLE_EVENT, LABEL_EXAMPLE_EVENT),
        (TYPE_GENERIC, LABEL_GENERIC)
    )

    type = models.CharField(max_length=100, choices=EVENT_TYPES)

    def get_intercom_data(self):
        data = super(IntercomEvent, self).get_intercom_data()
        if self.type == IntercomEvent.TYPE_EXAMPLE_EVENT:
            data["metadata"] = {
                "text_content": self.text_content,
                # anything more you want
            }
        elif self.type in [
            IntercomEvent.TYPE_GENERIC,
            # some other types can be added
        ]:
            data["metadata"] = {
                "text_content": self.text_content,  # text, depending on the object
                # type of content (topic, session, what to do, etc)
                "type": self.content_type.name if self.content_type else "",
                "id": self.object_id if self.object_id else "",  # id of object from type
            }
        else:
            raise UnsupportedIntercomEventType

        return data


post_save.connect(account_post_save, sender=UserModel)
post_save.connect(intercom_event_push_to_intercom_post_save, sender=IntercomEvent)
