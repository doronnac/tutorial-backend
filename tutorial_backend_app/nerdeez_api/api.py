
'''
Created on May 13, 2013
the rest api is defined here
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from nerdeez_backend_app.models import University
from tastypie import fields

#===============================================================================
# end imports
#===============================================================================


#===============================================================================
# begin security resource
#===============================================================================



#===============================================================================
# end security resource
#===============================================================================


#===============================================================================
# begin rest resources
#===============================================================================



class NerdeezResource(ModelResource):
    '''
    abstract class with common attribute common to all my rest models
    '''
    class Meta:
        allowed_methods = ['get']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()

  
#===============================================================================
# begin model resources
#===============================================================================


class UniversityResource(NerdeezResource):
    '''
    the rest api for the university model is defined here
    '''
    class Meta(NerdeezResource.Meta):
        allowed_methods= ['get', 'post', 'put', 'delete'] #put and delete only added for testing
        queryset = University.objects.all()
    
    def get_object_list(self, request):
        '''
        search group logic
        '''
        object_list = super(UniversityResource, self).get_object_list(request)
        ids = []
        req = request.GET.get('search')
        if req != None:
            search_object_list = University.search(req)
            [ids.append(obj.id) for obj in search_object_list]
        if len(ids) > 0:
            object_list = object_list.filter(id__in=ids)
        return object_list
                   
#===============================================================================
# end model resources
#===============================================================================

#===============================================================================
# end rest resources
#===============================================================================