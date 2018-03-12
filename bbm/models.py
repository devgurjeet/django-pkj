from django.db import models

class Pins(models.Model):
    pin = models.CharField(max_length=25)

    def __str__(self):
        return self.pin

    class Meta:
        verbose_name_plural = "pins"


class PinMeta(models.Model):
    meta_key = models.CharField(max_length=100)
    meta_value = models.CharField(max_length=500)
    pin = models.ForeignKey(Pins, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pin) +"|" + str(self.meta_key)


class Contacts(models.Model):
    pin = models.ForeignKey(
        Pins, related_name='contact_set'
    )
    contact = models.ForeignKey(
        Pins, related_name='to_contact_set'
    )
    #
    # def __unicode__(self):
    #     return u'%s, %s' % (
    #         self.from_pin.id,
    #         self.to_pin.id
    #     )

    def __str__(self):
        return self.pin.pin

    class Meta:
        unique_together = (('pin', 'contact'),)
        verbose_name_plural = "contacts"

