# -*- coding: utf-8 -*-
'''
Created on May 13 2013
contains the db models
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''


#===============================================================================
# begin imports
#===============================================================================

from django.db import models
import datetime


#===============================================================================
# end imports
#===============================================================================


#===============================================================================
# begin constants
#===============================================================================


#===============================================================================
# end constants
#===============================================================================


#===============================================================================
# begin nerdeez models
#===============================================================================

class NerdeezModel(models.Model):
    '''
    this class will be an abstract class for all my models
    and it will contain common information
    '''
    creation_date = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0))
    modified_date = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0), auto_now=True)
    
    class Meta:
        abstract = True
        
class University(NerdeezModel):
    '''
    this model represents a university
    contains general information
    '''
    title = models.CharField(max_length = 250, blank=False, null=False)
    description = models.CharField(max_length = 1000, null=True, blank=True, default="")
    image = models.CharField(max_length = 250, null=True, blank=True, default="")
    website = models.CharField(max_length = 250, null=True, blank=True, default="")
    
    def __unicode__(self):
        return u'%s' % (self.title)
        
#===============================================================================
# end nerdeez models
#===============================================================================