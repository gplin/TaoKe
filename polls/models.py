import datetime
from django.utils import timezone
from django.db import models

class PollManager(models.Manager):
    def get_by_natural_key(self,question):
        return self.get(question=question)


class Poll(models.Model):
    objects = PollManager()

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date pulished')
    
    def __unicode__(self):
        return self.question

    def natural_key(self):
        return self.question
    
    def was_published_recently(self):
        now = timezone.now()
        return now > self.pub_date >= now-datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text